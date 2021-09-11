#coding=utf8
import function

challengePic = function.importPic('partner', 'challengePic')
endPic = function.importPic('partner', 'victoryPic')
fudaiPic = function.importPic('partner', 'fudaiPic')
xuanPic = function.importPic('partner', 'xuanshang')
autoPic = function.importPic('common', 'auto')
defeatPic = function.importPic('common', 'defeat')


def clickFunction(sp, res, box):

    clickRange = [sp[1], sp[0]]  # 点击范围
    x, y = function.getPoint(res, box[0], box[1], clickRange)
    function.moveCurPos(x, y)
    function.clickLeftCur()


def partner():
    while True:
        box = function.getWindowInfo()
        pic = function.screenShot(box)
        function.randomDelay(0.2, 0.5)
        if function.match(pic, challengePic).max() > 0.75:
            print('组队开始')
            res = function.match(pic, challengePic)
            sp = challengePic.shape
            clickFunction(sp, res, box)
            function.randomDelay(15, 20)  # 时间可以自己设置
        elif function.match(pic, autoPic).max() > 0.75:
            print('自动')
            res = function.match(pic, autoPic)
            sp = autoPic.shape
            clickFunction(sp, res, box)
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
            clickFunction(sp, res, box)
            function.randomDelay(0.3, 0.6)
        elif function.match(pic, defeatPic).max() > 0.75:
            print('失败')
            res = function.match(pic, defeatPic)
            sp = defeatPic.shape
            clickFunction(sp, res, box)
            function.randomDelay(0.3, 0.6)
            clickFunction(sp, res, box)
        elif function.match(pic, fudaiPic).max() > 0.8:
            print('福袋')
            res = function.match(pic, fudaiPic)
            sp = fudaiPic.shape
            clickFunction(sp, res, box)
        elif function.match(pic, xuanPic).max() > 0.8:
            print('悬赏')
            res = function.match(pic, xuanPic)
            sp = xuanPic.shape
            clickFunction(sp, res, box)
            function.randomDelay(0.3, 0.8)


if __name__ == '__main__':
    partner()