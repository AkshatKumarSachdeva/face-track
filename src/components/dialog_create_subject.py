import streamlit as st
from src.database.db import create_subject
@st.dialog("Create New Subject")
def create_subject_dialog(teacher_id):
    st.markdown("""
        <style>
            /* Dialog background and all text */
            [data-testid="stDialog"] {
                color: var(--text-color) !important;
            }

            /* Dialog title and all headings */
            [data-testid="stDialog"] h1,
            [data-testid="stDialog"] h2,
            [data-testid="stDialog"] h3,
            [data-testid="stDialog"] p,
            [data-testid="stDialog"] label,
            [data-testid="stDialog"] span,
            [data-testid="stDialog"] .stMarkdown,
            [data-testid="stDialog"] .stMarkdown p,
            [data-testid="stDialog"] [data-testid="stCaptionContainer"] {
                color: var(--text-color) !important;
                opacity: 1 !important;
            }

            /* Input labels */
            [data-testid="stDialog"] .stTextInput label {
                color: var(--text-color) !important;
                font-weight: 600 !important;
            }

            /* Input text */
            [data-testid="stDialog"] input {
                color: var(--text-color) !important;
                caret-color: var(--text-color) !important;
            }

            /* Input placeholder */
            [data-testid="stDialog"] input::placeholder {
                color: var(--text-color) !important;
                opacity: 0.55 !important;
            }

            /* Buttons */
            [data-testid="stDialog"] button {
                color: var(--text-color) !important;
            }

            /* Success, warning and error messages */
            [data-testid="stDialog"] [data-testid="stAlert"] p {
                color: inherit !important;
            }

            /* Code blocks */
            [data-testid="stDialog"] [data-testid="stCode"] {
                opacity: 1 !important;
            }

        </style>
    """, unsafe_allow_html=True)
    st.write("Enter the details of new subject:")
    sub_id = st.text_input(
        'Subject Code',
        placeholder='CS24101',
        key='create_subject_code'
    )
    sub_name = st.text_input(
        'Subject Name',
        placeholder='Artificial Intelligence',
        key='create_subject_name'
    )
    sub_section = st.text_input(
        'Section',
        placeholder='A',
        key='create_subject_section'
    )
    if st.button(
        'Create Subject Now!',
        type='primary',
        width='stretch',
        key='create_subject_submit'
    ):
        if not sub_id.strip() or not sub_name.strip() or not sub_section.strip():
            st.warning('Please fill all the fields!')
            return
        try:
            create_subject(
                sub_id,
                sub_name,
                sub_section,
                teacher_id
            )
            st.success("Subject Created Successfully!")
            st.rerun()
        except Exception as e:
            error_message = str(e).lower()
            if (
                'unique_subject_code_section' in error_message
                or 'duplicate key' in error_message
                or '23505' in error_message
            ):
                st.error(
                    f"{sub_id.upper()} - Section {sub_section.upper()} "
                    "already exists!"
                )
            else:
                st.error(f"Unable to create subject: {str(e)}")
