import streamlit as st
import joblib
import pandas as pd
import os

# Define the path to the model file
model_path = os.path.join(os.getcwd(), 'xgboost_model.pkl')

# Load the model
model = joblib.load(model_path)

# Streamlit app title


st.title("Customer Churn Prediction 📈")
st.markdown("""
Welcome to the Bank Customer Exit Prediction Tool! This application predicts the likelihood of a customer exiting the bank based on their profile and account features.
Enter the relevant customer details below, and our model will assess whether the customer is likely to stay or leave.
""")
image_path = os.path.join(os.getcwd(), 'exit_img.png')
st.image(image_path, width=700)


# Create input fields for all required features
age = st.number_input("Age", min_value=18, max_value=100)
credit_score = st.number_input("Credit Score", min_value=300, max_value=850)
balance = st.number_input("Balance", min_value=0.0)
num_of_products = st.number_input("Number of Products", min_value=1, max_value=5)

# Input fields for boolean values
has_cr_card = st.selectbox("Has Credit Card", options=["No", "Yes"])  # User selects Yes/No
is_active_member = st.selectbox("Is Active Member", options=["No", "Yes"])  # User selects Yes/No
complain = st.selectbox("Complain", options=["No", "Yes"])  # User selects Yes/No

# Convert Yes/No to 1/0
has_cr_card = 1 if has_cr_card == "Yes" else 0
is_active_member = 1 if is_active_member == "Yes" else 0
complain = 1 if complain == "Yes" else 0

# Continue with other input fields
estimated_salary = st.number_input("Estimated Salary", min_value=0.0)
point_earned = st.number_input("Points Earned", min_value=0.0)
tenure = st.number_input("Tenure (in years)", min_value=0)

# Button for prediction
if st.button("Predict"):
    # Create a DataFrame from user input
    input_data = pd.DataFrame({
        'Age': [age],
        'CreditScore': [credit_score],
        'Balance': [balance],
        'NumOfProducts': [num_of_products],
        'HasCrCard': [has_cr_card],
        'IsActiveMember': [is_active_member],
        'EstimatedSalary': [estimated_salary],
        'Point Earned': [point_earned],
        'Tenure': [tenure],
        'Complain': [complain]  # Ensure to include this if your model uses it
    })

    # Make prediction
    prediction = model.predict(input_data)

    # Show prediction result
    if prediction[0] == 1:
        st.success("Prediction: The customer is likely to churn.")
    else:
        st.success("Prediction: The customer is likely to stay.")
