from datetime import datetime
from os import path
from random import randrange
import praw
import urllib.request
from ctypes import windll


#Approved subreddits to get pics from, just add subreddits to the array
#ex. ['spaceporn', 'earthporn']
approved_subs = []
#Subreddit to get wallpapers from
subreddit = approved_subs[randrange(0, len(approved_subs))]
#Collects current date and stores it in the format month.day.year
date_today = datetime.now()
date_today = str(date_today.month) + "." + str(date_today.day) + "." + str(date_today.year)
#Folder where the wallpapers will be saved an located
wallpaper_folder = ""
#Creates a final folder path from the file name, directory, and .jpg extension
wallpaper_location = wallpaper_folder + date_today + ".jpg"

#Does the downloading of the wallpaper for the day
def download_wallpaper(date):
    #Sets up and finds the post from reddit
    r = praw.Reddit(user_agent = "Image Downloader")
    post = r.get_subreddit(subreddit).get_top(limit=1)
    for post in post:
        img_url = post.url

    #Checks to see if the url it got is a direct link to the image
    #If it is not, then the link will be converted to a direct image link
    if img_url[0:10] == "https://im":
        img_url = img_url[0:9] + ".i" + img_url[9:] + ".jpg"

    #Actually downloads the file and sves it to the wallpaper folder
    urllib.request.urlretrieve(img_url, wallpaper_location)


def set_background(file_location):
    windll.user32.SystemParametersInfoW(20, 0, file_location , 0)


#Checks to see if the wallpaper for today has already been downloaded
if path.isfile(wallpaper_location):
    quit()
else:
    download_wallpaper(date_today)
    set_background(wallpaper_location)
