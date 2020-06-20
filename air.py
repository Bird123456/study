import requests
import re
import xlwt

url = 'https://flights.ctrip.com/?'
headers = {
    #修改为自己的
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"

}


def get_page(url):
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            print (1)
            return response.text
        else:
            print('获取网页失败')
    except Exception as e:
        print(e)


def get_info(page):
    # print(123)
    items = re.findall('<strong class="pubFlights_.*? " .*?>(.*?)</strong></a><br>.*?<strong class="time">(.*?)</strong>'
                       '.*?<div class="airport" .*?>(.*?)</div>.*?<strong class="time">(.*?)</strong>'
                       '.*?<div class="airport" .*?>(.*?)</div>',page,re.S)
    # print(123)
    for item in items:
        data = {}
        data['num'] = item[0]
        data['timeleft'] = item[1]
        data['airportleft']=item[2]
        data['timearrive'] = item[3]
        data['airportarrive'] = item[4]
        # data['lefttime']=item[5]
        # print (123)
        print(data)
        yield data

basic_url = 'https://flights.ctrip.com/domestic/schedule/'
last_url='.html'
list=['can','bjs','sha','szx','ctu','hgh','wuh','sia','ckg','tao','csx','nkg','xmn','kmg','dlc','tsn','cgo','syx','tna','foc']   #携程上的名称参数
list1=['can','bjs','sha','szx','ctu','hgh','wuh','sia','ckg','tao','csx','nkg','xmn','kmg','dlc','tsn','cgo','syx','tna','foc']  #携程上的名称参数
DATA = [] #对保存数据全局变量初始化
for x in list:
    for y in list1:
        if(x!=y):
            urls = [basic_url +x+str('.')+y+ str('.p')+str(i)+last_url for i in range(1, 7)]  # 所有url都urls里。
# urls = ['https://flights.ctrip.com/domestic/schedule/bjs.sha.p1.html?']

            for url in urls:
                 print (url)
                 page = get_page(url)
                 print (11)
                 datas = get_info(page)
                 for data in datas:
                    DATA.append(data)  # 将所有的数据添加到DATA里

f = xlwt.Workbook(encoding='utf-8')
sheet01 = f.add_sheet(u'sheet1', cell_overwrite_ok=True)
sheet01.write(0, 0, 'num')  # 第一行第一列
sheet01.write(0, 1, 'timeleft')  # 第一行第二列
sheet01.write(0, 2, 'airportleft')  # 第一行第三列
sheet01.write(0, 3, 'timearrive')  # 第一行第四列
sheet01.write(0, 4, 'airportarrive')  # 第一行第五列
# sheet01.write(0, 5, 'lefttime')  # 第一行第六列
# 写内容
for i in range(len(DATA)):
    sheet01.write(i + 1, 0, DATA[i]['num'])
    sheet01.write(i + 1, 1, DATA[i]['timeleft'])
    sheet01.write(i + 1, 2, DATA[i]['airportleft'])
    sheet01.write(i + 1, 3, DATA[i]['timearrive'])
    sheet01.write(i + 1, 4, DATA[i]['airportarrive'])
    # sheet01.write(i + 1, 5, DATA[i]['lefttime'])
    print( end='')
f.save('F:\Python\pachong\飞机热门旅程.xls')
