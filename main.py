import time
import os
from wikipedia_table_scraper import get_url_info, one_wikitable, multi_wikitable, sort_csv_to_folder

def main():
    soup = None
    
    while True:
        print("----------------------------------")
        print("Wikipedia Table Scraper")
        print("1. Fetch and parse Wikipedia page")
        print("2. Retrieve First Wikipedia Table")
        print("3. Retrieve All Wikipedia Tables")
        print("4. Create Folders for Files")
        print("5. Exit")
        print("----------------------------------")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            url = input("Enter Wikipedia URL: ")
            soup = get_url_info(url)
            
        elif choice == "2":
            if soup:
                title = input("Enter title for CSV file: ")
                one_wikitable(soup, title)
            else:
                print("Please enter a URL first. (Option 1)")
        elif choice == "3":
            if soup:
                title = input("Enter title for CSV file: ")
                multi_wikitable(soup, title)
            else:
                print("Please enter a URL first. (Option 1)")
        elif choice == "4":
            base_path = input("Enter folder path or press 'C' for current directory: ")
            if base_path.lower() == 'c':
                base_path = os.getcwd()
                
            keyword = input("Enter folder name: ")
            sort_csv_to_folder(base_path, keyword)
        elif choice == "5":
            print("Exiting program..")
            time.sleep(1)
            break
        else:
            print("Please select an option.")