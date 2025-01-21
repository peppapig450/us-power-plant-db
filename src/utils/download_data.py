import os
import json
import requests

def download_data_from_urls(urls_json_path="data/data_urls.json", download_dir="data/raw"):
    """
    Downloads data files from URLs specified in the data_urls.json file.
    
    Args:
        urls_json_path (str): Path to the JSON file containing the URLs.
        download_dir (str): Directory where the data files should be saved.
    """
    # Read the JSON file containing the data URLs
    try:
        with open(urls_json_path, "r") as f:
            data_urls = json.load(f)
    except FileNotFoundError:
        print(f"Error: {urls_json_path} not found.")
        return
    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON from {urls_json_path}.")
        return

    # Ensure the download directory exists
    os.makedirs(download_dir, exist_ok=True)

    # Iterate over the URLs and download the data
    for dataset, info in data_urls.items():
        url = info.get("url")
        filename = info.get("filename")
        
        if url and filename:
            try:
                print(f"Downloading {dataset} from {url}...")
                response = requests.get(url)
                response.raise_for_status()  # Check if the request was successful
                
                file_path = os.path.join(download_dir, filename)
                with open(file_path, "wb") as f:
                    f.write(response.content)
                print(f"Downloaded {dataset} to {file_path}")
            except requests.exceptions.RequestException as e:
                print(f"Error downloading {dataset}: {e}")
        else:
            print(f"Skipping {dataset}: missing URL or filename.")

if __name__ == "__main__":
    download_data_from_urls()