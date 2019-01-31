#!/usr/bin/env python
#coding:utf8

import sys
import subprocess
import os

def genThumb(src):
	"""
	경로를 입력받으면 썸네일을 만든다.
	"""
	if not os.path.exists(src):
		return "", "파일이 존재하지 않습니다."
	if not os.path.exists(src):
		return "", "파일형태가 아닙니다."
	if not os.path.exists("/usr/bin/convert"):
		return None, "ImageMagick이 설치되지 않았습니다."

	d, f = os.path.split(src)
	notuse, ext = os.path.splitext(f)
	dst = d+"/"+f.replace(ext, ".jpg")
	size="360X240"
	cmds = ["convert", src, "-thumbnail", size,
			"-background", "black", "-gravity", "center",
			"-extent", size, dst]
	p = subprocess.Popen(cmds, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	return p.communicate()

if __name__ == "__main__" :
	src = "/project/circle/in/aces_exr/A003C025_150830_R0D0/A003C025_150830_R0D0.078950.exr"
	stdOut, stdErr = genThumb(src)
	if stdErr :
		sys.stderr.write(stdErr)
	sys.stdout.write(stdOut)
