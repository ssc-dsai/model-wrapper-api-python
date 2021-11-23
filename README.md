# Model API Wrapper

Model API Wrapper, like the name suggest, is an API template that wraps a Machine Learning model. 

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
- Python 3 / Anaconda

### Installing
Clone the repository:
```
git clone https://gitlab.com/dsa8/model-wrapper-api.git
cd model-wrapper-api
```

Optionally (**recommended**), create and activate conda environment:
```
conda create -n modelapi  
conda activate modelapi
```

Install requirements:
```
pip install -r requirements.txt
```

Modify the .env.example file with secrets and save as `.env` in the root directory.

### Using the API Wrapper

To use this API you only need to modify the Model class in src/model.py

The class requires 3 things:
- A model property to store the active model
- A init method to activate/load the model
- A run method for your prediction code

FastAPI recommends that you use types to validate your requests.
Examples are already in src/model.py

## Running
You can now run the model locally:
```
cd src
uvicorn main:app --reload
```

By default, this will start the server on port 8000.


### Running unit tests
TODO

### TODO
Standard Reference: https://www.canada.ca/en/government/system/digital-government/modern-emerging-technologies/government-canada-standards-apis.html
- Testing code
- CI/CD Pipeline
- Add logger for monitoring
- Version API
- Provide point of contact
- Define an SLA up front – Each API should be accompanied with a clearly defined Service Level Agreement (SLA). At a minimum, the SLA should define the following:
    Support hours (e.g., 24/7, 9/5, coast to coast business hours)
    Service availability (e.g., 99%)
    Support response time (e.g., within the hour, 24 hours, best effort)
    Scheduled outages (e.g., nightly, weekly, every 2nd Sunday evening)
    Throughput limit (e.g., 100 requests per second per consumer)
    Message size limit (e.g., <1Mb per request)

## Security Checklist
- Enforce secure communications – Never send sensitive data over an insecure or unencrypted connection, and where possible non-sensitive data should also be sent over a secure connection. Enable TLS 1.2 or subsequent versions, in accordance with CSE guidance.

- Design APIs to be resistant to attacks – All APIs should be designed and implemented to be resistant to common API attacks such as buffer overflows and SQL injection. Treat all submitted data as untrusted and validate before processing. Leverage schema and data models for ensuring correct data validation.

- Protect access to APIs - Implement an access control scheme that protects APIs from being improperly invoked, including unauthorized function and data references. Always authenticate and authorize before any operation to ensure access to APIs are restricted to permitted individuals and/or systems. Use open standards such as OpenID Connect and Open Authorization 2.0 (OAuth 2.0) for RESTful APIs, and Security Assertion Markup Language 2.0 (SAML 2.0) for SOAP APIs. Ensure that the API key/secret is adequately protected. Open data APIs must be secured with an API key to allow for usage tracking and provide the ability to identify and prevent potential malicious use.

- Apply secure token management practices – Token-based authentication is strongly recommended and is mandatory for any APIs published to be consumed across the Government of Canada and/or externally. Use industry standard tokens; do not create custom tokens; and avoid using vendor proprietary token schemes. JSON Web Token (JWT) is required for RESTful API interactions. WS-Security SAML Token Profile is required for SOAP APIs. All access tokens must expire within a reasonable amount of time (i.e., less than 24 hours). In the case of SAML, the assertion expiry must be set to control the validity period of the entire authentication and authorization session.

- Use gateways and proxies instead of whitelists – When exposing APIs to the internet, use a secure gateway layer to provide a security control point instead of simply whitelisting inbound Internet Protocol addresses (IPs). The API Store’s gateway functionality may be used. When consuming external APIs, route flows through a forward (egress) proxy instead of using IP address whitelisting on the outbound firewall.

- Integrate security testing - Automate security testing to validate any new changes to API source code and to ensure robustness of requested changes. Assess the change impact and conduct testing accordingly.

- Audit access to sensitive data – Access to APIs dealing with sensitive and/or personal data must be logged for future audit and reviewed on a regular basis. Access logs must include as a minimum both the system and individual identifiers attempting to access the API along with the timestamp. Periodic audits of API access may be required depending on the nature of the data and its usage.

- Log and monitor for performance and activity – Track usage and monitor for suspicious activity including abnormal access patterns such as after-hours requests, large data requests, etc. Use logging standards (e.g. common event format) and integrate logs centrally. Identify dependencies and monitor for vulnerabilities, especially those for uploaded run-times that work as part of the API. Suspicious events must be sent to the appropriate security operations capability or authority in compliance with Government of Canada Cyber Security policies and Government of Canada Cyber Security Event Management Plan.
