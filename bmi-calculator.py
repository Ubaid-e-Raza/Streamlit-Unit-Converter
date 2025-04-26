import streamlit as st

st.title('BMI Calculator')
weight_str = st.text_input('Enter your Weight in Kilograms: ')
col1, col2 = st.columns([2, 1])
with col1:
    height_str = st.text_input('Enter your height: ')
with col2:
    unit = st.selectbox("Unit",["Feet", "Inches"]).lower()
if weight_str and height_str:
    weight = float(weight_str)
    height = float(height_str)
    if unit == "inches":
        meter_height = float(height / 39.37)
    else:
        meter_height = float(height * 0.3048)   
    bmi = float(weight / meter_height**2)
    if bmi < 18.5:
        st.write(f"Your BMI is {bmi:.2f}, this is considered Underweight!")
    elif bmi >= 18.5:
        st.write(f"Your BMI is {bmi:.2f}, this is considered Normal!")
    elif bmi >= 25:
        st.write(f"Your BMI is {bmi:.2f}, which is considered Overweight!")
    elif bmi >= 30:
        st.write(f"Your BMI is {bmi:.2f}, this is considered Obese Class-I")
    elif bmi >= 35:
        st.write(f"Your BMI is {bmi:.2f}, this is considered Obese Class-II")
    elif bmi >= 40:
        st.write(f"Your BMI is {bmi:.2f}, this is considered Obese Class-III")
