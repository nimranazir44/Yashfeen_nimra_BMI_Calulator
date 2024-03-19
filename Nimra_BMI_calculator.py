import streamlit as st

def check_age(age):
    if age >= 18:
        st.success("Welcome! You have access to open the app.")
    else:
        st.error("Sorry, you are too young to use this app.")

def main():
    st.title("Age Verification App")
    user_age = st.number_input("Please enter your age:", min_value=0, max_value=150, step=1)
    if st.button("Check Age"):
        check_age(user_age)

if _name_ == "_main_":
    main()
