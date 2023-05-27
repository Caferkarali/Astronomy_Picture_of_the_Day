# -*- coding: utf-8 -*-
"""
Created on Sat May 27 21:53:35 2023

@author: Cafer karali
"""

import requests
import webbrowser

url = "https://api.nasa.gov/planetary/apod"
api_key = "YOUR API_KEY"
desired_date = "2022-08-29"  # Değiştirmek istediğiniz tarih

params = {
    "api_key": api_key,
    "date": desired_date
}

response = requests.get(url, params=params)
data = response.json()

if response.status_code == 200:
    date = data["date"]
    explanation = data["explanation"]
    hdurl = data["hdurl"]
    media_type = data["media_type"]
    title = data["title"]
    url = data["url"]

    print("Date:", date)
    print("Title:", title)
    print("Explanation:", explanation)
    print("Media Type:", media_type)
    print("URL:", url)
    print("HD URL:", hdurl)

    # Resme doğrudan web tarayıcısında gitmek için aşağıdaki kodu kullanabilirsiniz
    webbrowser.open(hdurl)
else:
    print("An error occurred:", response.status_code)
