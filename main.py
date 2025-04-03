import streamlit as st

# st.title("Unit Converter")

def convert_units ( value: float, value_from : str , unit_to : str) :
    if value_from == "kilometers" and unit_to == "meters":
        return value * 1000
    elif value_from == "meters" and unit_to == "kilometers":
         return value * 0.001
    elif value_from == "grams" and unit_to == "kilograms":
         return value * 1000
    elif value_from == "kilograms" and unit_to == "grams":
        return value * 10000
    else :
        return "invalid Unit"

result1 = convert_units(1.5, "kilograms", "grams")
print(result1)
