import requests;

# url = 'http://registration.msu.ac.th/webservice/registration/get/getStdinfo.php?stdcode=66011212125';
url = 'http://10.9.10.4/linkurl/reg/isuser.php'

def get():
    data = requests.get(url);
    print(data.text)

get()

#  //var params = {checktype: 'uid', user: 'adam', password: 'pass1234', profile: 'dart', defaultdb: 'kts'};