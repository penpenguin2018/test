#!/usr/bin/env python
#coding:utf8

import os
import subprocess

def search(root):
	"""
	경로를 찾는다
	"""
	seqs = []
	for subdir in os.listdir(root):
		shot = []
		for f in os.listdir(root+"/"+subdir):
			shot.append("/".join([root,subdir,f]))
		shot.sort()
		seqs.append(shot)
	return seqs
	#seqs는 폴더 구조를 그대로 리스트로 묶어둔 것임

def genproxy(root):
	"""
	경로를 받으면 proxy 경로를 만든다.
	"""
	for subdir in os.listdir(root):
		os.system("mkdir -p /tmp/proxy%s/%s/" %(root,subdir))

def genjpg(root):
	for subdir in os.listdir(root):
		for f in os.listdir(root+"/"+subdir):
			src = "/".join([root,subdir,f])
			dst = "/".join(["/tmp/proxy",root,subdir,f.replace(".exr",".jpg")])
			cmd = "convert %s %s" %(src, dst)
			os.system(cmd)


####

def genmov(proxy):
	start = 

####

if __name__ == "__main__":
	root = "/project/circle/in/aces_exr"
	genproxy(root)
	genjpg(root)
