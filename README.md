# AIOT_final
## 要求
- [darknet](https://github.com/AlexeyAB/darknet)
- [openpose](https://github.com/CMU-Perceptual-Computing-Lab/openpose)
- [GPT2-chitchat](https://github.com/yangjianxin1/GPT2-chitchat)
- [OpenCC](https://github.com/BYVoid/OpenCC)
- 註冊 [LINE Developers](https://developers.line.biz/zh-hant/) 和 [Imgur](https://imgur.com/)

## 使用說明

### 1. 檔案結構
- 下載 [pytorch_model.bin](https://github.com/Kenhchs/large-files/blob/main/GPT2/pytorch_model.bin?raw=true) , [config.json](https://github.com/Kenhchs/large-files/blob/main/GPT2/config.json?raw=true) , [coin_counter_29_v2.weights](https://github.com/Kenhchs/large-files/blob/main/yolov4/coin_counter_29_v2.weights?raw=true) ,  [mask_137.weights](https://github.com/Kenhchs/large-files/blob/main/yolov4/mask_137.weights?raw=true)

- 在 ```ActionScoring_Image``` 裡創建3個資料夾名稱為 ```Image``` , ```outputJson``` , ```RenderImage```
- 在 ```ActionScoring_Video``` 裡創建3個資料夾名稱為 ```CompareJson``` , ```SampleJson``` , ```VideoSource```
- 將 ```pytorch_model.bin``` 和 ```config.json``` 放到 ```GPT2-chitchat/model/```
- 將 ```chat.py``` 放到 ```GPT2-chitchat/```
- 將 ```GPT2-chitchat``` 放到 ```darknet/```
- 在 ```darknet/``` 創建 ```Stock``` 資料夾再把 ```stock.py``` 放到 ```Stock/```
- 將 ```coin_counter_29.cfg``` 和 ```mask_137.cfg``` 放到 ```darknet/cfg/```
- 將 ```coin_counter_29.data``` 和 ```mask_137.data``` 放到 ```darknet/data/``` 
- 將 ```app.py``` , ```auth.ini``` , ```coin_counter_29_v2.weights``` , ```mask_137.weights``` , ```openpose``` , ```ActionScoring_Image``` , ```ActionScoring_Video``` 放到 ```darknet/```
- 檔案結構如下
```
darknet
│ README.md    
│
|
└───ActionScoring_Image
|      |  Image
|      |  outputJson
|      |  RenderImage
|      |  ImageJudge.py
|
|
└───ActionScoring_Video
|      |  CompareJson
|      |  SampleJson
|      |  VideoSource
|      |  FinalVideoScore.txt
|      |  videoJudger.py
|
|
└───GPT2-chitchat
│      └───model
|      |     |  pytorch_model.bin
|      |     |  config.json
|      |
│      │  chat.py
│      |......
|
|
│      
└───Stock
│      │  stock.py
|
|
└───cfg
|      |  coin_counter_29.cfg
|      |  mask_137.cfg
|      |......
|
|
└───data
|      |  coin_counter_29.data
|      |  mask_137.data
|      |......
|
|
| app.py
| auth.ini
| coin_counter_29_v2.weights
| mask_137.weights
|......
```
### 2. Imgur
- 打開 ```auth.ini``` ,  ```imgur_username``` 和 ```imgur_password``` 分別填入你 imgur 的帳號和密碼 
- 註冊 [Imgur App](https://api.imgur.com/oauth2/addclient)<br>
- Authorization type 選擇第二個不用回傳 URL<br>
![alt text](https://github.com/Kenhchs/Image/blob/main/imgur1.png) <br>
- 輸入完 email 後按下 ```submit``` , 就可以看到 App 的 Client ID 和 Client secret , 把這個數值填入```auth.ini``` , 也記住這兩個數值等一下會用到<br>
![alt text](https://github.com/Kenhchs/Image/blob/main/imgur2.png)<br>
- 註冊了 App 後 , 在個人設定(settings)的 Applications 中就會看到了<br>
![alt text](https://github.com/Kenhchs/Image/blob/main/imgur3.png)<br>
- 按下 ```Redirect``` 的 ```edit``` , 輸入 ```https://www.getpostman.com/oauth2/callback``` , 再按下 ```update``` <br>
![alt text](https://github.com/Kenhchs/Image/blob/main/imgur4.png)<br>
- 下載 [Postman](https://www.postman.com/downloads/)<br>
- 開啟 Postman , 選擇新建 ```Request```<br>
![alt text](https://github.com/Kenhchs/Image/blob/main/imgur5.png)<br>
- ```TYPE``` 選擇 ```OAuth 2.0``` , 再點 ```Get New Access Token```<br>
![alt text](https://github.com/Kenhchs/Image/blob/main/imgur6.png)<br>
- 點完後會出現以下畫面 , ```Client ID```、```Client Secret``` 填註冊完App後葉面顯示的 ,```Token Name```隨意 , 其他跟下圖一樣<br>
![alt text](https://github.com/Kenhchs/Image/blob/main/imgur7.png)<br>
- 填完後按下 Request Token , 就會出現一個要登入 Imgur 帳號的視窗<br>
![alt text](https://github.com/Kenhchs/Image/blob/main/imgur8.png)<br>
- 最終得到下圖 , 打開 ```auth.ini``` , ```imgur_Access_Token``` 填入下圖的 ```Access Token```<br>
![alt text](https://github.com/Kenhchs/Image/blob/main/imgur9.png)<br>

### 3. LINE Bot
- 登入[LINE Developers](https://developers.line.biz/console/)
- 找到 Providers 點選 ```Create```
![alt text](https://github.com/Kenhchs/Image/blob/main/linebot1.png)<br>
- 輸入 ```Provider name``` 按 ```Create```
![alt text](https://github.com/Kenhchs/Image/blob/main/linebot2.png)<br>
- 選擇 ```Create a Messaging API channel``` , 填寫資訊 , 按 ```Create``` , 接著按 ```OK``` , 最後按 ```同意```
![alt text](https://github.com/Kenhchs/Image/blob/main/linebot3.png)<br>
![alt text](https://github.com/Kenhchs/Image/blob/main/linebot4.png)<br>
![alt text](https://github.com/Kenhchs/Image/blob/main/linebot5.png)<br>
![alt text](https://github.com/Kenhchs/Image/blob/main/linebot6.png)<br>
- ```Basic settings``` 裡有 ```Channel secret``` , 打開 ```auth.ini``` ,  ```LINE_Channel_secret``` 填入看到的 ```Channel secret```
![alt text](https://github.com/Kenhchs/Image/blob/main/linebot7.png)<br>
- 按下 ```Messaging API``` 找到 ```Channel access token``` 按下 ```issue``` 後 , 你就會獲得 ```Channel access token``` , 打開 ```auth.ini``` ```LINE_Channel_access_token``` 填入看到的 ```Channel access token```
![alt text](https://github.com/Kenhchs/Image/blob/main/linebot8.png)<br>
![alt text](https://github.com/Kenhchs/Image/blob/main/linebot9.png)<br>
- 到 Basic settings 點選 ```LINE Official Account Manager``` , 點選 ```回應設定``` , 將基本設定與進階設定調整成下圖所示
![alt text](https://github.com/Kenhchs/Image/blob/main/linebot10.png)<br>
![alt text](https://github.com/Kenhchs/Image/blob/main/linebot11.png)<br>


### 4. LINE 圖文選單
- 開啟 Postman
- 步驟0 在執行下面 1~10 步驟前請先完成下圖步驟: ```GET``` 改成 ```POST``` , ```TYPE``` 改成 ```Bearer Token``` , ```Token``` 輸入 [LINE Bot](#3-line-bot) 的 ```Channel access token```<br>
![alt text](https://github.com/Kenhchs/Image/blob/main/Postman1.png)<br>
- 步驟1 Post 輸入 ```https://api.line.me/v2/bot/richmenu``` , 點 ```Headers``` 增加 ```Content-Type``` 和 ```application/json``` , 點 ```Body``` 然後點 ```raw``` 中間輸入  [步驟1 json檔](https://github.com/Kenhchs/Image/blob/main/Postman1.json) , 最後按```Send``` , 得到 ```richMenuId```
![alt text](https://github.com/Kenhchs/Image/blob/main/Postman2.png)<br>
![alt text](https://github.com/Kenhchs/Image/blob/main/Postman3.png)<br>
- 步驟2 Post 輸入 ```https://api-data.line.me/v2/bot/richmenu/{步驟1得到的 richMenuId}/content``` , 點 ```Headers``` 增加 ```Content-Type``` 和 ```image/png``` , 點 ```Body``` 然後點 ```binary```  圖片選擇 ```menu_1.JPG``` , 最後按 ```Send```
![alt text](https://github.com/Kenhchs/Image/blob/main/Postman5.png)<br>
![alt text](https://github.com/Kenhchs/Image/blob/main/Postman4.png)<br>
- 步驟3 同步驟1 , 但中間輸入變 [步驟3 json檔](https://github.com/Kenhchs/Image/blob/main/Postman2.json)
- 步驟4 同步驟2 , 但圖片改成 ```menu_2.JPG``` , ```richMenuId``` 改成步驟3得到的
- 步驟5 同步驟1 , 但中間輸入變 [步驟5 json檔](https://github.com/Kenhchs/Image/blob/main/Postman3.json)
- 步驟6 同步驟2 , 但圖片改成 ```menu_3.JPG``` , ```richMenuId``` 改成步驟5得到的
- 步驟7 Post 輸入 ```https://api.line.me/v2/bot/user/all/richmenu/{步驟1得到的 richMenuId}``` , 最後按 ```Send```
![alt text](https://github.com/Kenhchs/Image/blob/main/Postman6.png)<br>
- 步驟8 Post 輸入 ```https://api.line.me/v2/bot/richmenu/alias``` , 點 ```Headers``` 增加 ```Content-Type``` 和 ```application/json``` ,  點 ```Body``` 然後點 ```raw``` 中間輸入如下圖所示其中 ```richMenuAliasId``` 填 ```步驟1得到的 richMenuId``` , 最後按 ```Send```
![alt text](https://github.com/Kenhchs/Image/blob/main/Postman7.png)<br>
![alt text](https://github.com/Kenhchs/Image/blob/main/Postman8.png)<br>
- 步驟9 同 步驟8 , 其中 ```richMenuAliasId``` 改成 ```richmenu-alias-2``` , ```richMenuId``` 改成 ```步驟3得到的 richMenuId```
- 步驟10 同 步驟8 , 其中 ```richMenuAliasId``` 改成 ```richmenu-alias-3``` , ```richMenuId``` 改成 ```步驟5得到的 richMenuId```

### 5. 執行
- 到 ```darknet``` 執行 ```python3 app.py```<br>
![alt text](https://github.com/Kenhchs/Image/blob/main/execute1.png)<br>
- 開一個新的 terminal 打 ```ngrok http 5000```<br>
![alt text](https://github.com/Kenhchs/Image/blob/main/execute2.png)<br>
- 找到有 https 的複製起來<br>
![alt text](https://github.com/Kenhchs/Image/blob/main/execute3.png)<br>
- 到創建的 [LINE Bot](#3-line-bot)找到 ```Webhook URL``` , 輸入剛才複製的再加上 ```/callback```
![alt text](https://github.com/Kenhchs/Image/blob/main/execute4.png)<br>
- 按下 ```Verify```<br>
![alt text](https://github.com/Kenhchs/Image/blob/main/execute5.png)<br>
- 成功的話會顯示 ```Success```<br>
![alt text](https://github.com/Kenhchs/Image/blob/main/execute6.png)<br>
- 以上步驟做完即可開始使用 LINE Bot<br>
<img src="https://github.com/Kenhchs/Image/blob/main/execute7.png" alt="Cover" width="50%"/>

### 6. 提醒
- 以下 python 檔指的是此 repository 的 python 檔 , [要求](#要求)中的不用更改
- 由於此專案是在 Ubuntu 18.04 LTS 執行 , 如需更改成其他平台 , 請將 python 檔裡不屬於欲使用平台的指令更改掉 , 例如<br>
https://github.com/michael54856/AIOT_final/blob/9ca3ca8b767a1c71ad1ee8d2d470d853956aec5c/app.py#L226<br>
在 Windows 下需改成 ```darknet.exe detector test data/coin_counter_29.data cfg/coin_counter_29.cfg coin_counter_29_v2.weights -dont_show -ext_output < test.txt > result.txt```
- ```app.py``` 會用 subprocess 呼叫其他 python 檔 , 所以 python 檔所寫的路徑都是相對於 ```app.py``` 的路徑 , 請確保檔案的路徑正確,例如<br> 
https://github.com/michael54856/AIOT_final/blob/9ca3ca8b767a1c71ad1ee8d2d470d853956aec5c/stock.py#L283<br>
因為檔案結構如下 , 如果 ```app.py``` 想寫檔案 ```stock_predictions.txt``` 到 ```Stock``` 資料夾底下 , 相對路徑須設為 ```./Stock/stock_predictions.txt```
```
darknet
│      
└───Stock
│      │  stock.py
|
| app.py
|......
```
- 需安裝 ```pytorch``` 及 ```tensorflow``` , GPT2-chitchat(聊天機器人)會使用到 , 建議 gpu 不然會跑很久<br>
- [ngrok http 5000](#5-執行) 每次重新啟用都需修改 ```Webhook URL```<br>
- ```python3 app.py``` 需先於 [Verify Webhook URL](#5-執行) , 以免失敗<br>
- 如果動作評分出現 ```error == cudaSuccess (2 vs. 0) out of memory``` , 請將 ```--net_resolution``` 後面的 ```336x336``` 調低且兩個數字均須為16之倍數<br>
  - 相片請修改以下<br>
    https://github.com/michael54856/AIOT_final/blob/85120060d8d26c328253cb76536da7819f074592/ActionScoring_Image/ImageJudge.py#L175<br>
  - 影片請修改以下<br>
    https://github.com/michael54856/AIOT_final/blob/85120060d8d26c328253cb76536da7819f074592/ActionScoring_Video/videoJudger.py#L156-L158<br>

## 參考資料
- [darknet](https://github.com/AlexeyAB/darknet)
- [openpose](https://github.com/CMU-Perceptual-Computing-Lab/openpose)
- [GPT2-chitchat](https://github.com/yangjianxin1/GPT2-chitchat)
- [OpenCC](https://github.com/BYVoid/OpenCC)
- [Yolov4 Installation](https://medium.com/geekculture/yolov4-darknet-installation-and-usage-on-your-system-windows-linux-8dec2cea6e81)
- [Messaging API](https://developers.line.biz/en/docs/messaging-api/)
- [openpose Installation](https://www.youtube.com/watch?v=RSn8jVPopZo)
- [available-line-url-schemes](https://developers.line.biz/en/docs/line-login/using-line-url-scheme/#available-line-url-schemes)
