import streamlit as st
from src.database.db import create_subject
@st.dialog("Create New Subject")
def create_subject_dialog(teacher_id):
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
