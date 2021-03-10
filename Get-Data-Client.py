# Echo server program
import socket
import schedule
import time
import json
from urllib.request import urlopen

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print('Connected by', addr)
while True:
    data = conn.recv(1024)
    if not data: break
    print(data) # Paging Python!
    # do whatever you need to do with the data

# optionally put a loop here so that you start 
# listening again after the connection closes
def job():
        try:
                f = urlopen('http://192.168.1.70/admin/api.php')
                json_string = f.read()
                parsed_json = json.loads(json_string)
                queries = parsed_json['dns_queries_today']
                adsblocked = parsed_json['ads_blocked_today']
                clients = parsed_json['unique_clients']
                domainsblocked = parsed_json['domains_being_blocked']
                f.close()
        except:
                queries = '-'
                adsblocked = '-'
                clients = '-'
                
        pihole = 'Domains Blocked: ' + str(queries) + ' - ' 'DNS-Queries: ' + str(queries) + ' - ' + 'Ads blocked: ' + str(adsblocked) + ' - ' + 'Devices: ' + str(clients)
        print (pihole)

        f = open("pi-hole-data.txt", "w")
        f.write(str(queries))
        f.close()

schedule.every(30).seconds.do(job)

while 1:
    schedule.run_pending()
    time.sleep(1)
    clientSocket.send(queries.encode())
