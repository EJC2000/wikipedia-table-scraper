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
    
    filename = f"{title}_table.csv"
    with open(filename, "w", newline='', encoding="utf-8") as file:
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


def multi_wikitable(soup, title):
    tables = soup.find_all('table', class_='wikitable')
    
    for i, table in enumerate(tables):
        rows = table.find_all("tr")
        
        filename = f"{title}_table_{i+1}.csv"
        with open(filename, "w", newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            
            for row in rows:
                columns = row.find_all(["th", "td"])
                rows_data = []
                
                for column in columns:
                    text = column.text.strip()
                    rows_data.append(text)
                    
                    if rows_data:
                        writer.writerow(rows_data)
        print(f"CSV File for {filename} has been created.")
        

def sort_csv_to_folder(base_path, keyword):
    keyword = keyword.lower()
    folder_name = fr"{keyword.capitalize()} Folder"
    folder_path = os.path.join(base_path, folder_name)
    
    os.makedirs(folder_path)
    print(f"Folder: {folder_name} created at {folder_path}")
    
    for file_name in os.listdir(base_path):
        if file_name.endswith(".csv") and keyword in file_name.lower():              
            source_path = os.path.join(base_path, file_name)
            destination_path = os.path.join(folder_path, file_name)
            shutil.move(source_path, destination_path)
            print(f"Moved {file_name} to {destination_path}")