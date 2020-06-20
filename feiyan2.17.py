import requests
import json


def Down_data():
    url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5'
    headers = {
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Mobile Safari/537.36'
    }
    r = requests.get(url, headers)
    res = json.loads(r.text)
    data_res = json.loads(res['data'])
    return data_res


def Parse_data1():
    data = Down_data()
    list = ['截至时间：' + str(data['lastUpdateTime']) + '\n'
                                        '全国确诊人数：' + str(data['chinaTotal']['confirm']) + '\n'
                                        '今日新增确诊：' + str(data['chinaAdd']['confirm']) + '\n'
                                        '全国疑似：' + str(data['chinaTotal']['suspect']) + '\n'
                                        '今日新增疑似：' + str(data['chinaAdd']['suspect']) + '\n'
                                        '全国治愈：' + str(data['chinaTotal']['heal']) + '\n'
                                        '今日新增治愈：' + str(data['chinaAdd']['heal']) + '\n'
                                        '全国死亡：' + str(data['chinaTotal']['dead']) + '\n'
                                        '今日新增死亡：' + str(data['chinaAdd']['dead']) + '\n']
    result = ''.join(list)
    with open('肺炎查询2.17.txt', 'a+', encoding="utf-8") as f:
        f.write(result + '\n')


def Parse_data2():
    data = Down_data()['areaTree'][0]['children']
    list = ['湖北','广东','河南','浙江','湖南','安徽','江西','江苏','重庆','山东','四川','黑龙江','北京','上海','河北','福建','陕西','广西','云南','海南','贵州'
        , '山西', '天津', '辽宁', '甘肃', '吉林', '新疆', '内蒙古', '宁夏', '香港', '台湾', '青海', '澳门', '西藏']


    for i in data:
        for x in list:
            if x in i['name']:
                for item in i['children']:
                 list_city = [
                     '地区: ' + str(item['name']) + '\n'
                     ' 累计确诊：' + str(item['total']['confirm']),
                     ' 新增确诊：' + str(item['today']['confirm']),
                     ' 累计治愈：' + str(item['total']['heal']),
                     ' 累计死亡：' + str(item['total']['dead']) + '\n'
                 ]
                 res_city = ''.join(list_city)
                 with open('肺炎查询2.17.txt', 'a+', encoding="utf-8") as f:
                      f.write(res_city)


Down_data()
Parse_data1()
Parse_data2()
