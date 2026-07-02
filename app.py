import streamlit as st

from auth import Auth
from student import Student
from questions import Question
from test import Test
from result import Result

st.set_page_config(
    page_title="Online Exam System",
    page_icon="📝",
    layout="wide"
)

# ---------------- SESSION ----------------

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "user" not in st.session_state:
    st.session_state.user = None

if "page" not in st.session_state:
    st.session_state.page = "Login"


# ---------------- LOGOUT ----------------

def logout():
    st.session_state.logged_in = False
    st.session_state.user = None
    st.session_state.page = "Login"
    st.rerun()


# =====================================================
# LOGIN / REGISTER
# =====================================================

if not st.session_state.logged_in:

    st.title("📝 Online Exam System")

    option = st.sidebar.radio(
        "Menu",
        [
            "Login",
            "Register"
        ]
    )

    # ---------------- LOGIN ----------------

    if option == "Login":

        st.subheader("Student / Admin Login")

        email = st.text_input("Email")

        password = st.text_input(
            "Password",
            type="password"
        )

        if st.button("Login"):

            user = Auth.login(email, password)

            if user:

                st.session_state.logged_in = True
                st.session_state.user = user

                st.success("Login Success")

                st.rerun()

            else:

                st.error("Invalid Email or Password")

    # ---------------- REGISTER ----------------

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
            type="password"
        )

        if st.button("Register"):

            success, message = Student.register(
                student_id,
                name,
                email,
                password
            )

            if success:
                st.success(message)

            else:
                st.error(message)

    # IMPORTANT
    st.stop()


# =====================================================
# AFTER LOGIN
# =====================================================

user = st.session_state.user

if user is None:
    st.error("Please Login First")
    st.stop()


st.sidebar.success(f"👋 {user['name']}")

st.sidebar.write(
    "Role :",
    user["role"]
)

if st.sidebar.button("Logout"):
    logout()


# =====================================================
# ROUTING
# =====================================================

if user["role"] == "admin":

    menu = st.sidebar.selectbox(

        "Admin Menu",

        [
            "Dashboard",
            "Add Question",
            "View Question",
            "Create Test",
            "View Test",
            "View Results"
        ]
    )

else:

    menu = st.sidebar.selectbox(

        "Student Menu",

        [
            "Dashboard",
            "Available Tests",
            "My Results"
        ]
    )


# =====================================================
# DASHBOARD
# =====================================================

if menu == "Dashboard":

    st.title("Admin Dashboard")

    st.success(f"Welcome {user['name']}")

    st.write(f"Role : {user['role']}")

    questions = Question.get_all_questions()
    students = Student.get_all_students()
    tests = Test.get_all_tests()
    results = Question.get_all_questions()


    c1,c2 = st.columns(2)

    with c1:

        st.metric(
            "Total Students",
            len(students)
        )

        st.metric(
            "Total Questions",
            len(questions)

        )

    with c2:


        st.metric(
            "Total Tests",
            len(tests)
        )

        st.metric(
            "Results Published",
            len(results)
        )
elif menu == "Add Question":

    st.title("➕ Add Question")

    with st.form("question_form"):

        question_id = st.number_input(
            "Question ID",
            min_value=1,
            step=1
        )

        question = st.text_area(
            "Question"
        )

        option_a = st.text_input(
            "Option A"
        )

        option_b = st.text_input(
            "Option B"
        )

        option_c = st.text_input(
            "Option C"
        )

        option_d = st.text_input(
            "Option D"
        )

        correct_answer = st.selectbox(
            "Correct Answer",
            [
                option_a,
                option_b,
                option_c,
                option_d

            ]
        )

        marks = st.number_input(
            "Marks",
            min_value=1,
            value=1
        )

        submit = st.form_submit_button(
            "Save Question"
        )

        if submit:

            success , message = Question.add_question(
                question_id,
                question,
                option_a,
                option_b,
                option_c,
                option_d,
                correct_answer,
                marks
                
            )

            if success:
                st.success(message)

            else:
                st.error(message)    

elif menu == "View Question":

    st.title("View Question")








