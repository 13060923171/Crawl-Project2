# -*- coding: utf-8 -*-
import requests
import json
import hashlib
import time
import datetime


class LexinSport:
    def __init__(self, phone, password, step):
        # 手机号
        self.phone = phone
        # 密码
        self.password = password
        # 修改步数
        self.step = step
        # 用户id
        self.user_id = ''
        # 访问令牌
        self.access_token = ''

    # 登录
    def login(self):
        url = 'https://sports.lifesense.com/sessions_service/login?systemType=2&version=4.6.7'
        data = {'loginName': self.phone, 'password': hashlib.md5(self.password.encode('utf8')).hexdigest(),
                'clientId': '49a41c9727ee49dda3b190dc907850cc', 'roleType': 0, 'appType': 6}
        headers = {
            'Content-Type': 'application/json; charset=utf-8',
            'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 7.1.2; LIO-AN00 Build/LIO-AN00)'
        }
        response = requests.post(url, data=json.dumps(data), headers=headers)
        # print('登录状态码：%s' % response.status_code)
        # print('登录返回数据：%s' % response.text)
        if response.status_code != 200:
            return '登录失败'
        else:
            response_text = json.loads(response.text)
            # 无论账号密码是否对得上，响应状态码都是200，但如果账号密码对不上，返回数据中的code就不是200
            if response_text['code'] != 200:
                return '账号密码对不上，登录失败'
            else:
                self.user_id = response_text['data']['userId']
                self.access_token = response_text['data']['accessToken']
                return '登录成功'

    # 修改步数
    def change_step(self):
        url = 'https://sports.lifesense.com/sport_service/sport/sport/uploadMobileStepV2?systemType=2&version=4.6.7'
        data = {'list': [{'DataSource': 2, 'active': 1, 'calories': int(self.step/4), 'dataSource': 2,
                          'deviceId': 'M_NULL', 'distance': int(self.step/3), 'exerciseTime': 0, 'isUpload': 0,
                          'measurementTime': time.strftime('%Y-%m-%d %H:%M:%S'), 'priority': 0, 'step': self.step,
                          'type': 2, 'updated': int(round(time.time() * 1000)), 'userId': self.user_id}]}
        headers = {
            'Content-Type': 'application/json; charset=utf-8',
            'Cookie': 'accessToken=%s' % self.access_token
        }
        response = requests.post(url, data=json.dumps(data), headers=headers)
        # print('修改步数状态码：%s' % response.status_code)
        # print('修改步数返回数据：%s' % response.text)
        if response.status_code == 200:
            return '【%s】修改步数为【%s】成功' % (self.phone, self.step)
        else:
            return '【%s】修改步数失败' % self.phone

    # 一键修改步数
    def one_click_change_step(self):
        login_result = self.login()
        if login_result != '登录成功':
            print(login_result)
            return
        change_step_result = self.change_step()
        print(change_step_result)


# 睡眠到第二天执行修改步数的时间
def get_sleep_time():
    # 第二天日期
    tomorrow = datetime.date.today() + datetime.timedelta(days=1)
    # 第二天7点时间戳
    tomorrow_run_time = int(time.mktime(time.strptime(str(tomorrow), '%Y-%m-%d'))) + 25200
    # print(tomorrow_run_time)
    # 当前时间戳
    current_time = int(time.time())
    # print(current_time)
    return tomorrow_run_time - current_time


if __name__ == "__main__":
    # 最大运行出错次数
    fail_num = 3
    while 1:
        while fail_num > 0:
            try:
                # 执行一键修改步数
                LexinSport('13613092093', '123456', 46885).one_click_change_step()
                break
            except Exception as e:
                print('运行出错，原因：%s' % e)
                fail_num -= 1
                if fail_num == 0:
                    print('修改步数失败')
        # 重置运行出错次数
        fail_num = 3
        # 获取睡眠时间
        sleep_time = get_sleep_time()
        # 睡眠到下次执行时间
        time.sleep(sleep_time)