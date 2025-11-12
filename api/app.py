import os, streamlit as st
from supabase import create_client, Client

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_ANON_KEY")
supa: Client = create_client(url, key)

st.title("微舆 - 舆情速览")
rows = supa.table("topics").select("*").execute().data
st.dataframe(rows)
