
import streamlit as st
import time
from src.database.db import (
    enroll_student_to_subject,
    get_subject_by_code_section
)
@st.dialog("Enroll in Subject!")
def enroll_dialog():
    st.write(
        "Enter the subject code and section provided by your teacher."
    )
    join_code = st.text_input(
        "Subject Code",
        placeholder="Eg. CS24101",
        key="manual_join_code"
    )
    section = st.text_input(
        "Section",
        placeholder="Eg. A",
        key="manual_join_section"
    )
    if st.button(
        "Enroll Now",
        type="primary",
        width="stretch",
        key="manual_enroll_button"
    ):
        if not join_code.strip() or not section.strip():
            st.warning("Please enter both subject code and section.")
            return
        subject = get_subject_by_code_section(
            join_code,
            section
        )
        if not subject:
            st.error(
                f"Class not found: {join_code.upper()} - "
                f"Section {section.upper()}"
            )
            return
        student_id = st.session_state.student_data['student_id']
        try:
            enroll_student_to_subject(
                student_id,
                subject['subject_id']
            )
            st.success(
                f"Successfully enrolled in {subject['name']} "
                f"- Section {subject['section']}!"
            )
            time.sleep(1)
            st.rerun()
        except Exception:
            st.error(
                "Enrollment failed. You may already be enrolled "
                "in this section."
            )
