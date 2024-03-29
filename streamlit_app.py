import streamlit as st
import requests
from datetime import datetime, timedelta, timezone

API_Key = 'eyJraWQiOiJ0b2tlblNpZ25pbmciLCJhbGciOiJFUzI1NiJ9.eyJzdWIiOiJzZXJ2aWNldXNlci0zZDdhYzYzYS1mNzFkLTRiOTctYTI5MS1jMjZkZjdjYmEzN2VAbWdtdC0zNjUuc2VudGluZWxvbmUubmV0IiwiaXNzIjoiYXV0aG4tYXAtc291dGhlYXN0LTEtcHJvZCIsImRlcGxveW1lbnRfaWQiOiIzNjUiLCJ0eXBlIjoidXNlciIsImV4cCI6MTcxMzYxMTUwMywianRpIjoiMWRlN2YyNzYtYjZmNi00Zjc3LTlmMDUtMjljMTc2ZTllM2U2In0.be5Lg2dB6cM2TA4AO4C9djeivGRz4mN355ioaWOx7ObyvYWg-Y8hGZhhmqzq6Jb6SFI5yWRp9enVHNye0R_vXA'
Console_URL = 'https://apne1-1101-nfr.sentinelone.net/'

st.write('Welcome to Streamlit')

def load_data():
    url = f'{Console_URL}/web/api/v2.1/agents/count'
    headers = {'Authorization': f'ApiToken {API_Key}'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if 'data' in data and 'total' in data['data']:
            agent_count = data['data']['total']
            return agent_count
        else:
            st.write('Error: Unexpected API response format.')
    elif response.status_code == 401:
        st.write('Unauthorized: Please check your API key and console URL.')
    elif response.status_code == 404:
        st.write('API endpoint not found. Verify the endpoint URL.')
    else:
        st.write(f'Error fetching logs. Status Code: {response.status_code}')
        st.write(response.text)
    return None


st.title('SentinelOne Logs Dashboard')

#logs = load_data()
agent_count = load_data()


# def filter_logs_by_date(logs, days):
#     today = datetime.now(timezone.utc)
#     threshold_date = today - timedelta(days=days)
#     filtered_logs = [log for log in logs if datetime.fromisoformat(log['createdAt__lte']) >= threshold_date]
#     return filtered_logs
# if logs:
#     filtered_logs = filter_logs_by_date(logs, 30)
#     threat_count = len(filtered_logs)
#     st.write(f'Total Threats Created in Last 30 Days: {threat_count}')
#     st.write('Latest Threats:')
#     for log in filtered_logs:
#         st.write(log)
# else:
#     st.write('Failed to fetch logs. Please check your API key and console URL.')

# if logs:
#     st.write('Logs')
#     st.write(logs)
# else:
#     st.write('Failed to fetch logs.')

###########################################################################################


if agent_count is not None:
    st.write(f'Total Agents: {agent_count}')
else:
    st.write('Failed to fetch agent count.')


    