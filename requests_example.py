import requests
url = 'http://www.ibm.com'
r = requests.get(url)
# r.status_code :200
print(r.status_code)
print(r.request.headers)
print(r.request.body)
header = r.headers

print(f"####################################################################\n\n{header}")


print(header['date'])
print(header['Content-Type'])
print(r.encoding)