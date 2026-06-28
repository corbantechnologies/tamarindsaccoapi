# Tamarind Sacco Platform Documentation

This document outlines the core features and modules available within the Tamarind Sacco Platform. The system is designed to provide comprehensive financial management for Sacco operations, integrating both a robust backend API and an administrative/member portal.

## 1. Authentication & Role-Based Access Control (RBAC)
The platform enforces a strict security model with multi-tiered user roles, ensuring users only access what they are permitted to.
- **Superusers**: Highest level of access. Responsible for system monitoring, tracking audit logs, and managing top-level member tracking.
- **Sacco Admins**: Operational administrators who manage loans, savings, fees, and day-to-day Sacco activities.
- **Members**: End-users who can log in to view their savings, apply for loans, make payments, and manage personal profiles.
- **Onboarding & KYC**: Comprehensive member profiles tracking Next of Kin, employment details, and identity documents.

## 2. Comprehensive Loan Management
The loan module supports the full lifecycle of a loan, from application to final repayment.
- **Loan Products**: Administrators can configure various loan products with custom rules, interest rates, and limits.
- **Applications & Approvals**: Members can apply for loans. The system tracks the application status through approval workflows.
- **Guarantors**: Built-in support for guarantor profiles and guarantee requests, allowing members to secure their loans against other members' savings.
- **Disbursements & Repayments**: Automated tracking of loan disbursements and tracking of loan repayments.
- **Penalties**: Automated tracking of loan penalties for late payments.
- **Legacy Loans**: Specialized modules for onboarding and tracking existing/legacy loans and their historical payments.

## 3. Core Savings System
The system manages member savings with flexibility and accuracy.
- **Saving Types**: Configurable savings categories (e.g., normal savings, holiday funds).
- **Deposits**: Tracking of all member deposits into their savings accounts.
- **Withdrawals**: Secure processing and tracking of savings withdrawals.

## 4. Accounting & Financials Engine
A robust accounting backend ensures every transaction is accurately recorded in the general ledger.
- **General Ledger (GL) Accounts**: Standardized GL tracking.
- **Journal Entries & Batches**: Batch processing for journal entries to keep financial records balanced.
- **Financial Summaries**: Aggregated dashboards and reports for Sacco Admins.

## 5. Fee Management
Flexible tracking of various fees charged by the Sacco.
- **Fee Types**: Configuration for registration fees, late fees, processing fees, etc.
- **Fee Accounts & Payments**: Tracking member fee obligations and their corresponding payments.

## 6. Payments & M-Pesa Integration
Seamless transaction processing.
- **Global Transactions Ledger**: Centralized tracking for all monetary movements across savings, loans, and fees.
- **M-Pesa Integration**: Direct integration with the Safaricom Daraja API for automated mobile money deposits and loan disbursements.
- **Payment Accounts**: Management of the Sacco's internal bank or mobile money accounts.

## 7. Security & Audit Logging
To ensure compliance and accountability, the system maintains an immutable audit trail.
- **Audit Logs**: Every state-changing action (e.g., loan approvals, profile updates, password resets) is tracked.
- **Contextual Tracking**: Logs capture the exact action, the user responsible, the module affected, a highly descriptive summary of the event, and the IP address.
- **Superuser Monitoring**: Dedicated interfaces for Superusers to review the system's audit trail securely.