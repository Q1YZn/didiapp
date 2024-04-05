from dingtalkchatbot.chatbot import DingtalkChatbot, ActionCard, CardItem
import requests,urllib3
urllib3.disable_warnings()
import time,re

time_re_str = '\d{1,2}:\d{1,2}:\d{1,2}-\d{1,2}:\d{1,2}:\d{1,2}'
time_re = re.compile(time_re_str)

class Employee:
    def __init__(self,task,link,level,code_info):
        self.task = task
        self.link = link
        self.level = level
        self.code_info = code_info
        boy_time = time_re.search(self.task)[0]
        print(f"time is {boy_time}")
        boy_time_bool = deal_time(boy_time)  # 是否时间区间内 再设计一套结束前10分钟的


def deal_time(today_task_time):
    today_year = time.strftime("%Y-%m-%d", time.localtime())
    now_timestamp = int(time.time())
    if len(today_task_time.split("-")) < 2:
        return False
    start_time = today_year + " " + today_task_time.split("-")[0]
    end_time = today_year + " " + today_task_time.split("-")[1]

    if start_time[-8] == '2' and start_time[-7] == '4':  # 只有24点的这个情况需要处理
        start_time = today_year + " " + "23:59:00"
    if end_time[-8] == '2' and end_time[-7] == '4':
        end_time = today_year + " " + "23:59:00"

    start_time_array = time.strptime(start_time, "%Y-%m-%d %H:%M:%S")
    start_time_stamp = int(time.mktime(start_time_array))
    print(f"start time {start_time_stamp}")

    end_time_array = time.strptime(end_time, "%Y-%m-%d %H:%M:%S")
    end_time_stamp = int(time.mktime(end_time_array))
    print(f"end time {end_time_stamp}")

    if start_time_stamp < now_timestamp < end_time_stamp:
        print("在时间区间内")
        return True
    else:
        print("不在时间区间内")
        return False



def get_didiapp_info(api, token):
    burp0_url = api
    burp0_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0",
                     "access_token": token,
                     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
                     "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
                     "Accept-Encoding": "gzip, deflate", "Connection": "close", "Upgrade-Insecure-Requests": "1",
                     "Sec-Fetch-Dest": "document", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-Site": "none",
                     "Sec-Fetch-User": "?1", "Pragma": "no-cache", "Cache-Control": "no-cache"}
    r = requests.get(burp0_url, headers=burp0_headers,verify=False) #,proxies={"https": "http://127.0.0.1:8080"}
    reponse_json = ""
    if r.status_code == 200:
        reponse_json = r.json()

    return reponse_json

def send_ding_talk(boy,girl,tomboy,tomgirl):
    # WebHook地址
    webhook = 'https://oapi.dingtalk.com/robot/send?access_token='
    # secret = 'SEC11b9...这里填写自己的加密设置密钥'  # 可选：创建机器人勾选“加签”选项时使用
    # 初始化机器人小丁
    xiaoding = DingtalkChatbot(webhook)  # 方式一：通常初始化方式
    # xiaoding = DingtalkChatbot(webhook)  # 方式二：勾选“加签”选项时使用（v1.5以上新功能）
    # xiaoding = DingtalkChatbot(webhook, pc_slide=True)  # 方式三：设置消息链接在PC端侧边栏打开（v1.5以上新功能）
    # Text消息@所有人
    send_data = (f"今天的男方任务是:{boy.task}\r\n跳转链接:{boy.link}\r\ncodeinfo是:{boy.code_info}\r\nlevel是:{boy.level}\r\n\r\n"
                 f"今天的女方任务是:{girl.task}\r\n跳转链接:{girl.link}\r\ncodeinfo是:{girl.code_info}\r\nlevel是:{girl.level}\r\n\r\n"
                 f"明天的男方任务是:{tomboy.task}\r\n跳转链接:{tomboy.link}\r\ncodeinfo是:{tomboy.code_info}\r\nlevel是:{tomboy.level}\r\n\r\n"
                 f"明天的女方任务是:{tomgirl.task}\r\n跳转链接:{tomgirl.link}\r\ncodeinfo是:{tomgirl.code_info}\r\nlevel是:{tomgirl.level}\r\n\r\n"
                 )
    xiaoding.send_text(msg=send_data, is_at_all=False)