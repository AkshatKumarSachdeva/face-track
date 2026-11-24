import streamlit as st
from src.database.db import create_subject
@st.dialog("Create New Subject")
def create_subject_dialog(teacher_id):
            
    st.markdown("""
            <style>

            /* Apply theme-aware text color throughout the dialog */
            [data-testid="stDialog"],
            [data-testid="stDialog"] div,
            [data-testid="stDialog"] p,
            [data-testid="stDialog"] label,
            [data-testid="stDialog"] span,
            [data-testid="stDialog"] h1,
            [data-testid="stDialog"] h2,
            [data-testid="stDialog"] h3 {
                color: var(--text-color) !important;
            }

            /* Input fields */
            [data-testid="stDialog"] input,
            [data-testid="stDialog"] textarea {
                color: var(--text-color) !important;
                -webkit-text-fill-color: var(--text-color) !important;
                caret-color: var(--text-color) !important;
            }

            /* Input placeholders */
            [data-testid="stDialog"] input::placeholder,
            [data-testid="stDialog"] textarea::placeholder {
                color: var(--secondary-text-color) !important;
                opacity: 1 !important;
                -webkit-text-fill-color: var(--secondary-text-color) !important;
            }

            /* Widget labels */
            [data-testid="stDialog"] [data-testid="stWidgetLabel"] p {
                color: var(--text-color) !important;
            }

            /* Markdown text */
            [data-testid="stDialog"] [data-testid="stMarkdownContainer"] p {
                color: var(--text-color) !important;
            }

            /* Keep buttons readable */
            [data-testid="stDialog"] button p,
            [data-testid="stDialog"] button span {
                color: inherit !important;
            }

            /* Dialog title */
            [data-testid="stDialog"] [data-testid="stDialogHeader"] {
                color: var(--text-color) !important;
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
