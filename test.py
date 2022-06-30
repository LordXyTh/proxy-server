import requests

proxies = {
  'http': 'http://192.168.0.158:80',
  'https': 'http://192.168.0.158:80',
}

response = requests.get('http://httpbin.org/get', proxies=proxies)
print(response.text)

response = requests.get('http://httpbin.org/get?arg1=hello&arg2=world', proxies=proxies)
print(response.text)