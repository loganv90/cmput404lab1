import requests
print(requests.__version__)
print(requests.get("https://www.google.com").text)
print(requests.get("https://raw.githubusercontent.com/loganv90/cmput404lab1/main/q2.py").text)
