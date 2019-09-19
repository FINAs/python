import requests
import json
import re
import calendar
import time
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
response = requests.get('https://tvc4.forexpros.com/',headers=headers)
carrier = re.findall('carrier=([^&]+)', response.text)[0]
symbols = ['40820', '518880', '2111','510050','510300','510500']
duration = ["1401083200", str(calendar.timegm(time.gmtime()))]
def getData():
  for i in symbols:
    url = 'https://tvc4.forexpros.com/'+carrier+'/1557817526/1/1/8/history?symbol=' + \
        i+'&resolution=D&from='+duration[0]+'&to='+duration[1]
    print('get '+i +' data')
    r = requests.get(url,headers=headers)
    
    # print(json.loads(r.content))
    # print(r.content)
    with open('data'+ i +'.json', 'w') as outfile:
     json.dump(json.loads(r.content),outfile)
     print('save ' + i + 'data')

def main():
  getData()

if __name__ == "__main__":
    # execute only if run as a script
    main()
