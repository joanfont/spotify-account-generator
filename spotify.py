#!/usr/bin/env python

#Author: Joan Font
#URL: http://www.joan-font.com/

#You should have mechanize installed (http://wwwsearch.sourceforge.net/mechanize/)

import mechanize
import string
import random
import json

def id_generator(size=6, chars=string.ascii_lowercase + string.digits):
	return ''.join(random.choice(chars) for x in range(size))


print "------------------------------"
print "Spotify Account Generator v0.1"
print "------------------------------"

user = id_generator()
passwd = id_generator()
email = id_generator()+"@"+id_generator()+".com"
day = "24"
month = ["01"]
year = "1984"
gender = ["male"]
values = {'username' : user,
      'password' : passwd,
      'email' : email,
      'confirm_email' : email,
      'dob_day' : day,
      'dob_month' : month,
      'dob_year' : year,
      'gender' : gender
       }


br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(False)
br.addheaders = [('User-agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/536.29.13 (KHTML, like Gecko) Version/6.0.4 Safari/536.29.13')]
response = br.open("https://www.spotify.com/es/signup/")

br.select_form(nr=1)
for key,value in values.iteritems():
	br.form[key] = value

print "Connecting..."
br.submit()

result = br.response().read()
jsonData = json.loads(result)

if(jsonData['message'] == "status_ok"):
	print "Success!"
	print "User:",user
	print "Password:",passwd
else:
	print "Something went wrong..."



