# For prerequisites running the following sample, visit https://help.aliyun.com/document_detail/611472.html
# export DASHSCOPE_API_KEY=sk-3876d2fa763d431ca3aad55f841586c0
import requests
import json
import time
from http import HTTPStatus
import tkinter as tk
from tkinter import scrolledtext
import pyperclip
import threading
import tkinter.font as tkFont


#导入库
import ctypes
from tkinter import *
from tkinter.ttk import *

# #创建窗口，root可替换成自己定义的窗口
# root=Tk()
# #调用api设置成由应用程序缩放
# ctypes.windll.shcore.SetProcessDpiAwareness(1)
# #调用api获得当前的缩放因子
# ScaleFactor=ctypes.windll.shcore.GetScaleFactorForDevice(0)
# #设置缩放因子
# root.tk.call('tk', 'scaling', ScaleFactor/75)

text = 'init'
def call_with_messages(msg):
    url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions_pro?access_token=" + get_access_token()

    payload = json.dumps({
        "messages": [
            {
                "role": "user",
                "content": f"{msg}"
            }
        ]
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    res = json.loads(response.text)['result']
    # print(res)

    if response.status_code == HTTPStatus.OK:
        # print(response)
        # print(response.output.choices[0].message.content)
        return json.loads(response.text)['result']
    else:
        return 'query failed'



def get_access_token():
    """
    使用 API Key，Secret Key 获取access_token，替换下列示例中的应用API Key、应用Secret Key
    """

    url = "https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=MuNqpK3nENzTU5Ci8PSYTyL0&client_secret=xqlyev8nt8CNptaVyMTgDfw79NNtizd0"

    payload = json.dumps("")
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json().get("access_token")


def update_clipboard():
    try:
        last_text = pyperclip.paste()  # 初始时读取剪贴板内容

        while True:  # 使用全局变量running来控制循环
            current_text = pyperclip.paste()  # 不断检查当前剪贴板内容

            if current_text != last_text:  # 如果发生了变化
                print('-------------------------------------------------')
                text_to_insert = "剪贴板内容改变:" + current_text + "\n\n"
                print(text_to_insert)
                res = call_with_messages(current_text)
                print(res)
                # global text
                # text = text_to_insert + res
                # text_area.configure(state='normal')  # 解锁文本区域以便插入文本
                # text_area.insert(tk.END, text_to_insert + res + '\n')
                # text_area.configure(state='disabled')  # 再次锁定文本区域

                last_text = current_text  # 更新最后一次看到的内容以便下次比较

            time.sleep(0.5)  # 加上延时减少资源消耗

    except Exception as e:
        running = False  # 出现异常时停止线程循环


# # 建立窗口界面
# root = tk.Tk()
# root.title("剪贴板监视器")
# # 定义一个更大且易读的字体样式
# my_font = tkFont.Font(family="Monospaced", size=12)  # “微软雅黑”
# text_area = scrolledtext.ScrolledText(root, state='disabled', height=50, font=my_font)
# text_area.pack()
#
# # 开启后台线程来更新剪贴板内容显示在GUI上.
threading.Thread(target=update_clipboard).start()
#
#
# # 当关闭窗口时设置running为False，确保后台线程可以退出。
# def on_closing():
#     root.destroy()
#
#
# root.protocol("WM_DELETE_WINDOW", on_closing)
#
# # 主事件循环从这儿开始执行。
# root.mainloop()