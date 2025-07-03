# ❄️ ICE: Intelligent Credit Evaluator

> A smart AI-based system to evaluate and predict **loan approvals**, assess **approval probability**, and categorize **applicant risk** — all in real-time.

---

## 🚀 Demo

Upload applicant details → Get an instant decision.

Try the live app: [Hugging Face Space 🔗](https://huggingface.co/spaces/YourUsername/ICE)](https://huggingface.co/spaces/ravi86/ICE/tree/main)  


---

## 🧠 Features

- ✅ Predicts whether a **loan will be approved** or rejected  
- 📈 Shows **approval probability (%)**  
- ⚠️ Labels users as **High**, **Medium**, or **Low Risk**  
- 🧠 Trained using **Scikit-learn + XGBoost**  
- 💻 Built with **Gradio UI**  
- 🌐 Deployed on Hugging Face Spaces  

---

## 🗃️ Input Fields

- Gender  
- Married  
- Education  
- Self-Employed  
- Applicant Income  
- Coapplicant Income  
- Loan Amount  
- Loan Term  
- Credit History  
- Property Area  

---

## 📦 Tech Stack

- Python 3.10+  
- Scikit-learn  
- XGBoost  
- Gradio  
- NumPy, Joblib  

---

## 📊 Model Details

- Model file: `model_loan_predector.pkl`  
- Trained using: RandomForestClassifier / XGBoost  
- Accuracy: ~86% (on test set)  
- Feature engineering: Label encoding, scaling, missing value handling  

---

## ⚙️ How to Run Locally
# Clone the repository
git clone [https://github.com/TRavi8688/ICE-Loan-Prediction](https://github.com/TRavi8688/Veltrix/tree/main).git
cd ICE-Loan-Prediction

# Install required dependencies
pip install -r requirements.txt

# Run the app
python app.py

Access the app at http://localhost:7860/


📄 Example Output

    Loan Status: ✅ Approved

    Approval Probability: 82.56%

    Risk Category: Low Risk

🔒 Privacy

All predictions are processed locally in memory.
No data is stored, tracked, or shared.
👨‍💻 Author

T. Ravi Kumar
📧 travikumartravikumar00@gmail.com
🔗 GitHub
🔗 LinkedIn

❄️ ICE — Predict Smart. Decide Better.
---

✅ Let me know if you'd like me to:
- Add badges (build, license, Hugging Face)
- Auto-generate this file as a downloadable `README.md`
- Or help write one for StyleAI Mirror too!
