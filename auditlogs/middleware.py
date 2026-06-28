import threading
import json
from django.utils.deprecation import MiddlewareMixin
from auditlogs.models import AuditLog

class AuditLogMiddleware(MiddlewareMixin):
    def process_request(self, request):
        request._body_data = request.body
        
    def process_response(self, request, response):
        if request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            # Try to get the user
            user = request.user if hasattr(request, 'user') and request.user.is_authenticated else None
            
            # Module logic based on path
            path = request.path
            path_parts = [p for p in path.split('/') if p]
            module = path_parts[1] if len(path_parts) > 1 else 'general'
            
            # Action logic based on method and status
            action = f"{request.method}_{response.status_code}"
            if request.method == 'POST' and 'login' in path:
                action = 'LOGIN'
            
            # Extract IP
            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            if x_forwarded_for:
                ip_address = x_forwarded_for.split(',')[0]
            else:
                ip_address = request.META.get('REMOTE_ADDR')

            # Descriptive text
            description = f"{request.method} request to {path}"
            if user:
                description += f" by {user.get_full_name()} ({user.member_no})"
            else:
                description += " by anonymous user"
            
            if response.status_code >= 400:
                description += f" failed with status {response.status_code}"
            else:
                description += f" succeeded with status {response.status_code}"
                
            def _create_log():
                AuditLog.objects.create(
                    user=user,
                    action=action,
                    module=module,
                    description=description,
                    ip_address=ip_address
                )
                
            thread = threading.Thread(target=_create_log)
            thread.start()
            
        return response
