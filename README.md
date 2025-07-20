# 🏡 Property Underwriting API

An AI-powered Property Underwriting system that automates property document analysis, image evaluation, compliance checking, and risk assessment to streamline insurance underwriting workflows.

---

## 🚀 Features
- 📄 **Document Analysis**: Extracts text from property-related PDF documents.
- 🖼️ **Image Analysis**: Evaluates property images for condition and value.
- ✅ **Compliance Checker**: Verifies property documents against compliance rules.
- 📊 **Risk Assessment**: Calculates risk scores based on property and compliance data.
- ⚡ **FastAPI Backend**: Provides a REST API for integration with any frontend or service.

---

## 🛠️ Setup Instructions

### 1. **Clone the Repository**

git clone https://github.com/your-username/property-underwriting-api.git
cd property-underwriting-api

***Create Virtual Environment
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows

***Install Dependencies
pip install -r requirements.txt

 Project Structure

property-underwriting-api/
│
├── main.py                 # FastAPI application entry point
├── document_analysis.py    # PDF document analysis
├── image_analysis.py       # Image evaluation
├── compliance_checker.py   # Compliance checks
├── risk_assessment.py      # Risk scoring
└── sample_data/            # Sample PDFs and images
5. Run the Application

python -m uvicorn main:app --reload
Visit: http://127.0.0.1:8000

API Docs: http://127.0.0.1:8000/docs

📋 API Endpoints
GET /: Health check
POST /underwrite/: Upload property document and image to get:
Extracted Document Text
Image Analysis Result
Compliance Status
Risk Score

📌 Example Usage (via API Docs)
Upload:
A PDF document (document)
A property image (image)
Get:

{
  "document_text": "Extracted text content from PDF...",
  "image_analysis": "Image is clear and property condition looks good.",
  "compliance": "Compliant",
  "risk_score": 30
}

✅ Future Enhancements
Integrate ML models for better image and text analysis
Add database storage for underwriting records
Enhance compliance rules engine
Frontend dashboard for easy interaction

