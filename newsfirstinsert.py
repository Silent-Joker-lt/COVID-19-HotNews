#coding=gbk
"""
Written By Silent_Joker
2020��11��26��
"""
import requests
import json
import pymysql
import time

# ��ȡ����
# ��������
# url0 = 'https://opendata.baidu.com/data/inner?tn=reserved_all_res_tn&dspName=iphone&from_sf=1&dsp=iphone&resource_id=28565&alr=1&query=%E5%9B%BD%E5%86%85%E6%96%B0%E5%9E%8B%E8%82%BA%E7%82%8E%E6%9C%80%E6%96%B0%E5%8A%A8%E6%80%81&cb'
# headers = {'User-Agent': 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0'}
# r1 = requests.get(url0, headers=headers)
# state1 = json.loads(r1.text).get('Result')
# dataAll = state1[0]['items_v2'][0]['aladdin_res']['DisplayData']['result']['items']

def dataget(inOut):
    url = ['https://opendata.baidu.com/data/inner?tn=reserved_all_res_tn&dspName=iphone&from_sf=1&dsp=iphone&resource_id=28565&alr=1&query=%E5%9B%BD%E5%86%85%E6%96%B0%E5%9E%8B%E8%82%BA%E7%82%8E%E6%9C%80%E6%96%B0%E5%8A%A8%E6%80%81&cb',
            'https://opendata.baidu.com/data/inner?tn=reserved_all_res_tn&dspName=iphone&from_sf=1&dsp=iphone&resource_id=28565&alr=1&query=%E5%9B%BD%E5%A4%96%E6%96%B0%E5%9E%8B%E8%82%BA%E7%82%8E%E6%9C%80%E6%96%B0%E5%8A%A8%E6%80%81&cb']
    headers = {
        'User-Agent': 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0'}
    r1 = requests.get(url[inOut], headers=headers)
    state1 = json.loads(r1.text).get('Result')
    dataAll = state1[0]['items_v2'][0]['aladdin_res']['DisplayData']['result']['items']
    data=[]
    for i in range(len(dataAll)):
        dataOne = dataAll[i]
        event_time = int(dataOne['eventTime'])
        local_time = time.localtime(event_time)
        finalTime = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
        event = dataOne['eventDescription']
        eventUrl = dataOne['eventUrl']
        source = dataOne['siteName']
        yuanzu = ()
        yuanzu = yuanzu + (finalTime,) + (event,) + (eventUrl,) + (source,)
        data.append(yuanzu)
    return data
def news(inOut):
    conn = pymysql.connect("localhost", "root", "", charset="utf8")
    cur = conn.cursor()  # ��ȡ���ݿ�Ĺ��
    conn.select_db("����")
    data = dataget(inOut)
    base = ['��������', '��������']
    cur.executemany("INSERT INTO {}(ʱ��, �¼�����,�¼���ַ,�¼���Դ) VALUES (%s,%s,%s,%s)".format(str(base[inOut])), data)
    conn.commit()  # ����
    cur.close()
    conn.close()
