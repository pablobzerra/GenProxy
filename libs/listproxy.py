import requests
import json

url = "https://proxylist.geonode.com/api/proxy-list?limit=500&page=1&sort_by=lastChecked&sort_type=desc"

class ListProxy():

    def gen():
        data = requests.get(url).text
        data = json.loads(data)
        for data in data["data"]:
            ip = data["ip"]
            port = data["port"]
            protocol = data["protocols"]
            country = data["country"]
            city = data["city"]
            ping = data["latency"]
            anonlevel = data["anonymityLevel"]

            a = f'''
==================================
            {protocol[0]}
IP: {ip}
PORT: {port}
PAIS: {country}
CIDADE: {city}
LATENCIA: {ping}

==================================

            '''
            #print(a)
            print(f"[ {protocol[0]} ] | {anonlevel} | {country} | {ip} | {port}")