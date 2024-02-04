import os
import requests
from PIL import Image
import datetime

#create folder if not exist
if not os.path.exists('data'):
    os.makedirs('data')

# create folder image in data if not exist
if not os.path.exists('data/image'):
    os.makedirs('data/image')

# create folder text in data if not exist
if not os.path.exists('data/text'):
    os.makedirs('data/text')

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
print(response.json())

# Title of the image
img_title = response.json()[0]['title']

# Explanation of the image
img_explanation = response.json()[0]['explanation']

# URL of the image
img_url = response.json()[0]['url']

# date of download format year-month-day (20240203)
date = datetime.datetime.now().strftime('%Y%m%d')

# Save the image to a file
img = requests.get(img_url).content
img_filename = date + '_' + img_title.replace(' ', '_') + '.jpg'
img_path = os.path.join('data', 'image', img_filename)
with open(img_path, 'wb') as f:
    f.write(img)

# Save the text to the image
text_filename = date + '_' + img_title.replace(' ', '_') + '.txt'
text_path = os.path.join('data', 'text', text_filename)
with open(text_path, 'w') as f:
    f.write(f'Title: {img_title}\n')
    f.write(f'Source: {img_url}\n')
    f.write(f'Explanation: {img_explanation}')

# Show the image in the default image viewer
img = Image.open(img_path)
img.show()

# Print title, source and explanation
print(f'Title: {img_title}')
print(f'Source: {img_url}')
print(f'Explanation: {img_explanation}')






