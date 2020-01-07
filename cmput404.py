import requests

print(requests.__version__)

var = requests.get("https://raw.githubusercontent.com/QiaoyanAnna/CMPUT404/master/cmput404.py")

print(var.content)