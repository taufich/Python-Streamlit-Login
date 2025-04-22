import streamlit as st

USER_CREDENTIALS = {
    "admin": "admin123",
    "user" : "pass",
    "hr"   : "hrpass"
}


def login():
    st.title("Simple Login Form")
    

    username = st.text_input("username")
    password = st.text_input("password", type="password")

    if st.button("Login"):
        if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
            st.success("Welcome " + username)
        else:
            st.error("Invalid username or password.")





if __name__ == "__main__":
    login()



