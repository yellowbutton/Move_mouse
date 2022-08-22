#from pynput import keyboard as nputkeyboard
import pynput
import os
aaa=os
import webbrowser
import keyboard
import tkinter as tk
#from tkinter import ttk
root=tk.Tk()
root.attributes('-fullscreen', True)
root.withdraw()
cms=tk.Toplevel()
cms.attributes('-fullscreen', True)
cms.withdraw()

#alt_r:165
#w:87

speed=7
keyweblist=[[49,"https://cn.bing.com/"],[50,"http://qdzx.idsp.yunxiao.com/"],[51,"https://gt.yxzl.top/"]]
keydolist=[[87,"ctr.move(0, -1*speed)"],[83,"ctr.move(0, speed)"],[65,"ctr.move(-1*speed,0)"],[68,"ctr.move(speed, 0)"],[82,"ctr.scroll(0, 1)"],[70,"ctr.scroll(0,-1)"],[75,"os._exit(0)"]]
1
def getkey(msg, data):
    global speed
    if data.vkCode==20:
        listener.suppress_event()
    #!print(msg)
    for keys in keydolist:
        if data.vkCode==keys[0]:
            if keyboard.is_pressed('capslock'):
                if msg==256:
                    #!print(speed)
                    eval(keys[1])
                    speed+=1
                else:
                    #!print("elsestart")
                    speed=7
                listener.suppress_event()
            else:
                #!print("elseins")
                speed=7
    if data.vkCode==81:
        if keyboard.is_pressed('capslock'):
            if msg==256:
                ctr.press(pynput.mouse.Button.left)
            else:
                ctr.release(pynput.mouse.Button.left)
            listener.suppress_event()
    if data.vkCode==88:
        if keyboard.is_pressed('capslock'):
            if msg==256:
                ctr.press(pynput.mouse.Button.middle)
            else:
                ctr.release(pynput.mouse.Button.middle)
            listener.suppress_event()
    if data.vkCode==69:
        if keyboard.is_pressed('capslock'):
            if msg==256:
                ctr.press(pynput.mouse.Button.right)
            else:
                ctr.release(pynput.mouse.Button.right)
            listener.suppress_event()
    if data.vkCode==72:
        if keyboard.is_pressed('capslock'):
            if msg==256:root.deiconify()
            else:root.withdraw()
            listener.suppress_event()
        else:root.withdraw()
    for keys in keyweblist:
        if data.vkCode==keys[0]:
            if keyboard.is_pressed('capslock'):
                if msg==256:webbrowser.open_new(keys[1])
                listener.suppress_event()
    if keyboard.is_pressed('capslock'):listener.suppress_event()
    #print(msg, data.vkCode)

tk.Label(root,font=("",30),text="\t\nCapsLock+H\t=>\t帮助界面\t\nCapsLock+W/A/S/D\t=>\t鼠标移动\t\nCapsLock+Q\t=>\t鼠标左键\t\nCapsLock+K\t=>\t退出程序\t\nCapsLock+E\t=>\t鼠标右键\t\nCapsLock+R/F\t=>\t鼠标滚轮\t\nInsect+1~3\t=>\t打开:\t\t\n\t\t\t\t搜索/爱云校/瓜田\t").pack()
ctr = pynput.mouse.Controller() 
with pynput.keyboard.Listener(win32_event_filter=getkey) as listener:
    root.mainloop()
    listener.join()
