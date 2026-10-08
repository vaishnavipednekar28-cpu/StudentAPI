import requests
url="http://127.0.0.1:5000/students/1"

requests.put(url,
             json={
                 'Name':'Shyam',
                 'Course':'DA'
             })