import streamlit as st
from agent_count import AgentsCount

def main():
    st.title('SentinelOne Dashboard')
    
    # Input fields
    api_key = st.text_input('eyJraWQiOiJ0b2tlblNpZ25pbmciLCJhbGciOiJFUzI1NiJ9.eyJzdWIiOiJzZXJ2aWNldXNlci0zZDdhYzYzYS1mNzFkLTRiOTctYTI5MS1jMjZkZjdjYmEzN2VAbWdtdC0zNjUuc2VudGluZWxvbmUubmV0IiwiaXNzIjoiYXV0aG4tYXAtc291dGhlYXN0LTEtcHJvZCIsImRlcGxveW1lbnRfaWQiOiIzNjUiLCJ0eXBlIjoidXNlciIsImV4cCI6MTcxMzYxMTUwMywianRpIjoiMWRlN2YyNzYtYjZmNi00Zjc3LTlmMDUtMjljMTc2ZTllM2U2In0.be5Lg2dB6cM2TA4AO4C9djeivGRz4mN355ioaWOx7ObyvYWg-Y8hGZhhmqzq6Jb6SFI5yWRp9enVHNye0R_vXA')
    console_url = st.text_input('https://apne1-1101-nfr.sentinelone.net/')
    
    if st.button('Fetch Data'):
        if api_key and console_url:
            agents_count_api = AgentsCount(api_key, console_url)
            
            # Fetch and display agents count
            agents_count_data = agents_count_api.get_agents_count()
            st.subheader('Agents Count')
            st.write(agents_count_data)
            
        else:
            st.warning('API Key and Console URL')

if __name__ == '__main__':
    main()
