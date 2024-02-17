import diffbot

diffbot_client = diffbot.Client(token='your_diffbot_api_token')

def extract_with_diff(url, previous_data=None):
    article = diffbot_client.request(url, 'article')

    # Example - Extract Key Fields
    data = {
        'title': article['objects'][0]['title'],
        'text': article['objects'][0]['text'],
        'date': article['objects'][0]['date']
    }

    # Simple Difference Check (assumes previously stored data has same structure)
    if previous_data:
        for key in data:
            if data[key] != previous_data[key]:
                print(f"Change detected in '{key}' field")

    return data

# Example Usage
url = "https://www.example.com/news-article"

# First Run (no previous data)
extracted_data = extract_with_diff(url)
# ...Store 'extracted_data' somewhere...

# Subsequent Run
new_extracted_data = extract_with_diff(url, previous_data=extracted_data)
