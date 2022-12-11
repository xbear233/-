from tkinter import *
import tkinter
import tkinter.messagebox
import sys
#import speech

window = Tk()
window.title("这是Demo")
window.geometry("800x800")

l0 = tkinter.Label(window, text='风扇语音控制系统')
l0.pack()
canvas = tkinter.Canvas(window, bg='white', height=512, width=512)#画布
image_file = tkinter.PhotoImage(file='./tmp-0.gif')#图片地址
image = canvas.create_image(0,0, anchor='nw', image=image_file)#图片放在画布上
canvas.pack()#pack型排布

def fan_speech():
    import speech
    speech.say("Hello,你好,我是语音控制系统")
    while True:
        say = speech.input() # 接收语音
        speech.say("你的指令是:"+say) #说话
        if say == "开启风扇":
            speech.say("风扇已开启")
            #t.insert('insert',"[风扇状态提示] 风扇已开启！")
        elif say == "关闭风扇":
            speech.say("风扇已关闭")
            #t.insert('insert',"[风扇状态提示] 风扇已关闭！")
        elif say == "退出系统":
            break
        else : 
            speech.say("错误的指令")
            
    
l1 = tkinter.Label(window, text='点击“语音控制”按钮，再点击麦克风说话')
l1.pack()
l2 = tkinter.Label(window, text='想要开启风扇，请说：“开启风扇”')
l2.pack()
l3 = tkinter.Label(window, text='想要关闭风扇，请说：“关闭风扇”')
l3.pack()
l4 = tkinter.Label(window, text='想要退出语音控制系统，请说：“退出系统”')
l4.pack()
# 定义文本框
# t = tkinter.Text(window, 
#                  state='normal',  # 有disabled、normal 两个状态值，默认为normal
#                  width=30, height=1
#                  )
# t.pack()

first = Button(window, text="语音控制", fg="tomato", command=fan_speech)
first.pack()
b2 = tkinter.Button(window, text='退出', command=window.quit)
b2.pack()

window.mainloop()