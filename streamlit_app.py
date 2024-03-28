import streamlit as st
import requests


API_Key = 'eyJraWQiOiJ0b2tlblNpZ25pbmciLCJhbGciOiJFUzI1NiJ9.eyJzdWIiOiJzZXJ2aWNldXNlci0zZDdhYzYzYS1mNzFkLTRiOTctYTI5MS1jMjZkZjdjYmEzN2VAbWdtdC0zNjUuc2VudGluZWxvbmUubmV0IiwiaXNzIjoiYXV0aG4tYXAtc291dGhlYXN0LTEtcHJvZCIsImRlcGxveW1lbnRfaWQiOiIzNjUiLCJ0eXBlIjoidXNlciIsImV4cCI6MTcxMzYxMTUwMywianRpIjoiMWRlN2YyNzYtYjZmNi00Zjc3LTlmMDUtMjljMTc2ZTllM2U2In0.be5Lg2dB6cM2TA4AO4C9djeivGRz4mN355ioaWOx7ObyvYWg-Y8hGZhhmqzq6Jb6SFI5yWRp9enVHNye0R_vXA'
Console_URL = 'https://apne1-1101-nfr.sentinelone.net/'

st.write('Welcome to Streamlit')

def load_data():
    url = f'{Console_URL}/web/api/v2.1/log'
    headers = {'Authorization': f'ApiToken {API_Key}'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return None


st.title('SentinelOne Logs Dashboard')

logs = load_data()

if logs:
    st.write('logs:')
    st.write(logs)
else:
    st.write('Failed')
