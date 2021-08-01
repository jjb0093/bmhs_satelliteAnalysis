from bs4 import BeautifulSoup
import requests
import urllib.request

data = ["wv069"]
area="ko"
time="20210603"
key=""

for j in range(len(data)):
    print(data[j])
    url="http://apis.data.go.kr/1360000/SatlitImgInfoService/getInsightSatlit?serviceKey="+key+"&numOfRows=200&pageNo=1&sat=g2&data="+data[j]+"&area="+area+"&time="+time

    res = requests.get(url)
    html = res.text
    parse = BeautifulSoup(html, 'html.parser')
    fileURL = parse.find_all('satimgc-file')

    downloadAdd = "StateLite_DATA/KO" + "/" +  time + "/" + data[j] + "/"

    for i in range(522, len(fileURL)):

        #print(str(fileURL[i])[-35:-23])
        downloadName = str(fileURL[i])[-35:-23] + ".png"
        downloadURL = str(fileURL[i])[14:-15]
        urllib.request.urlretrieve(downloadURL, downloadAdd + downloadName)
        print(i)
