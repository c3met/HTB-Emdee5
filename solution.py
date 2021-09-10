import requests 
import hashlib 
from bs4 import BeautifulSoup

# GET the string that needs to be encrypted.

url = input("Enter the challenge Url: " )
r = requests.session()
getSite = r.get(url)

print('[+]Getting site content')
# Strip html content

soup = BeautifulSoup(getSite.content, "lxml")
strip = soup.h3.string

print("[+]String: " + strip)
# Encrypt the string

hashed = hashlib.md5(strip.encode()).hexdigest()
print("[+]Hash encrypted: " + hashed)

# Send the hash to the Site 

data = {'hash': hashed}
post = r.post(url, data = data)

print("[+]Getting flag!")

flag = post.text 

print(flag)
