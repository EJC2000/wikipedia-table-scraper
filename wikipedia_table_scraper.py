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

def one_wikitable(soup, title):
    table = soup.find('table', {'class': 'wikitable'})
    rows = table.find_all("tr")
    
    filename = f"{title}_wikipedia_table.csv"
    with open(filename, "w", newline='', encoding="uft-8") as file:
        writer = csv.writer(file)
        
        for row in rows:
            columns = row.find_all(["th", "td"])
            rows_data = []
            
            for column in columns:
                text = columns.text.strip()
                rows_data.append(text)
                
                if rows_data:
                    writer.writerow(rows_data)
    print(f"CSV File for {title} has been created.")
