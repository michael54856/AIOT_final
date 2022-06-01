# AIOT_final
## Requirements
- [darknet](https://github.com/AlexeyAB/darknet)
- [openpose](https://github.com/CMU-Perceptual-Computing-Lab/openpose)
- [GPT2-chitchat](https://github.com/yangjianxin1/GPT2-chitchat)

## How to use
- Download [pytorch_model.bin](https://github.com/Kenhchs/large-files/blob/main/GPT2/pytorch_model.bin?raw=true),  [config.json](https://github.com/Kenhchs/large-files/blob/main/GPT2/config.json?raw=true),  [coin_counter_29_v2.weights](https://github.com/Kenhchs/large-files/blob/main/yolov4/coin_counter_29_v2.weights?raw=true),  [mask_137.weights](https://github.com/Kenhchs/large-files/blob/main/yolov4/mask_137.weights?raw=true)
- Put ```pytorch_model.bin``` and ```config.json``` in ```GPT2-chitchat/model/```
- Put ```chat.py``` in ```GPT2-chitchat/```
- Put ```GPT2-chitchat``` in the ```darknet/```
- Create a ```Stock``` folder in ```darknet/``` and put ```stock.py``` in ```Stock/```
- Put ```coin_counter_29.cfg``` and ```mask_137.cfg``` in ```darknet/cfg/```
- Put ```coin_counter_29.data``` and ```mask_137.data``` in ```darknet/data/``` 
- Put ```app.py```, ```auth.ini```, ```coin_counter_29_v2.weights```, and ```mask_137.weights``` in ```darknet/```
- File structure is as follows
```
darknet
│ README.md    
│
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

## Reference
- [darknet](https://github.com/AlexeyAB/darknet)
- [openpose](https://github.com/CMU-Perceptual-Computing-Lab/openpose)
- [GPT2-chitchat](https://github.com/yangjianxin1/GPT2-chitchat)
- [installation](https://medium.com/geekculture/yolov4-darknet-installation-and-usage-on-your-system-windows-linux-8dec2cea6e81)
- [Messaging API](https://developers.line.biz/en/docs/messaging-api/)
