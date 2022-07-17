import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

YOUTUBE_TRENDING_URL = "https://www.youtube.com/feed/trending?bp=6gQJRkVleHBsb3Jl"

def get_driver():
  chrome_options = Options()
  chrome_options.add_argument('--no- sandbox')
  chrome_options.add_argument('-- headless')
  chrome_options.add_argument('-- disable-dev-shm-usage')
  driver = webdriver.chrome(options=chrome_options) #if u download the driver for your computer we need to put full path here
  return driver

def get_videos(driver):
  VIDEO_DIV_TAG = 'style-scope ytd-video-renderer'
  driver.get(YOUTUBE_TRENDING_URL)
  videos = driver.find_elements(By.TAG_NAME, VIDEO_DIV_TAG)
  return videos

def parse_video(video):
  title_tag = video.find_element(By.ID, 'video-title')
  title = title_tag.text
  url = title_tag.get_attribute('href')

  thumbnail_tag = video.find_element(By.TAG_NAME, 'thumbnail')
  thumbnail_url = thumbnail_tag.get_attribute('href')

  channel_div = video.find_element(By.CLASS_NAME, 'style-scope ytd-channel-name complex-string')
  channel_name = channel_div.text

  description = video.find_element(By.ID, 'description-text').text
  return {
    'title': title,
    'url' : url,
    'thumbnail_url' : thumbnail_url,
    'channel' : channel_name,
    'description' : description
  }
 
if __name__ =="__main__":
  print('Creating driver')
  driver = get_driver()

  print('fetching trendings videos')
  videos = get_videos(driver)
  
  print(f'Found {len(videos)} videos')

  print('Parsing top 10 videos')
  videos_data = [parse_video(video) for video in videos[:10]]
  print('Save the data to a CSV')
  videos_df = pd.DataFrame(videos_data)
  print(videos_df)
  videos_df.to_csv('trending.csv', index=None)
  
  



