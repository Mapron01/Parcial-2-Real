import sys
import json
import boto3
import datetime
import time
import urllib3

from bs4 import BeautifulSoup

now = datetime.datetime.now()

x = now.strftime("%Y")
x2 = now.strftime("%m")
x3 = now.strftime("%d")

s3 = boto3.client('s3')
data = s3.download_file('parcial2primer','headlines/raw/ElTiempo/year='+ x + '/month=' + x2 + '/day=' + x3 + '/archivo1.txt', '/tmp/archivo1.txt')

data2 = s3.download_file('parcial2primer','headlines/raw/Espectador/year='+ x + '/month=' + x2 + '/day=' + x3 + '/archivo2.txt', '/tmp/archivo2.txt')

with open("/tmp/archivo1.txt") as fp:
    soup = BeautifulSoup(fp, 'html.parser')

Title1 = soup.find_all(class_="title page-link")
Category1 = soup.find_all(class_="category-published")
Link1 = soup.find_all(class_="multimediatag page-link")


s = ""
for i in range(len(Title1)):
    s = s + Title1[i].contents[0] + "\n"


client = boto3.client("s3","us-east-1")
client.put_object(Body=s, Bucket='parcial2primer', Key ='headlines/final/ElTiempo/year='+ x + '/month=' + x2 + '/day=' + x3 + 'procesado1.csv')

with open("/tmp/archivo2.txtt") as fp:
    soup2 = BeautifulSoup(fp, 'html.parser')


Title2 = soup2.find_all(class_="title page-link")


p = ""
for i in range(len(Title2)):
    s = p + Title2[i].contents[0] + "\n"

client.put_object(Body=p, Bucket='parcial2primer', Key ='headlines/final/Espectador/year='+ x + '/month=' + x2 + '/day=' + x3 + 'procesado2.csv')