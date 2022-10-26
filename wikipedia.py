import requests
def main():
    session = requests.Session()

    url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "format": "json",
        "titles": "Albert Einstein",
        "prop": "links",
        "pllimit": "max"
    }

    res = session.get(url=url, params=params)
    data = res.json()
    pages = data["query"]["pages"]


    page_titles = []


    for key, val in pages.items():

        
        for link in val["links"]:
            print(link["title"])
            page_titles.append(link["title"])
    print(page_titles)
    


if __name__ == "__main__":
    main()
