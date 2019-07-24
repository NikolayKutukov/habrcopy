import requests
response=requests.get("http://habr.com")
with open("habr.html","w",encoding='utf-8') as file:
    file.write(response.text)
    
