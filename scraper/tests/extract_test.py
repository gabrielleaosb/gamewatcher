import requests
import json
from datetime import datetime


response = requests.get("https://store.steampowered.com/api/featuredcategories", {'cc': 'br', 'l': 'portuguese'})
print(response.json())