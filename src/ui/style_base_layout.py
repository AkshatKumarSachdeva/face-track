import streamlit as st

def style_background_home():
    st.markdown("""
    <style>
                .stApp{
                    background:#5865F2 !important;
                }

                .stApp div[data-testid="stColumn"]{
                    background-color:#E0E3FF !important;
                    padding:2.5rem !important;
                    border-radius:5rem !important;
                }
                

    </style>

        """,unsafe_allow_html=True)

def style_background_dashboard():
    st.markdown("""
    <style>
                .stApp{
                    background:#E0E3FF !important;
                }
                
                .stTextInput label,
                .stTextInput label p {
                    color: #000000 !important;
                    opacity: 1 !important;
                }

                /* Camera input label */
                .stCameraInput label,
                .stCameraInput label p {
                    color: #000000 !important;
                    opacity: 1 !important;
                }

                /* Voice Enrollment heading */
                h3, h3 p {
                    color: black !important;
                    opacity: 1 !important;
                }

                /* Audio recording instruction */
                .stAudioInput label,
                .stAudioInput label p {
                    color: black !important;
                    opacity: 1 !important;
                }

                /* Creating profile spinner text */
                .stSpinner,
                .stSpinner p {
                    color: black !important;
                    opacity: 1 !important;
                }

                hr {
                    border: none !important;
                    height: 2px !important;
                    background-color: #000000 !important;
                    opacity: 1 !important;
                }

    </style>

    """,unsafe_allow_html=True)

def style_base_layout():

    st.markdown("""
    <style>
            @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&display=swap');
            @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&family=Outfit:wght@100..900&display=swap');
            /*Hide top bar of streamlit*/
                
                #MainMenu,footer,header{
                    visibility:hidden;
                }
                .block_container{
                    padding-top:1.5rem !important;
                }

                h1{
                    font-family:'Climate Crisis',sans-serif !important;
                    font-size:3.5rem !important;
                    line-height:1.1 !important;
                    margin-bottom:0rem !important;
                    
                }

                h2{
                    font-family:'Climate Crisis',sans-serif !important;
                    font-size:2rem !important;
                    color: black !important;
                    line-height:1.1 !important;
                    margin-bottom:0rem !important;
                    
                }
                .dashboard-title{
                    color:#5865F2 !important;
                }
                h3,h4,p{
                    font-family:'Outfit',san-serif;
                }
                button
                {
                    border-radius: 1.5rem !important;
                    background-color: #5865F2 !important;
                    color: white !important;
                    padding: 10px 20px !important;
                    border: none !important;
                    transition: transform 0.25s ease-in-out !important;
                }
                button[kind="secondary"]
                {
                    border-radius: 1.5rem !important;
                    background-color: #EB459E !important;
                    color: white !important;
                    padding: 10px 20px !important;
                    border: none !important;
                    transition: transform 0.25s ease-in-out !important;
                }
                button[kind="tertiary"]
                {
                    border-radius: 1.5rem !important;
                    background-color: #EB459E !important;
                    color: white !important;
                    padding: 10px 20px !important;
                    border: none !important;
                    transition: transform 0.25s ease-in-out !important;
                }
                button:hover{
                    transform: scale(1.05)
                }
    </style>

    """,unsafe_allow_html=True)