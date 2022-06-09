# AIOT_final
## 要求
- [darknet](https://github.com/AlexeyAB/darknet)
- [openpose](https://github.com/CMU-Perceptual-Computing-Lab/openpose)
- [GPT2-chitchat](https://github.com/yangjianxin1/GPT2-chitchat)
- [OpenCC](https://github.com/BYVoid/OpenCC)
- 註冊 [LINE Developers](https://developers.line.biz/zh-hant/) 和 [Imgur](https://imgur.com/)

## 使用說明

### 1. 檔案結構
- 下載 [pytorch_model.bin](https://github.com/Kenhchs/large-files/blob/main/GPT2/pytorch_model.bin?raw=true),  [config.json](https://github.com/Kenhchs/large-files/blob/main/GPT2/config.json?raw=true),  [coin_counter_29_v2.weights](https://github.com/Kenhchs/large-files/blob/main/yolov4/coin_counter_29_v2.weights?raw=true),  [mask_137.weights](https://github.com/Kenhchs/large-files/blob/main/yolov4/mask_137.weights?raw=true)

- 將 ```pytorch_model.bin``` 和 ```config.json``` 放到 ```GPT2-chitchat/model/```
- 將 ```chat.py``` 放到 ```GPT2-chitchat/```
- 將 ```GPT2-chitchat``` 放到 ```darknet/```
- 在 ```darknet/``` 創建 ```Stock``` 資料夾再把 ```stock.py``` 放到 ```Stock/```
- 將 ```coin_counter_29.cfg``` 和 ```mask_137.cfg``` 放到 ```darknet/cfg/```
- 將 ```coin_counter_29.data``` 和 ```mask_137.data``` 放到 ```darknet/data/``` 
- 將 ```app.py```, ```auth.ini```, ```coin_counter_29_v2.weights```, ```mask_137.weights```, ```openpose```, ```ActionScoring_Image``` 放到 ```darknet/```
- 檔案結構如下
```
darknet
│ README.md    
│
|
└───ActionScoring_Image
|      |......
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
- 註冊 ![Imgur App](https://api.imgur.com/oauth2/addclient)
- Authorization type 選擇第二個不用回傳 URL。
![alt text](https://github.com/Kenhchs/Image/blob/main/imgur1.png) 
- 再輸入完email後按下 ```submit``` ，就可以看到 App 的 ID、secret
![alt text](https://github.com/Kenhchs/Image/blob/main/imgur2.png)
- 註冊了App後，在個人設定(settings)的 Applications 中就會看到了
![alt text](https://github.com/Kenhchs/Image/blob/main/imgur3.png)
- 按下 ```Redirect``` 的 ```edit``` ，輸入 ```https://www.getpostman.com/oauth2/callback``` , 再按下 ```update``` 
![alt text](https://github.com/Kenhchs/Image/blob/main/imgur4.png)


## 參考資料
- [darknet](https://github.com/AlexeyAB/darknet)
- [openpose](https://github.com/CMU-Perceptual-Computing-Lab/openpose)
- [GPT2-chitchat](https://github.com/yangjianxin1/GPT2-chitchat)
- [OpenCC](https://github.com/BYVoid/OpenCC)
- [Yolov4 Installation](https://medium.com/geekculture/yolov4-darknet-installation-and-usage-on-your-system-windows-linux-8dec2cea6e81)
- [Messaging API](https://developers.line.biz/en/docs/messaging-api/)
