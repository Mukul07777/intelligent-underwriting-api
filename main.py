from fastapi import FastAPI, UploadFile, File
from document_analysis import extract_text_from_pdf
from image_analysis import analyze_image
from compliance_checker import check_compliance
from risk_assessment import calculate_risk

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Property Underwriting API is Running!"}

@app.post("/underwrite/")
async def underwrite_document(file: UploadFile = File(...)):
    if file.filename.endswith(".pdf"):
        text = extract_text_from_pdf(file.file)
    else:
        text = analyze_image(file.file)

    compliance_result = check_compliance(text)
    risk_score = calculate_risk(text)

    return {
        "extracted_text": text,
        "compliance": compliance_result,
        "risk_score": risk_score
    }
