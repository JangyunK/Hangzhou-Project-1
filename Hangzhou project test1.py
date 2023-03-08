import requests
from bs4 import BeautifulSoup

# Define the URL of Hangzhou City's Wikipedia page
url = 'https://en.wikipedia.org/wiki/Hangzhou'

# Make a request to the URL and get the HTML content
response = requests.get(url)
content = response.content

# Use BeautifulSoup to parse the HTML content and extract the introduction section
soup = BeautifulSoup(content, 'html.parser')
intro_section = soup.find('div', {'class': 'mw-parser-output'}).p

# Print out the introduction text
print(intro_section.text.strip())
