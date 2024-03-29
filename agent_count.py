import requests
import streamlit as st

class AgentsCount:
    def __init__(self, api_key, console_url):
        self.api_key = api_key
        self.console_url = console_url
        self.headers = {
            'Authorization': f'ApiToken {self.api_key}',
            'Content-Type': 'application/json'
        }

    def get_agents_count(self):
        url = f'{self.console_url}/web/api/v2.1/agents/count'
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            data = response.json()
            if 'data' in data and 'total' in data['data']:
                threat_count = data['data']['total']
                return threat_count
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
