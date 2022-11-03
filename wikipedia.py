import requests
def main():
    session = requests.Session()

    test = [1,2,3,4,5]
    for i in test:
        if i == 2:
            test.remove(i)
        print(i)
    print(test)
    return 0
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
