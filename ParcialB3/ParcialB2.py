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
data = s3.download_file('parcial2primer','headlines/final/ElTiempo/year='+ x + '/month=' + x2 + '/day=' + x3 + '/procesado1.csv', '/tmp/archivo1.csv')

data2 = s3.download_file('parcial2primer','headlines/final/Espectador/year='+ x + '/month=' + x2 + '/day=' + x3 + '/procesado2.csv', '/tmp/archivo2.csv')


client = boto3.client("s3","us-east-1")
client.put_object(Body=/tmp/archivo1.csv, Bucket='parcial2primer', Key ='news/raw/ElTiempo/year='+ x + '/month=' + x2 + '/day=' + x3 + '/Final1.csv')

client.put_object(Body=/tmp/archivo2.csv, Bucket='parcial2primer', Key ='news/raw/Espectador/year='+ x + '/month=' + x2 + '/day=' + x3 + '/Final2.csv')