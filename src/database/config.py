import streamlit as st
from supabase import create_client, Client
SUPABASE_URL = st.secrets.get("SUPABASE_URL")
SUPABASE_KEY = st.secrets.get("SUPABASE_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    st.error(
        "Supabase credentials are missing. "
        "Please configure SUPABASE_URL and SUPABASE_KEY "
        "in Streamlit Cloud → Manage app → Settings → Secrets."
    )
    st.stop()
supabase: Client = create_client(
    SUPABASE_URL,
    SUPABASE_KEY
)
