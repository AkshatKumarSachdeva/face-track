import streamlit as st
from src.database.config import supabase
from src.database.db import create_attendance


def show_attendance_results(df,logs):
        st.write('Please review attendance before confirming.')
        st.dataframe(df,hide_index=True, width='stretch')
        col1,col2=st.columns(2)
        with col1: 
            if st.button('Discard',width='stretch'):
                st.session_state.attendance_images=[]
                st.session_state.voice_attendance_results=None
                st.rerun()

        with col2:
            if st.button('Confirm & Save', width='stretch',type='primary'):
                try:
                    create_attendance(logs)
                    st.toast('Attendance Taken')
                    st.session_state.attendance_images=[]
                    st.session_state.voice_attendance_results=None
                    st.rerun()
                except Exception as e:
                    st.error('Sync failed!')

@st.dialog('Attendance Reports')
def attendance_result_dialog(df,logs):
    st.markdown("""
            <style>
                /* Main dialog title and headings */
                [data-testid="stDialog"] h1,
                [data-testid="stDialog"] h2,
                [data-testid="stDialog"] h3,
                [data-testid="stDialog"] .stMarkdown h1,
                [data-testid="stDialog"] .stMarkdown h2,
                [data-testid="stDialog"] .stMarkdown h3 {
                    color: var(--text-color) !important;
                    opacity: 1 !important;
                    font-weight: 700 !important;
                }
            </style>
        """, unsafe_allow_html=True)
    show_attendance_results(df,logs)