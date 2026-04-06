import streamlit as st
import pandas as pd
from sklearn.linear_model import LogisticRegression
# load dataset
data = pd.read_csv("placement.csv")
# features & target
X = data[['cgpa','iq']]
y = data['placement']
# train model
model = LogisticRegression()
model.fit(X, y)
# UI
st.title("Placement Predictor")

cgpa = st.number_input("Enter CGPA")
iq = st.number_input("Enter IQ")

if st.button("Predict"):
    input_data = pd.DataFrame([[cgpa, iq]], columns=['cgpa','iq'])
    result = model.predict(input_data)

    if result[0] == 1:
        st.success("Placed ✅")
    else:
        st.error("Not Placed ❌")