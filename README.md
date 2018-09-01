# FjuScoreTelegram
開發者：陳常樂 輔大資管

介紹:
這是一個自動查詢輔大暫存成績的程式，用自己設定的時間，每隔一段時間，就會自動檢查老師是否已經把成績上傳到[學生查詢暫存成績系統]上，或是上傳至教務處，如果成績有更新，這個程式就會利用Telegram發送短訊並將結果一併傳送給你。如使用此程式則可省下每日上網查詢成績的時間。

使用方法:
1. 下載手機App - Telegram  
在手機下載Telegram(聊天APP)並註冊新帳號， 然後在搜尋裡輸入"@happy_notify_helper_bot"，點開進入名為”Happy通知小幫手”的聊天機器人。

2. 尋找自己的用戶id  
在對話欄中隨便輸入文字並送出，然後打開瀏覽器並輸入"https://api.telegram.org/bot583418329:AAGb6Kx1iFIovMrFTl6wAj_bJstI9gzt6H0/getUpdates"  ，在裡面找出自己帳號的[id]， 是一串數字(例: 627272727)，先把[id]記下來。

3. 修改幾行程式碼  
打開"FjuScoreTelegram.py"，在第17-19行輸入自己的帳號、密碼以及剛剛記下來的[id]。  
第20行是暫存成績的txt文字檔，txt檔產生出來後不要刪掉，直到你不用這個程式為止。  
注:Mac和Windows的路徑長得不一樣，請根據你電腦系統的不同，而去改變路徑的寫法。  

4. 下載ChromeDriver  
先在下面連結下載ChromeDriver。  
http://chromedriver.chromium.org/downloads  
找一個資料夾把ChromeDriver放好，修改第22行程式碼，把路徑修改成你放的位置。
注:Mac和Windows的路徑長得不一樣，請根據你電腦系統的不同，而去改變路徑的寫法。

5. 嘗試執行一次Python  
你可以先嘗試執行一次Python檔，應該會出現錯誤訊息，錯誤訊息大多是因為你還沒有下載某些軟體包，如果你透過錯誤訊息知道你缺少哪個軟體包的話，可以自行在[終端機]輸入指令"pip install some-package-name"來下載。如果你不知道要如何處理的話，可以複製->錯誤訊息 然後去Google搜尋，網路上會有該軟體包下載的指令。

6. 自動定時執行Python程式的方法  
當你成功執行"FjuScoreTelegram.py”一次以後，就可以進行這個步驟，自動定時執行Python程式的方法有幾種，Windows系統可以用[工作排程]去執行，面Mac系統則是用[crontab]和[launchctl]，教學方法下以用下面的連結，或是自己去Google更多教學； 我個人是選擇用crontab。  
工作排程: https://dotblogs.com.tw/what_s_note/2017/02/14/113920  
launchctl: https://blog.csdn.net/clwwlc/article/details/79849686  
crontab:  
https://dotblogs.com.tw/jason_wang/2016/10/27/crontab
https://hk.saowen.com/a/b0f3b8cdc172a3828e2a312bf8017189f5f420dcff64086c6bee278c1fa619fc
