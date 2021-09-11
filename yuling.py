# coding=utf-8
import function


challengePic = function.importPic('yuling', 'challengePic')
endPic = function.importPic('yuling', 'victoryPic')
fudaiPic = function.importPic('yuling', 'fudaiPic')
xuanPic = function.importPic('partner', 'xuanshang')


def clickFunction(sp, res, box):
	clickRange = [sp[1], sp[0]]  # 点击范围
	x, y = function.getPoint(res, box[0], box[1], clickRange)
	function.moveCurPos(x, y)
	function.clickLeftCur()


def yuling():
	while True:
		box = function.getWindowInfo()
		pic = function.screenShot(box)
		# print(box, pic)
		print ('ScreenShot')
		if function.match(pic, challengePic).max() > 0.75:
			print ('御灵开始')
			res = function.match(pic, challengePic)
			sp = challengePic.shape
			clickFunction(sp, res, box)
			function.randomDelay(20, 20)		# 时间可以自己设置
		elif function.match(pic, endPic).max() > 0.75:
			print (2)
			res = function.match(pic, endPic)
			sp = endPic.shape
			clickFunction(sp, res, box)
			function.randomDelay(0.3, 0.6)
			clickFunction(sp, res, box)
			function.randomDelay(0.3, 0.6)
			clickFunction(sp, res, box)
			function.randomDelay(0.3, 0.6)
			clickFunction(sp, res, box)
			function.randomDelay(0.3, 0.6)
		elif function.match(pic, fudaiPic).max() > 0.75:
			print (3)
			res = function.match(pic, fudaiPic)
			sp = fudaiPic.shape
			clickFunction(sp, res, box)
		elif function.match(pic, xuanPic).max() > 0.8:
			print(3)
			res = function.match(pic, xuanPic)
			sp = xuanPic.shape
			clickFunction(sp, res, box)
			function.randomDelay(0.3, 0.8)


if __name__ == '__main__':
	yuling()