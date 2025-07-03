import gradio as gr
import joblib
import numpy as np

# Load your model
model = joblib.load("model_loan_predector.pkl")

# Prediction function
def predict_loan(gender, married, education, self_employed, applicant_income, coapplicant_income,
                 loan_amount, loan_term, credit_history, property_area):

    # Convert inputs to numeric (Label encoding simulation)
    input_data = np.array([[
        1 if gender == "Male" else 0,
        1 if married == "Yes" else 0,
        1 if education == "Graduate" else 0,
        1 if self_employed == "Yes" else 0,
        float(applicant_income),
        float(coapplicant_income),
        float(loan_amount),
        float(loan_term),
        int(credit_history),
        {"Rural": 0, "Semiurban": 1, "Urban": 2}[property_area]
    ]])

    # Predict
    prediction = model.predict(input_data)[0]
    return "✅ Approved" if prediction == 1 else "❌ Not Approved"

# Gradio UI
iface = gr.Interface(
    fn=predict_loan,
    inputs=[
        gr.Radio(["Male", "Female"], label="Gender"),
        gr.Radio(["Yes", "No"], label="Married"),
        gr.Radio(["Graduate", "Not Graduate"], label="Education"),
        gr.Radio(["Yes", "No"], label="Self Employed"),
        gr.Number(label="Applicant Income"),
        gr.Number(label="Coapplicant Income"),
        gr.Number(label="Loan Amount"),
        gr.Number(label="Loan Term (in days)"),
        gr.Radio(["1", "0"], label="Credit History (1 = Good, 0 = Bad)"),
        gr.Radio(["Rural", "Semiurban", "Urban"], label="Property Area"),
    ],
    outputs=gr.Text(label="Loan Status Prediction"),
    title="Loan Approval Predictor App",
    description="Enter applicant details to predict whether the loan will be approved."
)

iface.launch()
