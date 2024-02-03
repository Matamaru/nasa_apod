import os
import requests
import webbrowser
from PIL import Image

# Get the API key from the environment
api_key = os.environ.get('NASA_API_KEY')

url = 'https://api.nasa.gov/planetary/apod'

# Set params for the request
params = {
    'api_key': api_key,
    'count': '1',
    'hd': 'True'
}

# Make the request
response = requests.get(url, params=params)

# Title of the image
img_title = response.json()[0]['title']

# Explanation of the image
img_explanation = response.json()[0]['explanation']

# URL of the image
img_url = response.json()[0]['url']

# Save the image to a file
img = requests.get(img_url).content
with open('image.jpg', 'wb') as f:
    f.write(img)

# Show the image in the default image viewer
img = Image.open('image.jpg')
img.show()

# Print title, source and explanation
print(f'Title: {img_title}')
print(f'Source: {img_url}')
print(f'Explanation: {img_explanation}')






