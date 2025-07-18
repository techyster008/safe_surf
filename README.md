URL Phishing and Scam Detector
This repository contains a Flask-based web application that serves as a URL phishing and scam detector. It provides a robust API to analyze URLs and determine their potential risk level by performing a series of security checks.

Features
Base64 URL Decoding: Automatically decodes URLs that may be obfuscated using Base64 encoding.

Domain Whitelisting: Skips analysis for a pre-defined list of well-known and trusted domains.

Domain Reputation Check: Integrates with the VirusTotal API to check if a domain has been flagged as malicious.

SSL Certificate Validation: Verifies the validity of the SSL certificate, a key indicator of a legitimate website.

Google Safe Browse Integration: Uses the Google Safe Browse API to check for known phishing or malware sites.

Whois Lookup: Performs a basic check on the domain's creation date to identify newly registered, potentially suspicious domains.

Containerized Environment: The application is configured to run inside a Docker container, ensuring a consistent and isolated environment.

Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

Prerequisites
You need to have Docker and Docker Compose installed on your machine.

Install Docker

Installation
Clone the repository:

Bash

git clone https://github.com/your-username/your-repository-name.git
cd your-repository-name
Build and run the Docker container:

Bash

docker-compose up --build
This command builds the Docker image and starts the Flask server, which will be accessible at http://localhost:5000.

API Endpoint
The application exposes a single API endpoint for URL analysis.

POST /analyze
Analyzes a URL and returns a safety score.

Request
Method: POST

Endpoint: /analyze

Headers: Content-Type: application/json

Body:

JSON

{
  "url": "https://www.example.com"
}
Response
Success (200 OK):

JSON

{
  "safe": true
}
Error:

JSON

{
  "safe": false
}
or an error message string.

Running Tests
To run the unit tests for the application, you can execute the following command inside the container or after installing the dependencies locally:

Bash

pytest
Contributing
We welcome contributions! Please feel free to submit a pull request or open an issue for any bugs or feature requests.

License
This project is licensed under the MIT License. See the LICENSE file for more details.
