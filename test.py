

def searchExt(rootPath, ext):
	"""
	"""
	results = []
	for root, dirs, files in os.walk(rootPath, topdown=

def genProxy(proxy, files):
	"""
	file 리스트를 받아서 proxy경로에 
	프록시 이미지를 생성한다.
	"""




def genMov(rootPath, ext):
	"""
	path 경로에 있는 파일을 이용해서 mov를 생성한다.
	"""
	results = []
	for root, dirs, files in os.walk(rootPath, topdown=True):
		if not files:
			continue
		files.sort()
		start = "/".join([root] + dirs + [files[0]])
		end = "/".join([root] + dirs + [files[-1]])
		print start
		print pathapi.seqnum

def seqnum(path):
	"""
	경로에서 시퀀스 넘버를 반환한다.
	"""
	p = re.findall('\.(\d+)\.', path.replace("\\","/"))
	if len(p) != 1:
		return -1, "경로에서 seqnum 정보를 가지고 올 수 없습니다."
	return int(p[0]), None
