# coding=utf-8
import function

challengePic = function.importPic('juexing', 'challengePic')
endPic = function.importPic('juexing', 'victoryPic')
fudaiPic = function.importPic('juexing', 'fudaiPic')


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
        print('ScreenShot')
        if function.match(pic, challengePic).max() > 0.75:
            print('觉醒开始！')
            res = function.match(pic, challengePic)
            sp = challengePic.shape
            clickFunction(sp, res, box)
            function.randomDelay(10, 20)  # 时间可以自己设置
            print('----')
        elif function.match(pic, endPic).max() > 0.75:
            print(2)
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
            print(3)
            res = function.match(pic, fudaiPic)
            sp = fudaiPic.shape
            clickFunction(sp, res, box)


if __name__ == '__main__':
    yuling()
