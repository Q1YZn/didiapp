from core.didiapp import get_didiapp_info,Employee,send_ding_talk



if __name__ == '__main__':
    get_task_info_api = "https://api.didiapp.com:443/client/challenge/info/"
    token = ""
    retData = get_didiapp_info(get_task_info_api, token)
    print(retData)

    if retData == "":
        print("[-]json is null! What happen get task?")

    boy_task = retData["challenge_info"]["boy_next_task_info"]["profile"]
    boy_link = retData["challenge_info"]["boy_next_task_info"]["link"]
    boy_level = retData["challenge_info"]["boy_next_task_info"]["level"]
    boy_code_info = retData["challenge_info"]["boy_next_task_info"]["code"]
    boy = Employee(boy_task,boy_link,boy_level,boy_code_info)

    girl_task = retData["challenge_info"]["girl_next_task_info"]["profile"]
    girl_link = retData["challenge_info"]["girl_next_task_info"]["link"]
    girl_level = retData["challenge_info"]["girl_next_task_info"]["level"]
    girl_code_info = retData["challenge_info"]["girl_next_task_info"]["code"]
    girl = Employee(girl_task,girl_link,girl_level,girl_code_info)


    tomboy_task = retData["challenge_info"]["boy_tomorrow_task_info"]["profile"]
    tomboy_link = retData["challenge_info"]["boy_tomorrow_task_info"]["link"]
    tomboy_level = retData["challenge_info"]["boy_tomorrow_task_info"]["level"]
    tomboy_code_info = retData["challenge_info"]["boy_tomorrow_task_info"]["code"]

    tomgirl_task = retData["challenge_info"]["girl_tomorrow_task_info"]["profile"]
    tomgirl_link = retData["challenge_info"]["girl_tomorrow_task_info"]["link"]
    tomgirl_level = retData["challenge_info"]["girl_tomorrow_task_info"]["level"]
    tomgirl_code_info = retData["challenge_info"]["girl_tomorrow_task_info"]["code"]


    tomboy = Employee(tomboy_task,tomboy_link,tomboy_level,tomboy_code_info)
    tomgirl = Employee(tomgirl_task,tomgirl_link,tomgirl_level,tomgirl_code_info)

    send_data = (
        f"今天的男方任务是:{boy.task}\r\n跳转链接:{boy.link}\r\ncodeinfo是:{boy.code_info}\r\nlevel是:{boy.level}\r\n\r\n"
        f"今天的女方任务是:{girl.task}\r\n跳转链接:{girl.link}\r\ncodeinfo是:{girl.code_info}\r\nlevel是:{girl.level}\r\n\r\n"
        f"明天的男方任务是:{tomboy.task}\r\n跳转链接:{tomboy.link}\r\ncodeinfo是:{tomboy.code_info}\r\nlevel是:{tomboy.level}\r\n\r\n"
        f"明天的女方任务是:{tomgirl.task}\r\n跳转链接:{tomgirl.link}\r\ncodeinfo是:{tomgirl.code_info}\r\nlevel是:{tomgirl.level}\r\n\r\n"
        )
    print(send_data)

    send_ding_talk(boy,girl,tomboy,tomgirl)
