import urllib.request as urlib


def connectivity_check(url):
    print("Checking Url Connection")
    response = urlib.urlopen(url)
    print(f"Connected to {url} Successfully")
    url_response = f"response code {response.getcode()}"
    return url_response

print(connectivity_check("https://www.youtube.com"))