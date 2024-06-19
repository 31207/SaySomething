import subprocess
import sys
import json
import time
from datetime import datetime
import tkinter as tk
import yaml

config_path = '/home/Dustwind/.config/saysomething/config.yaml'
saying_path = '/home/Dustwind/.config/saysomething/saying.json'


def generate(j:list):
    res = config['forward'] + '\n\n'
    for i in j:
        s = f'```{i['time_str']}\n{i['saying']}\n```\n\n'
        res += s
    return res
        

def add_saying(s:str):
    with open(saying_path,'r') as file:
        saying = json.loads(file.read())
    tmp = {
        'time': int(time.time()),
        'time_str': datetime.now().strftime("%Y-%m-%d-%H:%M:%S"),
        'saying': s
    }
    saying = [tmp] + saying
    with open(saying_path,'w') as file:
        file.write(str(saying).replace('\'','\"'))

    res = generate(saying)
    with open(config['blogPath']+'source/碎碎念/index.md','w') as file:
        file.write(res)
    cmds = [
        f'hexo g',
        f'hexo d'
    ]
    for i in cmds:
        subprocess.run(i,text=True,shell=True,cwd=config['blogPath'])


def gui():
    wnd = tk.Tk()
    
    # 创建标签
    label = tk.Label(wnd, text="请输入内容:")
    label.pack(pady=10)  # pady用于控制控件上下的空白空间
    # 创建输入框
    entry = tk.Entry(wnd, width=30)
    entry.pack(pady=10)
    # 创建按钮
    def button_click():
        user_input = entry.get()  # 获取输入框中的文本内容
        add_saying(user_input)
    button = tk.Button(wnd, text="提交", command=button_click)
    button.pack(pady=10)
    # 创建按钮点击事件处理函数

    wnd.mainloop()


if __name__ == '__main__':
    try:
        file = open(config_path,'r')
        config = yaml.safe_load(file)
    except Exception as e:
        print(e)
    print(len(sys.argv))
    for i in sys.argv:
        print(i)
    if len(sys.argv) == 1:
        gui()
    elif len(sys.argv) == 2:
        add_saying(sys.argv[1])
    else:
        print('fuckyou')

