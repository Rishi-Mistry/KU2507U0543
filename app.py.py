import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="Rishi Mistry - Final Project", page_icon="✈️", layout="wide")

# --- MAIN SECTION ---
st.title("✈️ Customer Churn Prediction")
st.write("Random Forest Classifier | B.Tech Gen AI – Final Project")

st.divider()

# --- MODEL METRICS ---
col1, col2 = st.columns(2)
with col1:
    st.write("Model")
    st.write("## Random Forest")
    st.write("AUC-ROC")
    st.write("## ~0.90")
with col2:
    st.write("Training Accuracy")
    st.write("## ~87%")

st.divider()

# --- WELCOME SECTION ---
st.write("👋 Welcome to the Customer Churn Predictor")
st.write(
    """
    This application uses a Random Forest machine learning model trained on travel customer data 
    to predict whether a customer is at risk of churning.
    """
)

st.subheader("How to use:")
st.write(
    """
    1. Fill in the customer details in the sidebar on the left.
    2. Click the "Predict Churn" button.
    3. View the prediction result, probability scores, and business recommendations.
    """
)

st.divider()

# --- DATASET FEATURES TABLE ---
st.write("📊 Dataset Features")

features_data = [
    ["Age", "Numeric", "Customer age (27–38)"],
    ["FrequentFlyer", "Categorical (Yes/No)", "Whether the customer is a frequent flyer"],
    ["AnnualIncomeClass", "Categorical (4 classes)", "Annual income bracket of the customer"],
    ["ServicesOpted", "Numeric (1–6)", "Number of travel services opted by customer"],
    ["AccountSyncedToSocialMedia", "Categorical (Yes/No)", "Whether account is synced to social media"],
    ["BookedHotelOrNot", "Categorical (Yes/No)", "Whether the customer has booked a hotel"],
]

# Define column headers
cols = st.columns([2, 2, 4])
with cols[0]: st.write("**Feature**")
with cols[1]: st.write("**Type**")
with cols[2]: st.write("**Description**")

# Populate table rows
for row in features_data:
    cols = st.columns([2, 2, 4])
    cols[0].write(row[0])
    cols[1].write(row[1])
    cols[2].write(row[2])

st.divider()

# --- FOOTER ---
st.write("Built with ❤️ using Streamlit | B.Tech Gen AI – Customer Churn Prediction Project")