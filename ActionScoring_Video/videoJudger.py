import subprocess
import numpy as np
import os, json
import pandas as pd
import math
import time
import glob
import matplotlib.pyplot as plt
import socket
import cv2


def generateVector(fileName): #生成這個frame的向量資訊(讀取json)
	myVector = []
	with open(fileName) as f:
		data = json.load(f)
		if(len(data["people"]) == 0):
			return myVector

		keys = data["people"][0]["pose_keypoints_2d"]
		#head
		if keys[2] == 0 or keys[5] == 0 : #若有一個點沒偵測到,向量設為0
			myVector.append([0,0])
		else:
			myVector.append([keys[3]-keys[0],keys[4]-keys[1]])

		#body
		if keys[26] == 0 or keys[5] == 0 : #若有一個點沒偵測到,向量設為0
			myVector.append([0,0])
		else:
			myVector.append([keys[24]-keys[3],keys[25]-keys[4]])
		
		#right hand
		if keys[8] == 0 or keys[5] == 0 : #若有一個點沒偵測到,向量設為0
			myVector.append([0,0])
		else :
			myVector.append([keys[6]-keys[3],keys[7]-keys[4]])

		if keys[11] == 0 or keys[8] == 0 : #若有一個點沒偵測到,向量設為0
			myVector.append([0,0])
		else:
			myVector.append([keys[9]-keys[6],keys[10]-keys[7]])
	   
		if keys[14] == 0 or keys[11] == 0 : #若有一個點沒偵測到,向量設為0
			myVector.append([0,0])
		else:
			myVector.append([keys[12]-keys[9],keys[13]-keys[10]])
		
		#left hand
		if keys[17] == 0 or keys[5] == 0 : #若有一個點沒偵測到,向量設為0
			myVector.append([0,0])
		else:
			myVector.append([keys[15]-keys[3],keys[16]-keys[4]])
		
		if keys[20] == 0 or keys[17] == 0 : #若有一個點沒偵測到,向量設為0
			myVector.append([0,0])
		else:
			myVector.append([keys[18]-keys[15],keys[19]-keys[16]])
		
		if keys[23] == 0 or keys[20] == 0 : #若有一個點沒偵測到,向量設為0
			myVector.append([0,0])
		else:
			myVector.append([keys[21]-keys[18],keys[22]-keys[19]])
		
		#right leg
		if keys[29] == 0 or keys[26] == 0 : #若有一個點沒偵測到,向量設為0
			myVector.append([0,0])
		else:
			myVector.append([keys[27]-keys[24],keys[28]-keys[25]])

		if keys[32] == 0 or keys[29] == 0 : #若有一個點沒偵測到,向量設為0
			myVector.append([0,0])
		else:
			myVector.append([keys[30]-keys[27],keys[31]-keys[28]])
		
		if keys[35] == 0 or keys[32] == 0 : #若有一個點沒偵測到,向量設為0
			myVector.append([0,0])
		else:
			myVector.append([keys[33]-keys[30],keys[34]-keys[31]])
		
		if keys[68] == 0 or keys[35] == 0 : #若有一個點沒偵測到,向量設為0
			myVector.append([0,0])
		else:
			myVector.append([keys[66]-keys[33],keys[67]-keys[34]])
		
		#left leg
		if keys[38] == 0 or keys[26] == 0 : #若有一個點沒偵測到,向量設為0
			myVector.append([0,0])
		else:
			myVector.append([keys[36]-keys[24],keys[37]-keys[25]])
		
		if keys[41] == 0 or keys[38] == 0 : #若有一個點沒偵測到,向量設為0
			myVector.append([0,0])
		else:
			myVector.append([keys[39]-keys[36],keys[40]-keys[37]])
		
		if keys[44] == 0 or keys[41] == 0 : #若有一個點沒偵測到,向量設為0
			myVector.append([0,0])
		else:
			myVector.append([keys[42]-keys[39],keys[43]-keys[40]])
		
		if keys[59] == 0 or keys[44] == 0 : #若有一個點沒偵測到,向量設為0
			myVector.append([0,0])
		else:
			myVector.append([keys[57]-keys[42],keys[58]-keys[43]])
		
	return myVector


def angleDiff(vector_1,vector_2): #回傳兩個向量的角度差
	unit_vector_1 = vector_1 / np.linalg.norm(vector_1)
	unit_vector_2 = vector_2 / np.linalg.norm(vector_2)
	dot_product = np.dot(unit_vector_1, unit_vector_2)
	if dot_product > 1 :
		dot_product = 1
	angle = np.arccos(dot_product)
	return angle*57.3

def VectorDiffLoss(vec1,vec2):
	points = 0
	i = 1
	zeroVectorCount = 0
	while i < 16 :
		if(vec1[i][0] == 0 and vec1[i][1] == 0) or (vec2[i][0] == 0 and vec2[i][1] == 0) :#如果有一個是0向量
			zeroVectorCount += 1
			points += 1 #加一意思一下
		else :
			t = angleDiff(vec1[i],vec2[i])
			t = (t/6.25)**(4) #相差5度內沒什麼關係
			points += t
		i+=1
	if zeroVectorCount >= 6: #如果超過8個向量沒被偵測,讓分數一次加很多
		points += 500000
	return points/16


def scoreCalculate(myVector):
	global a
	minLoss = 999999999
	chosen = 0
	for i in range(len(sampleSwingVector)):
		lossValue = VectorDiffLoss(myVector,sampleSwingVector[i])
		if lossValue < minLoss:
			chosen = i
			minLoss = lossValue
	a[chosen] = 1
	return minLoss


lastFiles = glob.glob('./ActionScoring_Video/SampleJson/*')
for f in lastFiles:
	os.remove(f)
lastFiles = glob.glob('./ActionScoring_Video/CompareJson/*')
for f in lastFiles:
	os.remove(f)
p1 = subprocess.Popen(['./openpose/build/examples/openpose/openpose.bin', '--model_folder', './openpose/models', '--num_gpu_start', '0', '--number_people_max', '1','--display', '0', '--net_resolution', '336x336', '--video', './ActionScoring_Video/VideoSource/Sample.mp4', '--write_video', './ActionScoring_Video/SampleRenderedOutput.avi', '--write_json', './ActionScoring_Video/SampleJson']) 
p1.wait()
p2 = subprocess.Popen(['./openpose/build/examples/openpose/openpose.bin', '--model_folder', './openpose/models', '--num_gpu_start', '0', '--number_people_max', '1','--display', '0', '--net_resolution', '336x336', '--video', './ActionScoring_Video/VideoSource/Compare.mp4', '--write_video', './ActionScoring_Video/CompareRenderedOutput.avi', '--write_json', './ActionScoring_Video/CompareJson']) 
p2.wait()

sampleSwingVector = []
path_to_Target = './ActionScoring_Video/SampleJson/'
Target_json_files = [pos_json for pos_json in os.listdir(path_to_Target) if pos_json.endswith('.json')]
for i in range(len(Target_json_files)):
	sampleSwingVector.append(generateVector(path_to_Target+Target_json_files[i]))


path_to_Compare = './ActionScoring_Video/CompareJson/'
Compare_json_files = [pos_json for pos_json in os.listdir(path_to_Compare) if pos_json.endswith('.json')]

a = np.zeros(shape=len(sampleSwingVector))

totalLoss = 0
num = 0
for index, currentFrameName in enumerate(Compare_json_files):
	currentVector = generateVector(path_to_Compare+currentFrameName) #取得target的向量資訊
	if(len(currentVector) > 0):
		score = scoreCalculate(currentVector)
		totalLoss += score
		num += 1

last = 1
continousZero = 0
val = 0
for p in range(len(a)):
	if a[p] == 1:
		val += continousZero*continousZero
		last = 1
		continousZero = 0
	else:
		continousZero += 1
		last = 0

finalScore = 0
if val >= 1500:
	finalScore += 1
elif val >= 1200:
	finalScore += 2
elif val >= 900:
	finalScore += 3
elif val >= 700:
	finalScore += 4
else:
	finalScore += 5

if (totalLoss/num) <= 1000:
	finalScore += 5
elif (totalLoss/num) <= 10000:
	finalScore += 4
elif (totalLoss/num) <= 30000:
	finalScore += 3
elif (totalLoss/num) <= 50000:
	finalScore += 2
else:
	finalScore += 1


print(val)
print(totalLoss/len(Compare_json_files))
print(finalScore/2)

f = open('./ActionScoring_Video/FinalVideoScore.txt', 'w')
f.write(str(int(finalScore/2)))
f.close()
   