import csv
import shutil
import os
import requests
from bs4 import BeautifulSoup

def get_url_info(url):
    headers = {"User-Agent": "Mozilla/5.0"} # Mimic a real browser to avoid request blocking
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        print(f"Failed to retrieve page. Status code: {response.status_code}")
        return None
    
    soup = BeautifulSoup(response.text, "html.parser")
    return soup
