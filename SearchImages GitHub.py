import requests
import json
import urllib


url = "https://api.imgur.com/oauth2/token"

payload = "PAYLOAD"

headers = {
    'content-type': "multipart/form-data; boundary=----APIKEY",
    'Cache-Control': "no-cache",
    'Postman-Token': "Postman Token"
}

response = requests.request("POST", url, data=payload, headers=headers)
IDS = []
LINKS=[]
TITLES=[]
DATE =[]
WIDTH = []
HIGHT=[]

for i in range(100):

    url = "https://api.imgur.com/3/gallery/search/{{sort}}/{{window}}/{}".format(i)

    querystring = {"q": "cats"}
    headers = {
        'Authorization': "Client-ID ClintIDHere",
        'Cache-Control': "no-cache",
        'Postman-Token': "Postman Token"
    }
    response = requests.request(
        "GET", url, headers=headers, params=querystring).json()
    for i in range(len(response['data'])):
        try:
            ID = (response['data'][i]['id'])
            LINK = (response['data'][i]['link'])
            TITLE = (response['data'][i]['title'])
            DA = (response['data'][i]['datetime'])
            WI = (response['data'][i]['cover_width'])
            HI = (response['data'][i]['cover_height'])
            IDS.append(ID)
            print('''
                     ID IS    ->  {} 
                     TITLE IS ->  {}
                     LINK IS  ->  {}
                     Date IS  ->  {}
                     WIDTH IS ->  {}
                     HIGHT IS ->  {}'''.format(ID,TITLE,LINK,DA,WI,HI))
            LINKS.append(LINK)
            TITLES.append(TITLE)
            DATE.append(DA)
            WIDTH.append(WI)
            HIGHT.append(HI)
        except:
            print('None')
