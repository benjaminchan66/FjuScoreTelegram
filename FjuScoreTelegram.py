
# coding: utf-8

# In[1]:

import requests
from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep
import os
import urllib.request as req
import urllib.parse as parse

# In[2]:

url = 'http://140.136.251.162/StuScore/login.aspx'
userId = ''     # 405283291(帳號)
userPw = ''     # ********(密碼)
chatId = ''     # 627272727(id)
file_path = "score.txt"     #你成績暫存檔案的路徑，請根據你的電腦做出改變，txt檔產生出來後不要刪掉，直到你不用這個程式為止。

browser = webdriver.Chrome('/Users/BENJAMIN/anaconda/chromedriver')     #把路徑改成你放chromedriver的資料夾。
browser.get(url)
browser.find_element_by_id('ctl00_ContentPlaceHolder1_idtb').clear()
browser.find_element_by_id('ctl00_ContentPlaceHolder1_idtb').send_keys(userId)
browser.find_element_by_id('ctl00_ContentPlaceHolder1_pawtb').clear()
browser.find_element_by_id('ctl00_ContentPlaceHolder1_pawtb').send_keys(userPw)
browser.find_element_by_id('ctl00_ContentPlaceHolder1_loginButton').click()


# In[3]:

soup = BeautifulSoup(browser.page_source)


# In[4]:

itemList = []

for i in range(len(soup.select('#ctl00_ContentPlaceHolder1_scoreGV tr td'))):
    str = soup.select('#ctl00_ContentPlaceHolder1_scoreGV tr td')[i].text.strip()
    if(i % 4 != 0):
        start_index = str.find('/')
        if(start_index != -1):
            itemList.append(str[:start_index])
        else:
            itemList.append(str)


# In[5]:

#[爬下來的資料]整理
newItemList = []
string = ''
count1 = 0
for item in itemList:
    count1 += 1
    if(count1%3 == 0):
        string = string + "," + item
        newItemList.append(string[1:])
        string = ''
    else:
        string = string + ',' + item


# In[6]:

#讀取[舊資料]
oldItemList = []
 
if(os.path.isfile(file_path)):
    text_file = open(file_path, "r", encoding='utf-8')
    oldItemList = text_file.readlines()
    count3 = 0

    for oldItem in oldItemList:
        oldItemList[count3] = oldItem.strip()
        count3 +=1
else:
    text_file = open(file_path, "w", encoding='utf-8')
    count2 = 0
    for item in itemList:
        count2 += 1
        if(count2%3 == 0):
            text_file.write("%s\n" % item)
        else:
            text_file.write("%s," % item)
    text_file.close()


# In[7]:

#把[爬下來的資料]跟[舊資料]做比對
isNewList = []
count4 = 0
for i in range(len(newItemList)):
    for j in range(len(oldItemList)):
        if(newItemList[i] == oldItemList[j]):
            count4 += 1


    if(count4 > 0):
        isNewList.append(1)
    else:
        isNewList.append(0)
    count4 = 0


# In[8]:

for i in range(len(isNewList)):
#     print(isNewList[i])
    if(isNewList[i] == 0):
        result = req.urlopen("https://api.telegram.org/bot583418329:AAGb6Kx1iFIovMrFTl6wAj_bJstI9gzt6H0/sendMessage?chat_id=" + chatId + "&text=" + parse.quote("你的成績有更新: \n"+newItemList[i]))


# In[9]:

#把爬蟲結果寫入txt
text_file = open(file_path, "w", encoding='utf-8')
count2 = 0
for item in itemList:
    count2 += 1
    if(count2%3 == 0):
        text_file.write("%s\n" % item)
    else:
        text_file.write("%s," % item)
text_file.close()


# In[10]:

browser.quit()




