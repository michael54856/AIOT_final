# 智慧物聯網綜合系統-Peter的一天
## 目錄
- [簡介](#簡介)
- [動機與目的](#動機與目的)
  - [聊天機器人-動機](#1-聊天機器人-動機)
  - [股票預測-動機](#2-股票預測-動機)
  - [口罩辨識-動機](#3-口罩辨識-動機)
  - [零錢辨識-動機](#4-零錢辨識-動機)
  - [動作評分-動機](#5-動作評分-動機)
- [相似研究](#相似研究)
  - [聊天機器人-相似研究](#1-聊天機器人-相似研究)
  - [股票預測-相似研究](#2-股票預測-相似研究)
  - [口罩辨識-相似研究](#3-口罩辨識-相似研究)
  - [零錢辨識-相似研究](#4-零錢辨識-相似研究)
  - [動作評分-相似研究](#5-動作評分-相似研究)
  - [論文參考](#論文參考)
- [安裝說明](#安裝說明)
  - [要求](#要求)
  - [使用說明](#使用說明)
    - [1. 檔案結構](#1-檔案結構)
    - [2. Imgur](#2-imgur)
    - [3. LINE Bot](#3-line-bot)
    - [4. LINE 圖文選單](#4-line-圖文選單)
    - [5. 執行](#5-執行)
  - [提醒](#提醒)
- [使用說明與結果](#使用說明與結果)
  - [Line介面](#1-Line介面)
  - [聊天機器人-結果](#2-聊天機器人-結果)
  - [股票預測-結果](#3-股票預測-結果)
  - [口罩辨識-結果](#4-口罩辨識-結果)
  - [零錢辨識-結果](#5-零錢辨識-結果)
  - [動作評分_相片-結果](#6-動作評分_相片-結果)
  - [動作評分_影片-結果](#7-動作評分_影片-結果)
- [參考資料](#參考資料)

## 簡介
Peter是一個非常忙碌的人，我們想利用A.I的能力以及Line這個方便的介面，為Peter這樣忙碌的人提供生活中的便利性，建立一個綜合的智慧物聯網系統。
<br>我們的系統包含了以下幾個功能：
- 聊天機器人
- 股票預測
- 口罩辨識
- 零錢辨識
- 動作評分(相片)
- 動作評分(影片)
<img src="https://raw.githubusercontent.com/michael54856/Images/main/AIOT_final/xmind.png">

## 動機與目的

### 1. 聊天機器人-動機
* 經統計發現，通訊軟體的使用率高達9成。
  <img src="https://raw.githubusercontent.com/michael54856/Images/main/AIOT_final/chatStats1.png">
* 現在的社會步調快速，許多人都專注於工作、學業，當想要與別人進行聊天的時候，往往沒辦法獲得即時的回覆，因此我們想建立一個智慧聊天機器人，除了能夠讓人毫無顧慮的進行聊天以外，當猶豫不決時，也可以讓機器人幫忙做出決定。

### 2. 股票預測-動機
* 依證券交易所及櫃檯買賣中心統計，今（110）年 7 月我國上市櫃股票平均每日成交金額 6,523 億元，較去（109）年同月增 1.3 倍，已連續 22 個月正成長；累計 1-7 月上市櫃股票 總成交金額為 70.0 兆元，較去年同期增 1.3 倍，平均每日成交 5,070 億元，亦增 1.4 倍。
  <img src="https://raw.githubusercontent.com/michael54856/Images/main/AIOT_final/stocks1.png">
* 近年來股市熱絡，許多投資人經驗並不是那麼豐富，因此我們想要結合數據分析以及深度學習的技術，建立一個股票預測系統。

### 3. 口罩辨識-動機
* 中央流行疫情指揮中心公布國內新增53,707例COVID-19確定病例，分別為53,643例本土個案及64例境外移入，另確診個案中新增181例死亡，可見疫情對生活的影響。
  <img src="https://raw.githubusercontent.com/michael54856/Images/main/AIOT_final/mask1.png">
* 近年來Covid-19疫情嚴重，口罩已成為我們日常生活的必需品，我們想利用A.I的技術幫助我們進行配戴口罩的檢測，可以一次辨識多人是否正確配戴口罩。

### 4. 零錢辨識-動機
* 在日常生活中找零問題往往困擾著我們，忙碌中難免會算錯零錢數量，因此我們想要透過深度學習的技術來幫助計算，提供公正性與便利性。

### 5. 動作評分-動機
* 在體育署多年來推廣全民運動政策下，民眾已逐漸養成運動習慣。雖然去年（109年）開始的疫情一度影響民眾的運動行為，但也使民眾更關注身體健康並恢復運動習慣。110年規律運動人口達33.9%，較109年（33.0%）增加0.9%。民眾平均每週運動次數為3.83次，較109年（3.72次）增加0.11次；運動強度為44.4%，較109年（42.8%）提高1.6%。
* 受到疫情影響，許多學校運動場地管制進入，民眾運動地點以公園的比例最高（35.4%），其次是人行道/道路（26.2%），學校運動場地（25.8%）。疫情也改變了部分民眾的運動模式，在家運動的比例（15.3%）較109年（9.0%）大幅增加6.3%。
* 隨著人們健康意識的抬頭，運動風氣越加盛行，相關運動產業也蓬勃發展，其中將人工智慧運用在運動領域中，能有效的幫助人們進行運動訓練，在沒有教練的情況下也能夠獲得運動回饋，進行自我姿勢矯正。

## 相似研究

### 1. 聊天機器人-相似研究
* [1]這個研究是利用Google Dialogflow 和 BERT 預訓練模型進行結合，當用戶與 Dialogflow 聊天機器人互動時，它會匹配聊天意圖並將請求發送到 BERT 模型。最後BERT 模型為聊天機器人提供答案並回覆用戶。 QAM 可針對大型數據集的問題向用戶提供準確的響應。
* [2]這個研究在文本的生成階段，使用了Temperature、Top-k Sampling和Nucleus Sampling等技術，這是一種簡單但有效的方法，可以充分利用神經網路的生成。通過從概率分佈的動態核中採樣文本，並允許多樣性，同時有效地截斷分佈不太可靠的尾部，生成的文本更好地展示了人類文本的質量，在不犧牲流暢性和連貫性的情況下產生增強的多樣性。
* 而我們將基於[2]的延伸，GPT2-chitchat，來執行生成中文的聊天機器人。

### 2. 股票預測-相似研究
* [6]此篇論文基於LSTM模型去預測股價，通過分析股票市場的歷史信息發現時間序列的作用，並通過LSTM神經網絡模型的選擇性記憶高級深度學習功能深入挖掘其內在規律，從而實現對股票的預測以及價格趨勢。
* 本次的專案將會利用兩層的LSTM來建立模型，讓模型能夠獲得更佳的效能。

### 3. 口罩辨識-相似研究
* [7]這篇論文使用YOLOv4 架構，該系統被訓練以捕捉圖像和實時流中的面部面具特徵。在訓練了 4000 個 epoch 後，在實時場景中取得了顯著的效果，平均 FPS 為 49.5，mAP 為 98%。
* 我們也將利用YOLOv4進行預測，但是除了有配戴口罩以及無配戴口罩之外，我們將多預測一種非正確配戴口罩，例如鼻子露出來。

### 4. 零錢辨識-相似研究
* [8]這篇論文採用Hough Detection Method檢測圖像中的硬幣區域，並使用半徑比、顏色特徵和相對位置約束來消除噪聲圓。並利用多層卷積神經網絡對proposal進行分類，得到最終的識別結果。
* 為了簡化辨識，本次的研究將直接利用YOLOv4來進行。

### 5. 動作評分-相似研究
* [3]與[4]這兩項研究都是利用在身上的穿戴式裝置建立感測器網路，並利用這些資訊與範本動作進行比對。
* 我們可看出透過穿戴式裝置蒐集運動資料並加以進行分析的應用已非常成熟。
* 但是一般人難以擁有這些裝置，因此我們想要提供一個使用門檻低，且成本低廉的分析方式。
* [5]是利用AlphaPose先取出動作人體的關節位置，經過數據處理後，再使用深度學習的模型將資料轉換為評測分數，這項研究類似於本次的計畫，但是將預測分數的行為交由人工智慧進行，反而會缺乏評測的彈性，我們並不知道人工智慧內部是如何計算分數，只能夠獲得結果。
* 本次的計畫中，我們將設計一套演算法能夠有邏輯的計算節點訊息，並提供評測的彈性給使用者，我們可以讓使用者設定各部位的權重進行評測，避免出現人工智慧將頭部或是其他較不重要的資訊設為重點等尷尬情形。
* 並且我們可以回傳該注意哪些部位來改善動作。


### 論文參考
* [1]N. Kanodia, K. Ahmed and Y. Miao, "Question Answering Model Based Conversational Chatbot using BERT Model and Google Dialogflow," 2021 31st International Telecommunication Networks and Applications Conference (ITNAC), 2021, pp. 19-22, doi: 10.1109/ITNAC53136.2021.9652153.
* [2] Holtzman, A., Buys, J., Du, L., Forbes, M., & Choi, Y. (2019). The curious case of neural text degeneration. arXiv preprint arXiv:1904.09751.
* [3] Ghasemzadeh, H., & Jafari, R. (2010, March). Body sensor networks for baseball swing training: Coordination analysis of human movements using motion transcripts. In 2010 8th IEEE International Conference on Pervasive Computing and Communications Workshops (PERCOM Workshops) (pp. 792-795). IEEE. 
* [4] Kim, Y. J., Kim, K. D., Kim, S. H., Lee, S., & Lee, H. S. (2017). Golf swing analysis system with a dual band and motion analysis algorithm. IEEE Transactions on Consumer Electronics, 63(3), 309-317
* [5] Liu, J. J., Newman, J., & Lee, D. J. (2020, October). Body Motion Analysis for Golf Swing Evaluation. In International Symposium on Visual Computing (pp. 566-577). Springer, Cham.
* [6] D. Wei, "Prediction of Stock Price Based on LSTM Neural Network," 2019 International Conference on Artificial Intelligence and Advanced Manufacturing (AIAM), 2019, pp. 544-547, doi: 10.1109/AIAM48774.2019.00113.
* [7] R. R. Mahurkar and N. G. Gadge, "Real-time Covid-19 Face Mask Detection with YOLOv4," 2021 Second International Conference on Electronics and Sustainable Communication Systems (ICESC), 2021, pp. 1250-1255, doi: 10.1109/ICESC51422.2021.9533008.
* [8] ZiHe Qiu, Ping Shi, Da Pan and DiXiu Zhong, "Coin detection and recognition in the natural scene," 2016 IEEE Advanced Information Management, Communicates, Electronic and Automation Control Conference (IMCEC), 2016, pp. 653-657, doi: 10.1109/IMCEC.2016.7867290.


## 安裝說明

## 要求
- [darknet](https://github.com/AlexeyAB/darknet)
- [openpose](https://github.com/CMU-Perceptual-Computing-Lab/openpose)
- [GPT2-chitchat](https://github.com/yangjianxin1/GPT2-chitchat)
- [OpenCC](https://github.com/BYVoid/OpenCC)
- 註冊 [LINE Developers](https://developers.line.biz/zh-hant/) 和 [Imgur](https://imgur.com/)


### 1. 檔案結構
- 下載 [pytorch_model.bin](https://github.com/Kenhchs/large-files/blob/main/GPT2/pytorch_model.bin?raw=true) , [config.json](https://github.com/Kenhchs/large-files/blob/main/GPT2/config.json?raw=true) , [coin_counter_29_v2.weights](https://github.com/Kenhchs/large-files/blob/main/yolov4/coin_counter_29_v2.weights?raw=true) ,  [mask_137.weights](https://github.com/Kenhchs/large-files/blob/main/yolov4/mask_137.weights?raw=true)

- 在 ```ActionScoring_Image``` 裡創建3個資料夾名稱為 ```Image``` , ```outputJson``` , ```RenderImage```
- 在 ```ActionScoring_Video``` 裡創建3個資料夾名稱為 ```CompareJson``` , ```SampleJson``` , ```VideoSource```
- 將 ```pytorch_model.bin``` 和 ```config.json``` 放到 ```GPT2-chitchat/model/```
- 將 ```chat.py``` 放到 ```GPT2-chitchat/```
- 在 ```darknet/``` 創建 ```Stock``` 資料夾再把 ```stock.py``` 放到 ```Stock/```
- 將 ```coin_counter_29.cfg``` 和 ```mask_137.cfg``` 放到 ```darknet/cfg/```
- 將 ```coin_counter_29.data``` 和 ```mask_137.data``` 放到 ```darknet/data/``` 
- 將 ```app.py``` , ```auth.ini``` , ```coin_counter_29_v2.weights``` , ```mask_137.weights``` , ```openpose``` , ```GPT2-chitchat``` , ```ActionScoring_Image``` , ```ActionScoring_Video``` 放到 ```darknet/```
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
| openpose
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
- 下載 [Postman](https://www.postman.com/downloads/)(網頁版有些地方不能修改)<br>
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
- 到 ```Messaging API``` 找到 ```QR code``` 加為 LINE 好友<br>
![alt text](https://github.com/Kenhchs/Image/blob/main/linebot12.png)<br>


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
- 到創建的 [LINE Bot](#3-line-bot) 找到 ```Webhook URL``` , 輸入剛才複製的再加上 ```/callback```
![alt text](https://github.com/Kenhchs/Image/blob/main/execute4.png)<br>
- 按下 ```Verify```<br>
![alt text](https://github.com/Kenhchs/Image/blob/main/execute5.png)<br>
- 成功的話會顯示 ```Success```<br>
![alt text](https://github.com/Kenhchs/Image/blob/main/execute6.png)<br>
- 以上步驟做完即可開始使用 LINE Bot<br>
<img src="https://github.com/Kenhchs/Image/blob/main/execute8.png" alt="Cover" width="50%"/>

## 提醒
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
- ``` ngrok http 5000``` 和 ```python3 app.py``` 需先於 [Verify Webhook URL](#5-執行) , 以免失敗<br>
- 如果動作評分出現 ```error == cudaSuccess (2 vs. 0) out of memory``` , 請將 ```--net_resolution``` 後面的 ```336x336``` 調低且兩個數字均須為16之倍數<br>
  - 相片請修改以下<br>
    https://github.com/michael54856/AIOT_final/blob/85120060d8d26c328253cb76536da7819f074592/ActionScoring_Image/ImageJudge.py#L175<br>
  - 影片請修改以下<br>
    https://github.com/michael54856/AIOT_final/blob/85120060d8d26c328253cb76536da7819f074592/ActionScoring_Video/videoJudger.py#L156-L158<br>
- 填寫 ```auth.ini``` 時不能有空格 , 例如你的 ```imgur access token``` 是 ```12345678910``` , 要填成 ```imgur_Access_Token=12345678910``` , 而不可以填成 ```imgur_Access_Token = 12345678910```



## 使用說明與結果

### 1. Line介面
* 我們的LineBot介面總共有三頁
* 第一頁有
  - 使用說明 : 按下時會跳出說明文件告知使用者該如何操作
  - 股票預測 : 跳到股票預測功能，會詢問使用者要預測的上市公司，以及要預測的時間長度(短期、中期、長期)
  <img src="https://raw.githubusercontent.com/michael54856/Images/main/AIOT_final/linePage1.png">
* 第二頁有
  - 零錢辨識 : 按下時後要求使用者上傳零錢的圖片
  - 口罩辨識 : 按下時後要求使用者上傳人物的圖片
  - 動作評分_相片 : 按下時後要求使用者上傳範本動作的相片，再上傳比對動作的相片
  - 動作評分_影片 : 按下時後要求使用者上傳範本動作的影片，再上傳比對動作的影片
  <img src="https://raw.githubusercontent.com/michael54856/Images/main/AIOT_final/linePage2.png">
* 第三頁有
  - 功能重置 : 按下時可清除執行途中的功能
  - 打開相機 : 按下時後可以直接打開相機進行拍攝
  - 上傳檔案 : 讓使用者可從媒體庫上傳檔案
  <img src="https://raw.githubusercontent.com/michael54856/Images/main/AIOT_final/linePage3.png">
### 2. 聊天機器人-結果
* 我們可以直接在Line上面傳送訊息，我們會將訊息進行計算，並回復使用者
  <br>
  <img src="https://raw.githubusercontent.com/michael54856/Images/main/AIOT_final/chatResult.png">
### 3. 股票預測-結果
* 首先我們要選擇想要預測哪一間公司
  <br>
  <img src="https://raw.githubusercontent.com/michael54856/Images/main/AIOT_final/stockResult1.png">
* 之後可以選擇短期(7天)、中期(30天)、長期(180天)，會返回預測的圖表以及將來的收盤價格
  <br>
  <img src="https://raw.githubusercontent.com/michael54856/Images/main/AIOT_final/stockResult2.png">
* 對Intel進行長期預測
  <br>
  <img src="https://raw.githubusercontent.com/michael54856/Images/main/AIOT_final/stockResult3.png">
* 對Google進行中期預測
  <br>
  <img src="https://raw.githubusercontent.com/michael54856/Images/main/AIOT_final/stockResult4.png">
* 對Microsoft進行短期預測
  <br>
  <img src="https://raw.githubusercontent.com/michael54856/Images/main/AIOT_final/stockResult5.png">
### 4. 口罩辨識-結果
* 當我們選擇進行口罩辨識之後，系統會要求上傳圖片
  <img src="https://raw.githubusercontent.com/michael54856/Images/main/AIOT_final/maskResult1.png">
* 系統框出人臉，並計算出```正確配戴口罩```、```未正確配戴口罩```、```沒有配戴口罩```的人數
  <img src="https://raw.githubusercontent.com/michael54856/Images/main/AIOT_final/maskResult2.png">
### 5. 零錢辨識-結果
* 當我們選擇進行零錢辨識之後，系統會要求上傳圖片，系統會計算```1元```、```5元```、```10元```、```50元```分別有幾個，並算出總和
  <br>
  <img src="https://raw.githubusercontent.com/michael54856/Images/main/AIOT_final/coinResult.png">
### 6. 動作評分_相片-結果
### 7. 動作評分_影片-結果

## 參考資料
- [darknet](https://github.com/AlexeyAB/darknet)
- [openpose](https://github.com/CMU-Perceptual-Computing-Lab/openpose)
- [GPT2-chitchat](https://github.com/yangjianxin1/GPT2-chitchat)
- [OpenCC](https://github.com/BYVoid/OpenCC)
- [Yolov4 Installation](https://medium.com/geekculture/yolov4-darknet-installation-and-usage-on-your-system-windows-linux-8dec2cea6e81)
- [Messaging API](https://developers.line.biz/en/docs/messaging-api/)
- [openpose Installation](https://www.youtube.com/watch?v=RSn8jVPopZo)
- [available-line-url-schemes](https://developers.line.biz/en/docs/line-login/using-line-url-scheme/#available-line-url-schemes)
- [imgur API (Part 1/3)](https://www.youtube.com/watch?v=OiDQu-0-DIA)
- [imgur API (Part 2/3)](https://www.youtube.com/watch?v=kDcn_Tn-ti8)
- [imgur API (Part 3/3)](https://www.youtube.com/watch?v=MyCr8kPT3OI&t=5s)
- [Imgur API：upload, load 上傳、讀取 心得筆記](https://medium.com/front-end-augustus-study-notes/imgur-api-3a41f2848bb8)
- [Using rich menus](https://developers.line.biz/en/docs/messaging-api/using-rich-menus/)
