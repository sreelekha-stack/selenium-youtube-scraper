import requests
YOUTUBE_TRENDING_URL = "https://www.youtube.com/feed/trending?bp=6gQJRkVleHBsb3Jl"

response = requests.get(YOUTUBE_TRENDING_URL)

print('Status Code', response.status_code)
print('Output', response.text[:1000])

with open('trending.html', 'w') as f:
  f.write(response.text)
  