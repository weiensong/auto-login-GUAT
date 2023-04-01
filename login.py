# coding:utf-8
# Date: 2021/7/19
# Time: 14:41
# Author: Toutoutoutouer
# E-mail: wes0018@aliyun.com
# D:\Anacodar\python.exe
import requests
from bs4 import BeautifulSoup
from win10toast import ToastNotifier


def message(title, content):
    ToastNotifier().show_toast(title, content, icon_path=None, duration=5, threaded=True)


try:
    print('连接校园网中请稍等。。。')
    # 验证连接校园网成功
    url = 'http://10.1.2.3'
    response1 = requests.get(url)
    response1.encoding = 'utf-8'
    if response1.status_code == 200:
        bs = BeautifulSoup(response1.content, 'html.parser')
        if '上网登录页' in bs.text:
            header = {
                'Accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
                'Connection': '参数',
                'Cookie': '参数',
                'Host': '10.1.2.3',
                'Referer': '参数',
                'User-Agent': '参数',
                'X-Requested-With': '参数',
            }

            # 构造登录数据
            data = {
                'callback': '参数',
                'DDDDD': '你的账号',
                'upass': '你的密码',
                '0MKKey': '123456',
                'R1': '0',
                'R3': '参数',
                'R6': '0',
                'para': '00',
                'v6ip': '参数',
            }
            # 发送post请求登录网页
            response = requests.post(url, data=data, headers=header)
            response2 = requests.get(url)
            bs = BeautifulSoup(response2.content, 'html.parser')
            if '注销页' in bs.text:
                message('校园网自动登录python程序', '登录成功')
                exit()
            else:
                message('校园网自动登录python程序', '登录失败')
                exit()
    else:
        message('校园网自动登录python程序', '连接校园网失败')
        exit()
except:
    message('校园网自动登录python程序', '网络未连接')
