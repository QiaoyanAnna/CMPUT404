import requests

print(requests.__version__)

var = requests.get("https://www.google.com/")

print(var.content)