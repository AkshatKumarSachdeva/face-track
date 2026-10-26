import streamlit as st

def header_home():
    logo_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR_oYu0ydlehQLoH8G1cSo_zkHOETtyNRjhtdIaSfx1eg&s=10'
    st.markdown(f"""
        <div style="display:flex; flex-direction:column; align-items:center; justify-content:center; margin-bottom:20px; margin-top:0px;">    
            <img src='{logo_url}' style='height:100px'; />
            <h1 style='text-align:center; color:#E0E3FF'>Face<br>TracK</h1>
        </div>
    """,unsafe_allow_html=True)

def header_dashboard():
    logo_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR_oYu0ydlehQLoH8G1cSo_zkHOETtyNRjhtdIaSfx1eg&s=10'
    st.markdown(f"""
        <div style="display:flex; align-items:center; justify-content:center; gap:10px; margin-bottom:20px; margin-top:0px">    
            <img src='{logo_url}' style='height:85px'; />
            <h2 class="dashboard-title" style='text-align:left; color:#5865F2'>FACE<br>TRACK</h2>
        </div>
    """,unsafe_allow_html=True)