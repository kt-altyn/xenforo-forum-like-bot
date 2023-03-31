import requests
from bs4 import BeautifulSoup
import time

# Define the login credentials
login_url = 'https://forum.examplexenforoforum/login'
username = 'example_username'
password = 'example_password'

# Initialize a session and get the login page
session = requests.Session()
login_page = session.get(login_url)

# Parse the login page HTML with BeautifulSoup
soup = BeautifulSoup(login_page.content, 'html.parser')

# Extract the necessary form fields
login_data = {
    'login': username,
    'password': password,
    '_xfToken': soup.find('input', {'name': '_xfToken'})['value'],
    '_xfRedirect': soup.find('input', {'name': '_xfRedirect'})['value'],
    'remember': '1'
}

# Submit the login request
response = session.post(login_url, data=login_data)

# Check if the login was successful
if response.status_code == 200:
    print('Logged in successfully!')
else:
    print('Login failed!')
    print(f'Login failed with status code {response.status_code}')

# Set the session cookie
session_cookie = response.cookies.get('xf_session')

# Define the post URLs
post_urls = [
    'https://forum.examplexenforoforum.com/posts/78815',
    'https://forum.examplexenforoforum.com/posts/78553',
    'https://forum.examplexenforoforum.com/posts/78480'
]

# Define the reaction ID for the "like" reaction (1 = like)
reaction_id = 7

# Loop through the post URLs and react to each post
for post_url in post_urls:
    reaction_url = f'{post_url}/react?reaction_id={reaction_id}'

    # Send a reaction request for the post
    response = session.post(reaction_url)

    # Wait for 1 second to allow time for the confirmation page to load
    time.sleep(11)

    # Confirm the reaction by clicking the "Confirm" button
    confirm_url = f'{post_url}/react?reaction_id={reaction_id}&_xfRequestUri={post_url}'
    response = session.get(confirm_url)

    # Check if the reaction was successful
    if response.status_code == 200:
        print(f'Reacted to post: {post_url}')
    else:
        print(f'Failed to react to post: {post_url}')
        print(f'Reaction failed with status code {response.status_code}')
