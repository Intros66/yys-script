# coding=utf-8
import function

challengePic = function.importPic('liaoli', 'tiaozhan')
endPic = function.importPic('liaoli', 'shengli')
fudaiPic = function.importPic('liaoli', 'fudai')
finalPic = function.importPic('liaoli', 'finally')
xuanPic = function.importPic('liaoli', 'xuanshang')


def clickFunction(sp, res, box):
    clickRange = [sp[1], sp[0]]  # 点击范围
    x, y = function.getPoint(res, box[0], box[1], clickRange)
    function.moveCurPos(x, y)
    function.clickLeftCur()


def yuling():
    while True:
        box = function.getWindowInfo()
        pic = function.screenShot(box)
        print(function.match(pic, challengePic).max())
        function.randomDelay(0.2, 0.5)
        if function.match(pic, challengePic).max() > 0.75:
            print('挑战开始')
            res = function.match(pic, challengePic)
            print('res==>', res)
            sp = challengePic.shape
            clickFunction(sp, res, box)
            function.randomDelay(8,10)  # 时间可以自己设置
        elif function.match(pic, endPic).max() > 0.8:
            print('胜利')
            res = function.match(pic, endPic)
            sp = endPic.shape
            clickFunction(sp, res, box)
            function.randomDelay(0.3, 0.6)
            clickFunction(sp, res, box)
            function.randomDelay(0.3, 0.6)
            clickFunction(sp, res, box)
            function.randomDelay(0.3, 0.6)
      
        elif function.match(pic, fudaiPic).max() > 0.75:
            print(3)
            res = function.match(pic, fudaiPic)
            sp = fudaiPic.shape
            clickFunction(sp, res, box)
            function.randomDelay(0.3, 0.6)
            clickFunction(sp, res, box)
            function.randomDelay(0.3, 0.6)
        elif function.match(pic, xuanPic).max() > 0.8:
            print(3)
            res = function.match(pic, xuanPic)
            sp = xuanPic.shape
            clickFunction(sp, res, box)
            function.randomDelay(0.3, 0.8)



if __name__ == '__main__':
    yuling()
