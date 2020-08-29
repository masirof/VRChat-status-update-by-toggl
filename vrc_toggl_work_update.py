import json
import requests
from requests.auth import HTTPBasicAuth
from requests_oauthlib import OAuth1Session
import base64
import time
import re
import datetime


def vrc_status_change(json_catch):
    USER = ""  # Modify: xxx@gmail.com
    PASS = ""  # Modify: VRC_password
    apiKey = ""  # Modify: apikey
    status_url = "https://api.vrchat.cloud/api/1/users/[your-vrc-usrid]" # Modify: Update-info

    API_BASE = "https://api.vrchat.cloud/api/1"
    url = "{}/auth/user".format(API_BASE)
    ua = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    # ユーザーエージェントの偽装

    # authtokenの取得
    headers = {'User-Agent': ua}
    response = requests.get(url,
                            params={"apiKey": apiKey},
                            auth=HTTPBasicAuth(USER, PASS),
                            headers=headers)  # ユーザーエージェントの偽装忘れないように
    if response.status_code != 200:
        print("Error: cannot get workspace id. please check the token.")
    else:
        token = response.cookies["auth"]
        # print(response.cookies)
        print(token)

        # ユーザーのステータスを変える
        status = "active"
        headers = {'User-Agent': ua, 'Content-Type': 'application/json'}
        # json_data = json.dumps({"status": "active", "statusDescription": "Rest-休憩中"})
        json_data = json_catch

        update_info = requests.put(status_url,
                                   json_data,
                                   params={"apiKey": apiKey,
                                           "authToken": token},
                                   auth=HTTPBasicAuth(USER, PASS),
                                   headers=headers)
        if response.status_code != 200:
            print("Error: cannot get workspace id. please check the token.")
        else:
            print(update_info)
            # print(update_info.text)


def work_time_info():
    print(data)
    Data = data['data']['id']
    description = data['data']['description']
    start = data['data']['start']
    start_re = re.search(
        r'(?<=T)[0-9]{2}:[0-9]{2}:[0-9]{2}', start)
    start_time = start_re.group()
    # JST-time change-your-country-time
    start_time_re = re.findall('\d+', start_time)
    start_time_hour = (int(start_time_re[0])+9) % 24
    start_time_minute = int(start_time_re[1])
    start_time_second = int(start_time_re[2])
    start_datetime = datetime.time(
        start_time_hour, start_time_minute, start_time_second)
    print(start_datetime)

    # ポモドーロの終わる時刻
    pomodoro_time = datetime.datetime.combine(
        datetime.date.today(), start_datetime) + datetime.timedelta(minutes=25)
    pomodoro_time_str = str(pomodoro_time)
    pomodoro_time_re = re.findall('\d+', pomodoro_time_str)
    print(pomodoro_time_re)
    pomodoro_time_hour = int(pomodoro_time_re[3])
    print(pomodoro_time_hour)
    pomodoro_time_minute = int(pomodoro_time_re[4])
    print(pomodoro_time_minute)

    # 送信するやつ
    json1 = json.dumps(
        {"status": "ask me", "statusDescription": "Work-"+description+"  EndTime "+str(pomodoro_time_hour)+':'+str(pomodoro_time_minute)+'(JST)'})
    print(json1)
    vrc_status_change(json1)


state = ''
while True:
    # togglで現在ユーザーが作業しているかの確認 request-一秒に一回

    api_token = ''  # Modify: Toggl-api-token

    r = requests.get('https://www.toggl.com/api/v8/time_entries/current',
                     auth=(api_token, 'api_token'))
    # print(r)
    if r.status_code != 200:
        print("Error: cannot get workspace id. please check the token.")
    else:
        data = r.json()  # json形式でエクスポート

        if data['data']:
            # busy-作業中
            print('作業している   ', end="")  # 存在している
            now_time = datetime.datetime.now()
            now_time_str = '{0:%Y-%m-%d %H:%M:%S}'.format(now_time)  # strに変換
            print(now_time_str)

            if state == 'rest':
               work_time_info()
               state = 'work'

            elif state == '':
               work_time_info()
               state = 'work'
        else:
            # active-休憩中
            print('作業していない  ', end="")  # 存在していない
            now_time = datetime.datetime.now()
            now_time_str = '{0:%Y-%m-%d %H:%M:%S}'.format(now_time)  # strに変換
            print(now_time_str)
            if state == 'work':
                # print(json)
                json2 = json.dumps(
                    {"status": "active", "statusDescription": "Rest-休憩中"})
                print(json2)
                vrc_status_change(json2)
                state = 'rest'

            elif state == '':
                json2 = json.dumps(
                    {"status": "active", "statusDescription": "Rest-休憩中"})
                print(json2)
                vrc_status_change(json2)
                state = 'rest'
                # state ='work'
    time.sleep(30)
