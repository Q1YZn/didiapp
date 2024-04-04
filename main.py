import re

from core.didiapp import get_didiapp_info,Employee,send_ding_talk
import time

time_re_str = '\d{1,2}:\d{1,2}:\d{1,2}-\d{1,2}:\d{1,2}:\d{1,2}'
time_re = re.compile(time_re_str)


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




if __name__ == '__main__':
    boy = Employee
    girl = Employee
    tomboy = Employee
    tomgirl = Employee
    get_task_info_api = "https://api.didiapp.com:443/client/challenge/info/"
    token = ""
    retData = get_didiapp_info(get_task_info_api, token)

    print(retData)

    if retData == "":
        print("[-]json is null! What happen get task?")

    boy.task = retData["challenge_info"]["boy_next_task_info"]["profile"]

    boy_time = time_re.search(boy.task)[0]
    print(f"time is {boy_time}")
    boy_time_bool = deal_time(boy_time)  # 是否时间区间内 再设计一套结束前10分钟的

    boy.link = retData["challenge_info"]["boy_next_task_info"]["link"]
    boy.level = retData["challenge_info"]["boy_next_task_info"]["level"]
    boy.code_info = retData["challenge_info"]["boy_next_task_info"]["code"]

    girl.task = retData["challenge_info"]["girl_next_task_info"]["profile"]
    girl.link = retData["challenge_info"]["girl_next_task_info"]["link"]
    girl.level = retData["challenge_info"]["girl_next_task_info"]["level"]
    girl.code_info = retData["challenge_info"]["girl_next_task_info"]["code"]

    tomboy.task = retData["challenge_info"]["boy_tomorrow_task_info"]["profile"]
    tomboy.link = retData["challenge_info"]["boy_tomorrow_task_info"]["link"]
    tomboy.level = retData["challenge_info"]["boy_tomorrow_task_info"]["level"]
    tomboy.code_info = retData["challenge_info"]["boy_tomorrow_task_info"]["code"]

    tomgirl.task = retData["challenge_info"]["girl_tomorrow_task_info"]["profile"]
    tomgirl.link = retData["challenge_info"]["girl_tomorrow_task_info"]["link"]
    tomgirl.level = retData["challenge_info"]["girl_tomorrow_task_info"]["level"]
    tomgirl.code_info = retData["challenge_info"]["girl_tomorrow_task_info"]["code"]

    send_data = f"今天的男方任务是:{boy.task}\r\n跳转链接:{boy.link}\r\ncodeinfo是:{boy.code_info}\r\nlevel是:{boy.level}\r\n今天的女方任务是:{girl.task}\r\n跳转链接:{girl.link}\r\ncodeinfo是:{girl.code_info}\r\nlevel是:{girl.level}"
    print(send_data)

    send_ding_talk(boy,girl,tomboy,tomgirl)
