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
import opencc
from imgur import upload_image, upload_vedio

app = Flask(__name__)

config = configparser.ConfigParser()
config.read('auth.ini')
LINE_Channel_access_token = config.get('credentials', 'LINE_Channel_access_token')
print(LINE_Channel_access_token)
LINE_Channel_secret = config.get('credentials', 'LINE_Channel_secret')
print(LINE_Channel_secret)

# Channel Access Token
line_bot_api = LineBotApi(LINE_Channel_access_token)
# Channel secret
handler = WebhookHandler(LINE_Channel_secret)

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

# 6 modes : chat bot, stock prediction, coin counter, mask detection, action scoring(image), action scoring(video)
input_counter = 0 # count for action_scoring_image, action_scoring_video, stock_prediction
chat_bot = "功能重置"
stock_prediction = "股票預測"
coin_counter = "零錢辨識"
mask_detection = "口罩辨識"
action_scoring_image = "動作評分-照片"
action_scoring_video = "動作評分-影片"
mode = chat_bot
Time_Interval = "長期"
company = "GOOG"

# handle text message
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
	global mode
	global input_counter
	global Time_Interval
	global company
	try:
		if event.message.text == chat_bot:
			mode = chat_bot
			input_counter = 0
			line_bot_api.reply_message(event.reply_token,TextSendMessage(text='切換為聊天機器人'))

		elif event.message.text == stock_prediction:
			mode = stock_prediction
			flex_message = TextSendMessage(text='請選擇要想要的公司',
                                quick_reply=QuickReply(items=[
                                    QuickReplyButton(action=MessageAction(label="Google", text="GOOG")),
                                    QuickReplyButton(action=MessageAction(label="Microsoft", text="MSFT")),
                                    QuickReplyButton(action=MessageAction(label="Amazon", text="AMZN")),
									QuickReplyButton(action=MessageAction(label="Intel", text="INTC")),
									QuickReplyButton(action=MessageAction(label="NVIDIA", text="NVDA"))
                                ]))
			line_bot_api.reply_message(event.reply_token, [TextSendMessage(text='切換股票預測'), flex_message])
			input_counter = 1
		
		elif event.message.text == coin_counter:
			mode = coin_counter
			line_bot_api.reply_message(event.reply_token,TextSendMessage(text='切換為零錢辨識'))
		
		elif event.message.text == mask_detection:
			mode = mask_detection
			line_bot_api.reply_message(event.reply_token,TextSendMessage(text='切換口罩辨識'))
		
		elif event.message.text == action_scoring_image:
			mode = action_scoring_image
			input_counter = 0
			line_bot_api.reply_message(event.reply_token,TextSendMessage(text='切換為動作評分-照片\n請上傳範本照片'))

		elif event.message.text == action_scoring_video:
			mode = action_scoring_video
			input_counter = 0
			line_bot_api.reply_message(event.reply_token,TextSendMessage(text='切換為動作評分-影片\n請上傳範本影片'))
		
		elif event.message.text == "使用說明":
			mode = chat_bot
			line_bot_api.reply_message(event.reply_token,TextSendMessage(text='歡迎使用物聯網綜合系統，本專案有以下幾個功能\n\n1.聊天機器人\n2.股票預測\n3.零錢辨識\n4.口罩辨識\n5.動作評分-相片\n6.動作評分-影片\n\n聊天機器人:您只需要在此聊天視窗中正常聊天，機器人即會回覆您\n\n股票預測:點選股票預測的按鈕後，請打入要預測的公司名稱，並且選擇要預測的長度，之後會給予預測結果\n\n零錢辨識:點選零錢辨識得按鈕後，系統會要求您上傳圖片，之後會回覆您各個零錢分別有多少，以及金額的總和\n\n口罩辨識:點選口罩辨識得按鈕後，系統會要求您上傳圖片，之後會回覆您正確配戴口罩，未配戴口罩，以及未正確配戴口罩的人各有多少\n\n動作辨識-相片:點選動作辨識-相片的按鈕後，系統會要求上傳範本動作以及比對的動作，之後會回傳動作的相似程度(1~5分)，以及需要改進的人體位置\n\n動作辨識-影片:點選動作辨識-影片的按鈕後，系統會要求上傳範本動作以及比對的動作，之後會回傳動作的相似程度(1~5分)，以及渲染後的骨架影片'))

		elif (input_counter == 1 or input_counter == 2) and mode == stock_prediction:
			if input_counter == 1:
				company = event.message.text
				input_counter = 2
				flex_message = TextSendMessage(text='請選擇想要預測的時間長度',
									quick_reply=QuickReply(items=[
										QuickReplyButton(action=MessageAction(label="長期", text="長期")),
										QuickReplyButton(action=MessageAction(label="中期", text="中期")),
										QuickReplyButton(action=MessageAction(label="短期", text="短期"))
									]))
				line_bot_api.reply_message(event.reply_token, [flex_message])
			
			elif input_counter == 2:
				input_counter = 0
				Time_Interval = event.message.text
				fw = open("stock_information.txt", "w")
				fw.write("{}\n{}".format(company, Time_Interval))
				fw.close()

				print(Time_Interval)
				print(company)
				command = ("python3 ./Stock/stock.py")
				print("stock.py running")
				subprocess.call(command, shell=True)

				# check if the stock.py execute successfully
				fr = open("./Stock/success_or_error.txt", 'r')
				temp = fr.read()
				if temp == "1":
					line_bot_api.reply_message(event.reply_token,[TextSendMessage(text="公司名字或時間長度或其他錯誤")])

				elif temp == "0":
					uploaded_image = upload_image("./Stock/Stock_prediction.png")
					image_message = ImageSendMessage(original_content_url=uploaded_image.link, preview_image_url=uploaded_image.link)
					return_text = ""
					fr = open("./Stock/stock_predictions.txt", 'r')
					for line in fr:
						return_text += line
						print(line)
					fr.close()
					line_bot_api.reply_message(event.reply_token,[image_message, TextSendMessage(text=return_text)])
				
				else:
					line_bot_api.reply_message(event.reply_token,TextSendMessage(text='系統錯誤(text handler)'))

		else:
			if mode == chat_bot:
				command = ("python3 ./GPT2-chitchat/chat.py --model_path ./GPT2-chitchat/model --device 0")
				print("chat_bot running")
				subprocess.call(command, shell=True)
				fr = open('./GPT2-chitchat//bot_content.txt', 'r')
				text = fr.read()
				fr.close()
				converter = opencc.OpenCC('s2t')
				line_bot_api.reply_message(event.reply_token,TextSendMessage(text=converter.convert(text)))

			else:
				line_bot_api.reply_message(event.reply_token,TextSendMessage(text='目前模式為' + mode + ", 如需聊天機器人請點選功能重置"))
	except:
		line_bot_api.reply_message(event.reply_token,TextSendMessage(text='系統錯誤(text handler)'))
# handle image message
@handler.add(MessageEvent, message=ImageMessage)
def handle_image_message(event):
	global mode
	global input_counter
	try:
		if mode == chat_bot:
			line_bot_api.reply_message(event.reply_token,TextSendMessage(text='目前模式為聊天機器人不支援照片功能'))

		elif mode == stock_prediction or mode == action_scoring_video:
			line_bot_api.reply_message(event.reply_token,TextSendMessage(text='目前模式為' + mode + "不支援照片功能"))
		
		elif mode == coin_counter or mode == mask_detection:
			if not os.path.isdir('./Mask_Coin_image'):
				os.mkdir('./Mask_Coin_image')
			message_content = line_bot_api.get_message_content(event.message.id)
			file_path = './Mask_Coin_image/yolov4_to_be_detected.jpg'
			# save image
			with open(file_path,'wb') as fd:
				for chunk in message_content.iter_content():
					fd.write(chunk)
			# write test.txt
			print("write test.txt")
			f = open("test.txt", "w")
			test_content = "./Mask_Coin_image/yolov4_to_be_detected.jpg"
			f.write(test_content)
			f.close()
			print("write test.txt end")
			# Coin counter
			if mode == coin_counter:
				print("This is coin")
				command = ("./darknet detector test data/coin_counter_29.data cfg/coin_counter_29.cfg coin_counter_29_v2.weights -dont_show -ext_output < test.txt > result.txt")
				subprocess.call(command, shell=True)
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
			# Mask detection
			else:
				print("This is mask")
				command = ("./darknet detector test data/mask_137.data cfg/mask_137.cfg mask_137.weights -dont_show -ext_output < test.txt > result.txt")
				subprocess.call(command, shell=True)
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

			# Send prediction to imgur
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
			
			# send back to user
			line_bot_api.reply_message(event.reply_token, [image_message, message])
		
		elif mode == action_scoring_image:
			if input_counter == 0:
				file_path = './ActionScoring_Image/Image/Sample.jpg'
				input_counter = 1
				line_bot_api.reply_message(event.reply_token,TextSendMessage(text='請上傳比對照片'))


			elif input_counter == 1:
				input_counter = 2
				file_path = './ActionScoring_Image/Image/Compare.jpg'
			
			else:
				line_bot_api.reply_message(event.reply_token,TextSendMessage(text='系統錯誤(image handler)'))
			
			# save image
			message_content = line_bot_api.get_message_content(event.message.id)
			with open(file_path,'wb') as fd:
				for chunk in message_content.iter_content():
					fd.write(chunk)
			if input_counter == 2:
				command = ("python3 ./ActionScoring_Image/ImageJudge.py")
				subprocess.call(command, shell=True)
				mode = chat_bot
				input_counter = 0

				# upload image
				image_list = []

				uploaded_image = upload_image("./ActionScoring_Image/RenderImage/Sample_rendered.png")
				image_message = ImageSendMessage(original_content_url=uploaded_image.link, preview_image_url=uploaded_image.link)
				image_list.append(image_message)

				uploaded_image = upload_image("./ActionScoring_Image/RenderImage/Compare_rendered.png")
				image_message = ImageSendMessage(original_content_url=uploaded_image.link, preview_image_url=uploaded_image.link)
				image_list.append(image_message)

				uploaded_image = upload_image("./ActionScoring_Image/TargetVector.png")
				image_message = ImageSendMessage(original_content_url=uploaded_image.link, preview_image_url=uploaded_image.link)
				image_list.append(image_message)

				uploaded_image = upload_image("./ActionScoring_Image/compareVector.png")
				image_message = ImageSendMessage(original_content_url=uploaded_image.link, preview_image_url=uploaded_image.link)
				image_list.append(image_message)

				fr = open('./ActionScoring_Image/FinalScore.txt', 'r')
				grade_image = fr.read()
				fr.close()
				text_message = TextSendMessage(text=grade_image + "分")

				line_bot_api.reply_message(event.reply_token, [image_list[0], image_list[1], image_list[2], image_list[3], text_message])
				print("ActionScoring-image finished")


		else:
			line_bot_api.reply_message(event.reply_token,TextSendMessage(text='系統錯誤(image handler)'))
			input_counter = 0
			mode = chat_bot
	
	except:
		line_bot_api.reply_message(event.reply_token,TextSendMessage(text='系統錯誤(image handler)'))
		input_counter = 0
		mode = chat_bot

# handle video message
@handler.add(MessageEvent, message=VideoMessage)
def handle_video_message(event):
	global mode
	global input_counter
	message_content = line_bot_api.get_message_content(event.message.id)
	
	if mode == chat_bot or mode == stock_prediction or mode == coin_counter or mode == mask_detection or mode == action_scoring_image:
		line_bot_api.reply_message(event.reply_token,TextSendMessage(text='目前模式為' + mode + "不支援影片片功能"))
	
	elif mode == action_scoring_video:
		# save video
		if input_counter == 0:
			input_counter = 1
			file_path = './ActionScoring_Video/VideoSource/Sample.mp4'
			line_bot_api.reply_message(event.reply_token,TextSendMessage(text='請上傳比對影片'))

		elif input_counter == 1:
			input_counter = 2
			file_path = './ActionScoring_Video/VideoSource/Compare.mp4'

		with open(file_path,'wb') as fd:
			for chunk in message_content.iter_content():
				fd.write(chunk)

		if input_counter == 2:
			command = ("python3 ./ActionScoring_Video/videoJudger.py")
			subprocess.call(command, shell=True)
			input_counter = 0
			mode = chat_bot
			video_list = []
			
			command = ("ffmpeg -i -y ./ActionScoring_Video/SampleRenderedOutput.avi ./ActionScoring_Video/SampleRenderedOutput.mp4")
			subprocess.call(command, shell=True)
			uploaded_video = upload_vedio("./ActionScoring_Video/SampleRenderedOutput.mp4")
			video_message = VideoSendMessage(original_content_url=uploaded_video, preview_image_url='https://imgur.com/Qf7sRds')
			video_list.append(video_message)

			command = ("ffmpeg -i -y ./ActionScoring_Video/CompareRenderedOutput.avi ./ActionScoring_Video/CompareRenderedOutput.mp4")
			subprocess.call(command, shell=True)
			uploaded_video = upload_vedio("./ActionScoring_Video/CompareRenderedOutput.mp4")
			video_message = VideoSendMessage(original_content_url=uploaded_video, preview_image_url='https://imgur.com/Qf7sRds')
			video_list.append(video_message)

			fr = open('./ActionScoring_Video/FinalVideoScore.txt', 'r')
			grade_video = fr.read()
			fr.close()
			text_message = TextSendMessage(text=grade_video + "分")

			line_bot_api.reply_message(event.reply_token, [video_list[0], video_list[1], text_message])

	else:
		line_bot_api.reply_message(event.reply_token,TextSendMessage(text='系統錯誤(video handler)'))
		input_counter = 0
		mode = chat_bot
		



# main function
import os
if __name__ == "__main__":
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port)
