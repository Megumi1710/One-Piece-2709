import streamlit as st
import pandas as pd

# Title
st.title("Student Information App")

# Sidebar
st.sidebar.header("Menu")
option = st.sidebar.selectbox(
    "Choose an option",
    ["Home", "Student Details", "Charts"]
)

# Home Page
if option == "Home":
    st.header("Welcome")
    st.write("This is an interactive Streamlit application.")

# Student Details Page
elif option == "Student Details":

    st.header("Student Details Form")

    # User Inputs
    name = st.text_input("Enter your name")
    age = st.number_input("Enter your age", 1, 100)
    clas = st.selectbox("Select Class", ["11th", "12th"])
    marks = st.slider("Enter your marks", 0, 100)

    hobby = st.checkbox("Do you like Coding?")

    # Button
    if st.button("Submit"):

        st.success("Form Submitted Successfully!")

        st.write("### Student Information")
        st.write("Name:", name)
        st.write("Age:", age)
        st.write("Class:", clas)
        st.write("Marks:", marks)

        if hobby:
            st.write("Hobby: Coding")

# Charts Page
elif option == "Charts":

    st.header("Student Marks Chart")

    data = pd.DataFrame({
        "Subjects": ["Math", "Science", "English", "Computer"],
        "Marks": [85, 90, 78, 95]
    })

    st.write(data)

    st.bar_chart(data.set_index("Subjects"))
