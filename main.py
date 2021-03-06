# import libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyautogui
from tkinter import *


class twitter_bot:
    def __init__(self,username,password):
        self.username=username
        self.password=password
        self.bot=webdriver.Firefox()

    def login(self):
        bot=self.bot
        bot.get('https://twitter.com/')
        time.sleep(5)
        email=bot.find_element_by_name('text')
        password=bot.find_element_by_name('password')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(10)

    def like_tweet(self):
        bot=self.bot
        bot.get('https://twitter.com/search?q='+str(entry3)+'&src=typed_query')
        while True:
            pyautogui.click(pyautogui.locateCenterOnScreen('https://cdn2.iconfinder.com/data/icons/media-player-ui/512/Media-Icon-25-512.png'))
            time.sleep(3)
            bot.execute.script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(3)


def execute():
    log = twitter_bot(str(entry1.get()), str(entry2.get()))
    log.login()
    log.like_tweet(entry3.get())


window = Tk()
window.geometry('700x600')
emails = Label(window,text="Enter your email", font='times 20 bold')
emails.grid(row=0, column=0)
entry1=Entry(window)
entry1.grid(row=0,column=6)
# entry for password
password=Label(window,text="Enter your Password",font='times 20 bold')
password.grid(row=2,column=0)
entry2=Entry(window)
entry2.grid(row=2,column=6)
# entry for hashtag
hashtag=Label(window,text="Enter your Hashtag",font='times 20 bold')
hashtag.grid(row=3,column=0)
entry3=Entry(window)
entry3.grid(row=3,column=6)

# button
b1=Button(window,text="G0",command=execute,width=12,bg='gray')
b1.grid(row=7,column=4)
window.mainloop()


