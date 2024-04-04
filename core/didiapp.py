from dingtalkchatbot.chatbot import DingtalkChatbot, ActionCard, CardItem
import requests,urllib3
urllib3.disable_warnings()

class Employee:
    pass

def get_didiapp_info(api, token):
    burp0_url = api
    burp0_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0",
                     "access_token": token,
                     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
                     "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
                     "Accept-Encoding": "gzip, deflate", "Connection": "close", "Upgrade-Insecure-Requests": "1",
                     "Sec-Fetch-Dest": "document", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-Site": "none",
                     "Sec-Fetch-User": "?1", "Pragma": "no-cache", "Cache-Control": "no-cache"}
    r = requests.get(burp0_url, headers=burp0_headers,verify=False)
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