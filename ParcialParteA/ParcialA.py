import sys
import json
import boto3
import datetime
import time
import urllib3

now = datetime.datetime.now()
    
x = now.strftime("%Y")
x2 = now.strftime("%m")
x3 = now.strftime("%d")
http= urllib3.PoolManager()

url= 'https://www.eltiempo.com/'
resp= http.request('GET', url)
print(resp.data.decode('utf-8'))


url2 = 'https://www.elespectador.com/'
resp2= http.request('GET', url2)
print(resp2.data.decode('utf-8'))

client = boto3.client("s3","us-east-1")
s3= boto3.resource('s3')
bucket = s3.Bucket('parcial2primer')

client.put_object(Body=resp.data.decode('utf-8'), Bucket='parcial2primer', Key ='headlines/raw/ElTiempo/year='+ x + '/month=' + x2 + '/day=' + x3 + '/archivo1.txt')
client.put_object(Body=resp2.data.decode('utf-8'), Bucket='parcial2primer', Key ='headlines/raw/Espectador/year='+ x + '/month=' + x2 + '/day=' + x3 + '/archivo2.txt')