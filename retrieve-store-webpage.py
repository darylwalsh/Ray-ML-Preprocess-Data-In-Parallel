import os
import re
import time

import pandas as pd
import ray
import requests

path = os.path.join(".", "news_files")

@ray.remote

def store_webpage_content_to_file(url: str, category: str):
    try:
        # Make an HTTP GET request to the URL content
        contentbody = requests.get(url).text
        filename = re.sub(r'http(s){0,1}://(.)*/', "", url)
        filename = os.path.join(path, category, filename)

        with open(filename, "w", encoding='utf-8') as f:
            f.write(contentbody)
        return 1

        # Raise an exception if the request was unsuccessful
        # response.raise_for_status()
        
        # Store the content of the web page in a variable
        # webpage_content = response.text
        
        # Write the content to a file
        # with open(filename, 'w', encoding='utf-8') as file:
        #     file.write(webpage_content)
        # print(f"Content saved to {filename}")
    except requests.RequestException as e:
        print(f"An error occurred: {e}")

def main():
    df = pd.read_json("./real_list.json", lines=False)
    print(df.head())
    if not os.path.exists(path):
        os.makedirs(path)

    res = []
    for category in df['category'].unique():
        category_path = os.path.join(path, category)
        if not os.path.exists(category_path):
            os.makedirs(category_path)

    for _ , row in df[:100].iterrows():
        lnk = row['link']
        res.append(store_webpage_content_to_file.remote(f"http://localhost:8000/{lnk}", row['category']))

    for r in res:
        ray.get(r)

if __name__ == '__main__':
    ray.init(num_cpus=8, dashboard_port=8265)
    main()

        
    
    
    
    # url = "http://localhost:8000/entry_2018-book-preview_us_5a383493e4b0c65287aba20b.html"
    # store_webpage_content_to_file(url)
    