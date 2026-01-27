
import requests
import json

def test():
    base_url = "http://localhost:8000"
    
    # 1. Get All News
    print("Fetching All News...")
    try:
        r = requests.get(f"{base_url}/news?limit=5")
        data = r.json()
        print(f"All News Count (first page): {len(data.get('items', []))}")
        print("First item sample:", filter_keys(data.get('items', [])[0]) if data.get('items') else "None")
    except Exception as e:
        print(f"Error fetching all news: {e}")

    # 2. Get Trending News
    print("\nFetching Trending News (filter_type=trending)...")
    try:
        r = requests.get(f"{base_url}/news?filter_type=trending&limit=5")
        data = r.json()
        print(f"Trending News Count: {len(data.get('items', []))}")
        if data.get('items'):
             print("Trending item sample:", filter_keys(data.get('items')[0]))
        else:
             print("No trending items found.")
    except Exception as e:
        print(f"Error fetching trending news: {e}")

def filter_keys(d):
    return {k: v for k, v in d.items() if k in ['headline', 'views']}

if __name__ == "__main__":
    test()
