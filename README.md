🫀 Heart Stroke Prediction App
A machine learning web application that predicts the risk of heart disease based on clinical parameters including ECG results, cholesterol levels, blood pressure, and exercise-related indicators.

🚀 Live Demo

Click here to view the app (replace with your Streamlit URL after deployment)


📌 About the Project
Heart disease is one of the leading causes of death worldwide. Early detection can save lives. This project uses a trained machine learning classifier to predict whether a patient is at risk of heart disease based on their clinical data — all through a simple, interactive web interface.

🧠 Features

Interactive web interface built with Streamlit
Trained on a real-world heart disease dataset
Instant prediction with a single click
Clean and user-friendly UI


📊 Input Features
FeatureDescriptionAgeAge of the patientSexMale or FemaleChest Pain TypeASY, ATA, NAP, or TAResting BPResting blood pressure (mm Hg)CholesterolSerum cholesterol level (mg/dL)Fasting Blood SugarWhether fasting blood sugar > 120 mg/dLResting ECGNormal, ST abnormality, or LVHMax Heart RateMaximum heart rate achievedExercise AnginaChest pain induced by exercise (Yes/No)OldpeakST depression induced by exerciseST SlopeSlope of the peak exercise ST segment

🛠️ Tech Stack

Python
Scikit-learn — ML model training
Pandas & NumPy — Data processing
Streamlit — Web application framework


⚙️ How to Run Locally

Clone the repository

bash   git clone https://github.com/YOUR_USERNAME/heart-stroke-prediction.git
   cd heart-stroke-prediction

Install dependencies

bash   pip install -r requirements.txt

Run the app

bash   streamlit run app.py

📁 Project Structure
heart-stroke-prediction/
│
├── app.py                  # Main Streamlit application
├── model.pkl               # Trained ML model
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation

👨‍💻 Author
Zeeshan Ali — @codeByShan

📄 License
This project is open source and available under the MIT License.