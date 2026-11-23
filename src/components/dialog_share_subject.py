# import streamlit as st
# import segno, io


# @st.dialog("Share Class Link")
# def share_subject_dialog(subject_name,subject_code):

#     st.markdown("""
#         <style>
#             /* Main dialog title and headings */
#             [data-testid="stDialog"] h1,
#             [data-testid="stDialog"] h2,
#             [data-testid="stDialog"] h3,
#             [data-testid="stDialog"] .stMarkdown h1,
#             [data-testid="stDialog"] .stMarkdown h2,
#             [data-testid="stDialog"] .stMarkdown h3 {
#                 color: var(--text-color) !important;
#                 opacity: 1 !important;
#                 font-weight: 700 !important;
#             }

#             /* Make the QR caption readable in both themes */
#             [data-testid="stDialog"] [data-testid="stImage"] figcaption {
#                 color: var(--text-color) !important;
#                 opacity: 0.85 !important;
#             }

#             /* Improve contrast for code blocks */
#             [data-testid="stDialog"] [data-testid="stCode"] {
#                 opacity: 1 !important;
#             }
#         </style>
#     """, unsafe_allow_html=True)

#     app_domain="facetrack-main.streamlit.app"
#     join_url=f"{app_domain}/?join-code={subject_code}"
#     st.header("Scan to Join")
#     qr=segno.make(join_url)
#     out=io.BytesIO()
#     qr.save(out,kind='png',scale=10,border=1)
#     col1,col2=st.columns(2)
#     with col1:
#         st.markdown('### Copy Link')
#         st.code(join_url,language="text")
#         st.code(subject_code,language="text")
#         st.info('Copy this link to share on Whatsapp or Email.')
#     with col2:
#         st.markdown('### Scan to Join')
#         st.image(out.getvalue(), caption='QR-CODE for Class Joining')

import streamlit as st
import segno
import io
from urllib.parse import urlencode
@st.dialog("Share Class Link")
def share_subject_dialog(subject_name, subject_code, section):
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

            /* Make the QR caption readable in both themes */
            [data-testid="stDialog"] [data-testid="stImage"] figcaption {
                color: var(--text-color) !important;
                opacity: 0.85 !important;
            }

            /* Improve contrast for code blocks */
            [data-testid="stDialog"] [data-testid="stCode"] {
                opacity: 1 !important;
            }
        </style>
    """, unsafe_allow_html=True)
    app_domain = "face_trackk-main.streamlit.app"

    subject_code = subject_code.strip().upper()
    section = section.strip().upper()

    params = urlencode({
        "join-code": subject_code,
        "section": section
    })
    join_url = f"https://{app_domain}/?{params}"
    st.header("Share Class: " + subject_name)
    st.info(
        f"Subject Code: {subject_code} | Section: {section}"
    )

    qr = segno.make(join_url)
    out = io.BytesIO()
    qr.save(
        out,
        kind='png',
        scale=10,
        border=1
    )
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### Copy Link")
        st.code(join_url, language="text")
        st.code(subject_code, language="text")
        st.code(section, language="text")
        st.info("Share this link through WhatsApp or Email.")

    with col2:

        st.markdown("### Scan to Join")
        st.image(
            out.getvalue(),
            caption=f"QR Code - Section {section}"
        )
