import requests
from bs4 import BeautifulSoup

YOUTUBE_TRENDING_URL = "https://www.youtube.com/feed/trending?bp=6gQJRkVleHBsb3Jl"

#does not execute javascript
response = requests.get(YOUTUBE_TRENDING_URL)

print('Status Code', response.status_code)
print('Output', response.text[:1000])

with open('trending.html', 'w') as f:
  f.write(response.text)

  doc = BeautifulSoup(response.text, 'html.parser')
  print('Page title', doc.title.text)

#find all the videos divs
video_divs = doc.find_all('div', class_='style-scope ytd-video-renderer')

print(f'found {len(video_divs)} videos')
  