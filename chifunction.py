# coding=utf-8
import function

challengePic = function.importPic('chi', 'challengePic')  # challengePic 开始挑战图片
endPic = function.importPic('chi', 'endPic')  # endPic 结束挑战图片
fudaiPic = function.importPic('chi', 'fudaiPic')
xuanPic = function.importPic('partner', 'xuanshang')

def clickFunction(sp, res, box):
    clickRange = [sp[1], sp[0]]  # 点击范围
    x, y = function.getPoint(res, box[0], box[1], clickRange)
    function.moveCurPos(x, y)
    function.clickLeftCur()


def chi():
    while True:
        box = function.getWindowInfo()
        pic = function.screenShot(box)  # type: box
        if function.match(pic, challengePic).max() > 0.75:
            res = function.match(pic, challengePic)
            sp = challengePic.shape
            clickFunction(sp, res, box)
            function.randomDelay(30, 32)
        elif function.match(pic, endPic).max() > 0.75:
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
            res = function.match(pic, fudaiPic)
            sp = fudaiPic.shape
            clickFunction(sp, res, box)
            function.randomDelay(0.3, 0.8)
        elif function.match(pic, xuanPic).max() > 0.8:
            res = function.match(pic, xuanPic)
            sp = xuanPic.shape
            clickFunction(sp, res, box)
            function.randomDelay(0.3, 0.8)


if __name__ == '__main__':
    chi()


