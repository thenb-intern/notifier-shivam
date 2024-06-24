## Sms Applications

SMS management system

#### License

mit
# API Key and Secret Generation

This document outlines the process for generating an API key and secret for users. The API key identifies the user, while the API secret validates the request. Together, they form a token that can be used for API requests.

## Methods for Generating API Keys and Secrets

API keys and secrets can be generated via three methods:
1. **Web Interface**
2. **Command Line**
3. **Remote Procedure Call (RPC)**

### 1. Web Interface

To generate the API key and secret via the web interface:

1. Log in to the web interface.
2. Navigate to `User -> Api Access -> Generate Keys`.

### 2. Command Line

To generate the API key and secret from the command line, use the following command:

```sh
bench execute frappe.core.doctype.user.user.generate_keys --args ['user_name']
