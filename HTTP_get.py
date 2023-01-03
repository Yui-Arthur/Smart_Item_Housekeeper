import requests
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("-ip" , dest="ip" , default="192.168.0.221")
parser.add_argument("-p" , dest="port" , default="3000")
parser.add_argument("-person_name" ,"--N", dest="person_name" , default="-1")

url = "http://" + parser.parse_args().ip + ":" + parser.parse_args().port + "/person/" + parser.parse_args().person_name

r = requests.get(url)

if r.status_code == requests.codes.ok:
  print("OK" , end=" ")
  
print(r.text , end="")
