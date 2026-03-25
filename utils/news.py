import requests

API_KEY = "3133069d3283440caaaca3768228426b"

def fetch_news():
    url = f"https://newsapi.org/v2/everything?q=cars OR bikes&language=en&apiKey={API_KEY}"
    
    response = requests.get(url)
    data = response.json()
    
    articles = []
    
    if data["status"] == "ok":
        for item in data["articles"][:5]:
            articles.append({
                "title": item["title"],
                "desc": item["description"],
                "url": item["url"]
            })
    
    return articles