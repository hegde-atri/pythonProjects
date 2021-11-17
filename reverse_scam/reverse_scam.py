import requests
import os
import random
import string
import json

url = ''
random.seed = (os.urandom(1024))
chars = string.ascii_letters + string.digits + '!@#$%^&*()'
names = 'Daniel, David' #This will be linked to a file rather than a small array

for name in names:
  password_length = random.randint(8, 14)
  name_extra = ''.join(random.choice(string.digits))

  username = name.lower() + name_extra + 'gmail.com' # I could add a random domain name, but its unnecessary for now.
  password = ''.join(random.choice(chars) for i in range(password_length))
  
  requests.post(url, allow_redirects=False, data={
# data format to post here
  })

  print('send username %s and password $s' % (username, password))