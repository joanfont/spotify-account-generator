#!/usr/bin/env python

#Author: Joan Font 
#Idea: Andreu Cortès
#URL: http://www.joan-font.com/

#You should have mechanize installed (http://wwwsearch.sourceforge.net/mechanize/)

import mechanize
import string
import random
import json

# Function to create random strings
def id_generator(size=6, chars=string.ascii_lowercase + string.digits):
	return ''.join(random.choice(chars) for x in range(size))


print "------------------------------"
print "Spotify Account Generator v0.1"
print "------------------------------"

# Values to fill in the form
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

# Handle the mechanize functions
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(False)
br.addheaders = [('User-agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/536.29.13 (KHTML, like Gecko) Version/6.0.4 Safari/536.29.13')]
response = br.open("https://www.spotify.com/es/signup/")

# Select the second form in the page, in this case the sign up form
br.select_form(nr=1)
# Fill in the values
for key,value in values.iteritems():
	br.form[key] = value

print "Connecting..."
# Submit the form
br.submit()

# Get the response
result = br.response().read()
# In this case, Spotify returns the results in JSON format, decode the response
jsonData = json.loads(result)

# If everything went OK
if(jsonData['message'] == "status_ok"):
  # Display the user and the password
	print "Success!"
	print "User:",user
	print "Password:",passwd
else:
  # Else report the user that something went wrong
	print "Something went wrong..."



