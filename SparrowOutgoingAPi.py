__author__ = 'bijay'
"""
An outgoing sms Api for SparrowSms using Python

"""
import urllib
import urllib2

# Credential for api sms

client_id = ''
username = ''
password = ''
sender = 5455
to = 9848422934
text_message = 'Testing sparrow sms'

#URL building and calling part

url = "http://api.sparrowsms.com/call_in.php?"
values = {'client_id': client_id,
          'username': username,
          'password': password,
          'from': sender,
          'to': to,
          'text': text_message
          }

data = urllib.urlencode(values)
req = urllib2.Request(url, data)
response = urllib2.urlopen(req)
response_value = response.read()
print response_value
