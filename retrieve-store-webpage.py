import requests


def store_webpage_content_to_file(url, filename='.retrieved/books/entry_2018-book-preview_us_5a383493e4b0c65287aba20b.html', category_name='books'):
    try:
        # Make an HTTP GET request to the URL
        response = requests.get(url)
        
        # Raise an exception if the request was unsuccessful
        response.raise_for_status()
        
        # Store the content of the web page in a variable
        webpage_content = response.text
        
        # Write the content to a file
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(webpage_content)
        print(f"Content saved to {filename}")
    except requests.RequestException as e:
        print(f"An error occurred: {e}")

        
    
    
    
    url = "http://localhost:8000/entry_2018-book-preview_us_5a383493e4b0c65287aba20b.html"
    store_webpage_content_to_file(url)
    