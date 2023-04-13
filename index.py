#Python script to extract all urls in a webpage
from bs4 import BeautifulSoup
import requests

def data_clean(urls:list):
    for url in urls:
        if url != "None" or url != url.startswith('#'):
            pass
        else:
            urls.remove(url)

    return urls
def get_urls(url : str):
    urls = []
    response = requests.get(url)
    if response.status_code == 200:

        soup = BeautifulSoup(response.text, 'html.parser')
        for link in soup.find_all('a'):
            href = link.get('href')
            urls.append(href)
        return urls
    else:
        return "An error occurred"
if __name__ == '__main__':
    #input website url such a www.carlnkyle.co.ke
    url = input("Enter website url to extract child urls i.e www.****\t")
    save = False
    if input("Do you want to save the urls to a file? (y/n)\t") == 'y':
        save = True
    urls = get_urls("https://"+url)
    # data clean
    urls = data_clean(urls)
    if save:
        with open('urls.txt', 'w') as f:
            for url in urls:
                f.write(str(url))
                f.write('\n')
        for i in urls:
            print(i)
    else:
        for i in urls:
            print(i)        
