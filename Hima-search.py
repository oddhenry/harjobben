import requests
from datetime import datetime

search_string = "Hilde martine Lindgren"
print(f"Searching for {search_string}")
search_string = search_string.replace(" ", "+")

r = requests.get(f'https://psapi.nrk.no/radio/search/search?q="{search_string}"')
result = r.json()
print(f"got {result['count']} results")

for episode in result['results']['episodes']['results']:
    date = datetime.fromisoformat(episode['date'])
    #print(episode['images'])

    print(f"got episode '{episode['title']}' from {date.strftime('%A %d. %B %Y kl. %H:%M')}.")
    
    #It has the following highlights:
    #for highlight in episode['highlights']:
    #    print(f"  {highlight['text']}")


