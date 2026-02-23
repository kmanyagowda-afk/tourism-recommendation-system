import streamlit as st
import pickle
import pandas as pd

# Load Model
model = pickle.load(open("travel_model.pkl", "rb"))
le_interest = pickle.load(open("interest_encoder.pkl", "rb"))
le_mode = pickle.load(open("mode_encoder.pkl", "rb"))

st.title(" Smart Tourist Recommendation System")

st.write("Enter your details to get personalized attraction recommendations.")

# User Inputs
age = st.slider("Age", 18, 60)
budget = st.number_input("Budget (INR)", 5000, 50000)
interest = st.selectbox("Interest Type", ["Beach", "Historical", "Religious", "Adventure", "Nature"])

# Encode interest
interest_encoded = le_interest.transform([interest])[0]

# Prediction
if st.button("Get Recommendation"):
    input_data = pd.DataFrame([[age, budget, interest_encoded]],
                              columns=["Age", "Budget", "Interest"])

    prediction = model.predict(input_data)[0]
    travel_mode = le_mode.inverse_transform([prediction])[0]

    st.success(f"Recommended Travel Mode: {travel_mode}")

    # Rule-based Attraction Recommendation
    if interest == "Beach":
        st.write("Suggested Place: Goa")
    elif interest == "Historical":
        st.write(" Suggested Place: Taj Mahal")
    elif interest == "Religious":
        st.write(" Suggested Place: Varanasi")
    elif interest == "Adventure":
        st.write("Suggested Place: Manali")
    elif interest == "Nature":
        st.write(" Suggested Place: Coorg")