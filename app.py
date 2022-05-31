# -*- coding: utf-8 -*-
#載入LineBot所需要的套件
from flask import Flask, request, abort

from linebot import (
	LineBotApi, WebhookHandler
)
from linebot.exceptions import (
	InvalidSignatureError
)
from linebot.exceptions import LineBotApiError
from linebot.models import *
from PIL import Image
import os
import subprocess
import pyimgur
import configparser
import time

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('Onz8na9xK1lXRNjDl763G0VDZt4BjYG/SFf2ONv/dlQZlha4QrFX/oKGU1npOGCeG6iE0UjJF5J1jrn7ehJLNHfRXr1CFvjwCzUfVSf+TbBHBGwABRrpKil+hAe7edkb1LXEq/MUYCENxTIYmW8+uwdB04t89/1O/w1cDnyilFU=')
# Channel secret
handler = WebhookHandler('c1a54670b3069c72b414263e637cc189')
 # ID
#line_bot_api.push_message('Ubb5625b53855903f25ed79edc377757e', TextSendMessage(text='你可以開始了'))

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
	# get X-Line-Signature header value
	signature = request.headers['X-Line-Signature']

 
	# get request body as text
	body = request.get_data(as_text=True)
	app.logger.info("Request body: " + body)

	# handle webhook body
	try:
		handler.handle(body, signature)
	except InvalidSignatureError:
		abort(400)

	return 'OK'

# 處理 event
@handler.add(FollowEvent)
def handle_follow(event):
	pass

@handler.add(UnfollowEvent)
def handle_unfollow(event):
	pass

@handler.add(JoinEvent)
def handle_join(event):
	pass

@handler.add(LeaveEvent)
def handle_leave(event):
	pass

# two modes : mask and coin
mode = "mask"

# handle text message
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
	if event.message.text != "使用說明":
		if	event.message.text == "face":
			mode = "mask"
		elif event.message.text == "coin":
			mode = "coin"
		f = open("mode.txt", "w")
		f.write(mode)
		f.close()
		line_bot_api.reply_message(event.reply_token,TextSendMessage(text='請輸入圖片'))
		print(mode)

# handle image message
@handler.add(MessageEvent, message=ImageMessage)
def handle_image_message(event):
	# save image
	try:
		if not os.path.isdir('./1Linebot/images'):
			os.mkdir('./1Linebot/images')
		message_content = line_bot_api.get_message_content(event.message.id)
		file_path = './1Linebot/images/' + event.message.id + '.jpg'
		with open(file_path,'wb') as fd:
			for chunk in message_content.iter_content():
				fd.write(chunk)
	except:
		print("save image error")
		line_bot_api.reply_message(event.reply_token, TextSendMessage(text='系統錯誤'))
		return

	# write test.txt
	try:
		print("write test.txt")
		f = open("test.txt", "w")
		test_content = "/home/lys-90/darknet/1Linebot/images/" + event.message.id + '.jpg'
		f.write(test_content)
		f.close()
		print("write test.txt end")
	except:
		line_bot_api.reply_message(event.reply_token, TextSendMessage(text='系統錯誤'))
		print("write test.txt error")
		return

	# yolov4 detector
	print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
	myfile = open("mode.txt", "r")
	mode = myfile.readline()
	print(mode)
	myfile.close()

	if mode == "mask":
		try:
			filename = file_path
			#command = ("./darknet detector test build/darknet/x64/data/mask.data cfg/yolo-mask.cfg yolo-mask_final.weights -dont_show -ext_output < test.txt > result.txt")
			command = ("./darknet detector test data/mask_137.data cfg/mask_137.cfg mask_137.weights -dont_show -ext_output < test.txt > result.txt")
			start_time = round(time.time() * 1000)
			subprocess.call(command, shell=True)
			end_time = round(time.time() * 1000)
			print("testing time {}ms".format(end_time - start_time))
			if len(os.listdir("./1Linebot/images")) >= 1000:
				command = ("rm ./1Linebot/images/*")
				subprocess.call(command, shell=True)
		except:
			print("yolov4 detecting error")
			line_bot_api.reply_message(event.reply_token, TextSendMessage(text='系統錯誤'))
			return
	else:
		print("This is coin")
		try:
			filename = file_path
			command = ("./darknet detector test data/coin_counter_29.data cfg/coin_counter_29.cfg coin_counter_29_v2.weights -dont_show -ext_output < test.txt > result.txt")
			#command = ("./darknet detector test /home/lys-90/darknet/build/darknet/x64/data/coin_counter_29.data /home/lys-90/darknet/build/darknet/x64/data/coin_counter_29.cfg coin_counter_29.weights -dont_show -ext_output < test.txt > result.txt")
			subprocess.call(command, shell=True)
			if len(os.listdir("./1Linebot/images")) >= 1000:
				command = ("rm ./1Linebot/images/*")
				subprocess.call(command, shell=True)
		except:
			print("yolov4 detecting error")
			line_bot_api.reply_message(event.reply_token, TextSendMessage(text='系統錯誤'))
			return

	# read predictions
	if mode == "mask":
		try:
			with_mask = "with_mask"
			without_mask = "without_mask"
			mask_weared_incorrect = "mask_weared_incorrect"

			with_mask_count = 0
			without_mask_count = 0
			mask_weared_incorrect_count = 0

			with open('result.txt') as f:
				lines = f.readlines()
				for line in lines:
					if with_mask in line:
						with_mask_count += 1
					elif without_mask in line:
						without_mask_count += 1
					elif mask_weared_incorrect in line:
						mask_weared_incorrect_count += 1
			content = "正確配戴口罩\t   : {}人\n".format(with_mask_count) + "未正確配戴口罩\t: {}人\n".format(mask_weared_incorrect_count) + "沒有配戴口罩\t   : {}人".format(without_mask_count)
			message = TextSendMessage(text=content)
			print("正確配戴口罩\t: {}人".format(with_mask_count))
			print("未正確配戴口罩\t: {}人".format(mask_weared_incorrect_count))
			print("沒有配戴口罩\t: {}人".format(without_mask_count))
		except:
			print("read predictions error, mask")
			line_bot_api.reply_message(event.reply_token, TextSendMessage(text='系統錯誤'))
			return
	else:
		print("This is coin, read prediction")
		try:
			one_dollar = "NT$1:"
			five_dollar = "NT$5:"
			ten_dollar = "NT$10:"
			fifty_dollar = "NT$50:"

			one_dollar_count = 0
			five_dollar_count = 0
			ten_dollar_count = 0
			fifty_dollar_count = 0

			with open('result.txt') as f:
				lines = f.readlines()
				for line in lines:
					if one_dollar in line:
						one_dollar_count += 1
					elif five_dollar in line:
						five_dollar_count += 1
					elif ten_dollar in line:
						ten_dollar_count += 1
					elif fifty_dollar in line:
						fifty_dollar_count += 1
			content = "1元  : {}枚\n".format(one_dollar_count) + "5元  : {}枚\n".format(five_dollar_count) + "10元 : {}枚\n".format(ten_dollar_count) + "50元 : {}枚\n".format(fifty_dollar_count) + "總共 {}元".format(one_dollar_count + 5*five_dollar_count + 10*ten_dollar_count + 50*fifty_dollar_count)
			message = TextSendMessage(text=content)
			print("1元  : {}枚".format(one_dollar_count))
			print("5元  : {}枚".format(five_dollar_count))
			print("10元 : {}枚".format(ten_dollar_count))
			print("50元 : {}枚".format(fifty_dollar_count))
			print("總共 {}元".format(one_dollar_count + 5*five_dollar_count + 10*ten_dollar_count + 50*fifty_dollar_count))
		except:
			print("read predictions error, coin")
			line_bot_api.reply_message(event.reply_token, TextSendMessage(text='系統錯誤'))
			return

	# send prediction to imgur
	try:
		path = "predictions.jpg"
		print("1111111111111111")
		config = configparser.ConfigParser()
		print("2222222222222222")
		config.read('auth.ini')
		print("33333333333333")
		client_id = config.get('credentials', 'client_id')
		print(client_id)
		print("444444444444")
		client_secret = config.get('credentials', 'client_secret')
		print("55555555555")
		image = pyimgur.Imgur(client_id)
		uploaded_image = image.upload_image(path, title="test")
		print("666666666666")
		print(uploaded_image.link)
		image_message = ImageSendMessage(original_content_url=uploaded_image.link, preview_image_url=uploaded_image.link)
		print("7777777777777")
	except:
		print("send prediction to imgur error")
		line_bot_api.reply_message(event.reply_token, TextSendMessage(text='系統錯誤'))
		return

	# send back to user
	try:	
		line_bot_api.reply_message(event.reply_token, [image_message, message])
	except:
		print("send back to user error")
		line_bot_api.reply_message(event.reply_token, TextSendMessage(text='系統錯誤'))
		return

# main function
import os
if __name__ == "__main__":
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port)
