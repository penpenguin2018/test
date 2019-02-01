#!/usr/bin/env python
#coding:utf8

import sys
import subprocess
import os

def searchItem(root):
	"""
	경로를 찾는다.
	"""
	seqs = []
	for subdir in os.listdir(root):
		shot = []
		for f in os.listdir(root+"/"+subdir):
			shot.append("/".join([root,subdir,f]))
		shot.sort()
		seqs.append(shot)
	return seqs

def genproxy(path):
	"""
	경로를 입력 받으면 proxy 경로를 만든다.
	"""
	for i in os.listdir(path):
		os.system("mkdir -p /tmp/proxy%s/%s/" %(path,i))

def conjpg(rootdir):
	"""
	입력받은 경로의 파일을 jpg로 바꾼다.
	"""
	for i in rootdir:
		for f in i:
			cmd = "convert %s /tmp/proxy%s" % (f,f.replace(".exr", ".jpg"))
			os.system(cmd)

def genmov(path):
	
	os.system("ffmpeg -f image2 -start_number 100 -r 24 -i %s" %(path)

def toFFmpeg(path) :
	"""
	경로를 받아서 시퀀스라면 ffmpeg 경로로 바꾸어준다.
	"""
	p = re.findall('\.(\d+)\.', path.replace("\\", "/")
	if len(p) != 1:                                     #예외 처리
		return path, "경로가 시퀀스 구조가 아닙니다."  
	digitNum = len(p[0])
	head, tail = path.split(p[0])
	return "%s%%%dd%s" %(head, digitNum, tail), None

if __name__ == "__main__":
	root = "/project/circle/in/aces_exr"
	genproxy(root)
	conjpg(searchItem(root))

#os.path.split(src)
#os.path.splitext(f)
