import snowflake.connector
import streamlit as st

@st.cache_resource
def get_snowflake_connection():
    conn = snowflake.connector.connect(
        user="kishoremudigonda",
        password="Kumar939108109",
        account="fukgbu-to83656",  # e.g., abcd-xy12345
        warehouse="SCM_WH",
        database="SCM_DB",
        schema="SCM_SCHEMA",
        role="ACCOUNTADMIN"  # or another role with access
    )
    return conn
