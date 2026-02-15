import requests
import csv
import time

# API setup
base_url = "https://api.wordpress.org/plugins/info/1.2/"
per_page = 100
page = 1
plugins = []
search_term = "optimization"

print(f"Fetching plugins matching '{search_term}'...")

while True:
    params = {
        'action': 'query_plugins',
        'request[page]': page,
        'request[per_page]': per_page,
        'request[search]': search_term
    }
    
    response = requests.get(base_url, params=params)
    data = response.json()
    
    # Stop if no more plugins
    if not data['plugins']:
        break
    
    plugins.extend(data['plugins'])
    print(f"Fetched page {page} with {len(data['plugins'])} plugins...")
    page += 1
    
    time.sleep(0.5)  # Gentle delay to be polite to their servers

print(f"Total plugins fetched: {len(plugins)}")

# Save to CSV
csv_filename = f"wordpress_plugins_ratings_{search_term}.csv"

with open(csv_filename, mode='w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Plugin Name', 'Rating'])

    for plugin in plugins:
        writer.writerow([plugin['name'], plugin['rating']])

print(f"Data saved to {csv_filename}")
