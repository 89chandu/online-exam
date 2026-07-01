import streamlit as st

from auth import Auth
from student import Student
from questions import Question
from test import Test
from result import Result

st.set_page_config(
    page_title="Online exam System",
    page_icon="📝",
    layout="wide"
)

# session

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "user" not in st.session_state:
    st.session_state.user = None

if "page" not in st.session_state:
    st.session_state.page = "Login"        

def logout():
    st.session_state.logged_in = False
    st.session_state.user = None
    st.session_state.page = "Login"

    st.rerun()

# Login / Register

if not st.session_state.logged_in:
    st.title("📝 Online Exam System ") 

    option = st.sidebar.radio(
        "Menu",
        [
            "Login",
            "Register"
        ]
    )


    # Login Screen

    if option == "Login":

        st.subheader("Student / Admin Login")
        email = st.text_input("Email")

        password = st.text_input(
            "Password",
            type = "password"
        )

        if st.button("Login"):

            user = Auth.login(
                email,
                password
            )

            if user:
                st.session_state.logged_in = True
                st.session_state.user = user
                st.success(

                    "Login Success"
                    
                )
                st.rerun()

            else:

                st.error(
                    "Invalid email or password"
                )
                

     #Register

    else:
        st.subheader("Student Registration")

        student_id = st.number_input(
            "Student ID",
            min_value=1
        )

        name = st.text_input("Name")
        email = st.text_input("Email")
        password = st.text_input(
            "Password",
            type='password'
        )

        if st.button("Register"):

            success ,message = Student.register(
                student_id,
                name,
                email,
                password
            )

            if success:
                st.success(message)

            else:
                st.error(message)  


#After Login

    user = st.session_state.user


    if user is None:
        st.error("please login first")
        st.stop()

    st.sidebar.success(
        f"{user['name']}"
        )   

    st.sidebar.write(
        "Role :", user["role"]
        
        )

    if st.sidebar.button("Logout"):
        logout()


# Routing
# 

if user["role"] == "admin":
    menu = st.sidebar.selectbox(
        "Admin Menu ",

        [
            "Dashboard",
            "Add Question",
            "View Question"
            "Create Question"
        ]
    )


                


