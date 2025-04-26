import streamlit as st

st.title("Unit Converter")
units = {
    "Mass": {"Kilograms": 1, "Grams": 0.001, "Milligrams": 0.000001, "Ounces": 0.0283495},
    "Length": {"Meters": 1, "Kilometers": 1000, "Feets": 0.3048, "Centimeters": 0.01, "Millimeters": 0.001, "Miles": 1609.34, "Inches": 0.0254},
    "Speed" : {"Meters/s": 1, "Kilometers/hr": 3.6, "Miles/hr": 2.23694, "Feets/s": 3.281},
    "Time" : {"Hours": 1, "Minutes": 60, "Seconds": 3600},
    "Temperature": {"Kelvin":"Kelvin", "Celsius":"Celsius", "Fahrenheit": "Fahrenheit"}
    }
category = st.selectbox("Select a category: ", list(units.keys()))
from_unit= st.selectbox("To", list(units[category].keys()))
to_unit = st.selectbox("From", list(units[category].keys()))
value = st.number_input("Enter the value: ")
if category != "Temperature":
    if from_unit and to_unit:
        baseValue = value * units[category][from_unit]
        result = baseValue / units[category][to_unit]
else:
    if from_unit == "Kelvin":
        if to_unit == "Celsius":
            result = value - 273.15
        elif to_unit == "Fahrenheit":
            result = (value - 273.15) * 9/5 + 32
        else:
            result = value
    elif from_unit == "Celsius":
        if to_unit == "Kelvin":
           result = value + 273.15 
        elif to_unit == "Fahrenheit":
            result = (value * 9/5) + 32
        else: 
            result = value
    elif from_unit == "Fahrenheit":
        if to_unit == "Celsius":
            result = (value * 5/9) - 32
        elif to_unit == "Kelvin":
            result = (value - 32) * 5/9 + 273.15
        else:
            result = value

if result is not None:
    st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")