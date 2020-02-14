import requests
import sys
from bs4 import BeautifulSoup

http_proxy = "#"

proxy = {
    "http" : http_proxy,
    "https" : http_proxy
}

URL = "https://www.instagram.com/{}/"

def scrape(username):
    full_url = URL.format(username)
    r = requests.get(full_url, proxies=proxy)
    s = BeautifulSoup(r.text, "lxml")
    main_text = "\n\n"
    tag = s.find("meta", attrs= {"property":"og:title"})
    text = tag.attrs['content']
    main_text += "Name: "+text.split("(")[0] +"\n"
    main_text += "Username: " +text.split("(")[1].split(")")[0]+"\n"
    tag = s.find("meta", attrs = {"name":"description"})
    text = tag.attrs['content']
    main_text += "Followers: "+text.split("-")[0].split(",")[0]+"\n"
    main_text += "Following:"+text.split("-")[0].split(",")[1]+"\n"
    main_text += "Posts:"+text.split("-")[0].split(",")[2]+"\n"
    tag = s.find("meta", attrs= {"property":"og:url"})
    text = tag.attrs['content']
    main_text += "URL: " + text +"\n\n"
    return main_text


data = scrape("username")

with open("Data.txt", "w", encoding="utf-8") as f:
    f.write(data)

