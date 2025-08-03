# AI Guard - Security & Compliance Suite

A comprehensive full-stack application for API security, compliance auditing, and AI threat simulation. This toolkit helps organizations assess, harden, and test their AI-powered applications against various security threats and compliance requirements.

## 🚀 Features

### 1. **Privacy Audit & Compliance Analysis**
- Analyze data flow descriptions for compliance gaps
- Generate detailed reports in JSON and Markdown formats
- Identify potential privacy and security vulnerabilities
- Download comprehensive audit reports

### 2. **API & Endpoint Hardening**
- **Rate Limiting**: Test and implement request rate limiting
- **Two-Factor Authentication (2FA)**: Setup and verify TOTP-based 2FA
- **CAPTCHA Integration**: Simulate CAPTCHA verification systems
- **Authentication Middleware**: Customizable auth token validation

### 3. **AI Threat Simulation & Security Testing**
- **AI Voice Cloning Attack Simulation**: Test voice-based authentication systems
- **Prompt Injection Attack Testing**: Validate prompt security measures
- **Data Poisoning Attack Simulation**: Test data integrity safeguards
- **Model Extraction Attack Testing**: Assess model protection mechanisms
- **Biometric Authentication Testing**: Simulate voice-based biometric systems
- **Endpoint Stress Testing**: Performance and security under load

### 4. **Incident Response & Reporting**
- Real-time security incident simulation
- Automated response generation
- Comprehensive reporting dashboard
- Downloadable security reports

## 🛠️ Technology Stack

- **Backend**: FastAPI (Python)
- **Frontend**: HTML5, CSS3, JavaScript
- **Templates**: Jinja2
- **Rate Limiting**: SlowAPI
- **Authentication**: PyOTP (TOTP-based 2FA)
- **Security**: Built-in CORS, rate limiting, and middleware

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd ai-guard-app
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

4. **Access the application**
   Open your browser and navigate to `http://localhost:8000`

## 📁 Project Structure

```
ai-guard-app/
├── main.py                 # FastAPI application entry point
├── requirements.txt        # Python dependencies
├── README.md              # This file
├── routers/               # API route modules
│   ├── audit.py          # Privacy audit endpoints
│   ├── hardening.py      # Security hardening endpoints
│   ├── testing.py        # Security testing endpoints
│   ├── response.py       # Incident response endpoints
│   └── reporting.py      # Reporting endpoints
├── utils/                 # Utility modules
│   ├── compliance.py     # Compliance analysis logic
│   └── report_generator.py # Report generation utilities
├── templates/            # HTML templates
│   └── index.html       # Main application interface
├── static/              # Static assets
│   ├── css/
│   │   └── style.css    # Application styles
│   └── js/
│       └── main.js      # Frontend JavaScript
└── reports_data/        # Generated reports storage
```

## 🔧 Configuration

### Rate Limiting
The application implements rate limiting with a default of 20 requests per minute per IP address. This can be configured in `main.py`.

### CORS Settings
CORS is configured to allow all origins for development. In production, restrict this to your frontend domain:

```python
origins = ["https://yourdomain.com"]  # Production setting
```

### Authentication
The application includes a dummy authentication middleware that can be replaced with real JWT validation or other authentication systems.

## 📊 API Endpoints

### Audit Module (`/audit`)
- `POST /audit/analyze` - Analyze data flow for compliance gaps

### Hardening Module (`/hardening`)
- `POST /hardening/rate-limit-test` - Test rate limiting
- `POST /hardening/setup-2fa` - Setup 2FA
- `POST /hardening/verify-2fa` - Verify 2FA token
- `POST /hardening/captcha-test` - Test CAPTCHA integration

### Testing Module (`/testing`)
- `POST /testing/voice-clone` - Simulate voice cloning attack
- `POST /testing/prompt-injection` - Test prompt injection
- `POST /testing/data-poisoning` - Simulate data poisoning
- `POST /testing/model-extraction` - Test model extraction
- `POST /testing/stress-test` - Run stress tests
- `POST /testing/biometric-auth` - Test biometric authentication

### Response Module (`/response`)
- `POST /response/simulate-incident` - Simulate security incident
- `GET /response/status` - Get response status

### Reporting Module (`/reporting`)
- `GET /reports/download/{report_id}/{format}` - Download reports

## 🔒 Security Features

- **Rate Limiting**: Prevents abuse and DDoS attacks
- **CORS Protection**: Configurable cross-origin resource sharing
- **Authentication Middleware**: Extensible authentication system
- **Input Validation**: Comprehensive input sanitization
- **Error Handling**: Secure error responses without information leakage

## 🧪 Testing

The application includes built-in security testing capabilities:

1. **Manual Testing**: Use the web interface to test various security features
2. **API Testing**: Use tools like Postman or curl to test endpoints directly
3. **Automated Testing**: Extend the application with automated test suites

## 📈 Usage Examples

### Running a Privacy Audit
1. Navigate to the "Initial Assessment & Privacy Audit" section
2. Enter your data flow description
3. Click "Analyze for Compliance Gaps"
4. Review results and download reports

### Testing Rate Limiting
1. Go to the "API & Endpoint Hardening" section
2. Click "Test Rate-Limited Endpoint" 6 times quickly
3. Observe the 429 error response

### Setting Up 2FA
1. Click "Setup 2FA" to generate a QR code
2. Scan with your authenticator app
3. Enter the 6-digit token
4. Click "Verify Token"

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## ⚠️ Disclaimer

This application is designed for educational and testing purposes. The security simulations are meant to help understand potential vulnerabilities and should not be used for malicious purposes. Always ensure you have proper authorization before testing security measures on production systems.

## 🆘 Support

For support and questions:
- Create an issue in the repository
- Check the documentation in the code comments
- Review the API documentation at `/docs` when the application is running

## 🔄 Version History

- **v1.0.0**: Initial release with core security and compliance features
