from tkinter import *
import tkinter.messagebox as messagebox

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.helloLabel = Label(self, text='Hello, world!')
        self.helloLabel.pack()
        self.quitButton = Button(self, text='Quit', command=self.quit)
        self.quitButton.pack()

app = Application()
# 设置窗口标题:
app.master.title('Hello World')
# 主消息循环:
app.mainloop()

class application1(Frame):
    def __init__(self):
        Frame.__init__(self,None)
        self.pack()
        self.createwigets()
    def createwigets(self):
        self.nameinput=Entry()
        self.nameinput.pack()
        self.altertbutton=Button(self,text='hello',command=self.hello)
        self.altertbutton.pack()
    def hello(self):
        name=self.nameinput.get()   
        messagebox.showinfo('message title','hello,%s'%name)
app1=application1()
app1.master.title('hello,title')
app1.mainloop()