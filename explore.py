import function
import win32gui
import win32con
import win32api
import win32con
import random

tansuoPic = function.importPic('explore', 'tansuo')
suodingPic = function.importPic('explore', 'suoding')
fightPic = function.importPic('explore', 'fight')
fudaiPic = function.importPic('explore', 'fudai')
quedingPic = function.importPic('explore', 'queding')
endPic = function.importPic('explore', 'shengli')
zhunbeiPic = function.importPic('explore', 'zhunbei')
bossPic = function.importPic('explore', 'boss')
exitPic = function.importPic('explore', 'exit')
di28Pic = function.importPic('explore', 'di28')
tingyuanPic = function.importPic('explore', 'tingyuan')
floorPic = function.importPic('explore', 'floor')

def clickFunction(sp, res, box):
    clickRange = [sp[1], sp[0]]  # 点击范围
    x, y = function.getPoint(res, box[0], box[1], clickRange)
    function.moveCurPos(x, y)
    function.clickLeftCur()


def explore():
    i = 0
    while True:

        box = function.getWindowInfo()
        pic = function.screenShot(box)
        # print(box, pic)
        print('ScreenShot')
        if function.match(pic, tansuoPic).max() > 0.75:
            print('探索开始！')
            ## 点击探索
            res = function.match(pic, tansuoPic)
            sp = tansuoPic.shape
            clickFunction(sp, res, box)
            function.randomDelay(2, 3)  # 时间可以自己设置
            # x1, y1, x2, y2 = box
            # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN | win32con.MOUSEEVENTF_LEFTUP, x2 + random.randint(300, 370), y2 - random.randint(150,170))
            # function.randomDelay(3, 5)
        elif function.match(pic, fightPic).max() > 0.75:
            print('开始挑战！')
            res = function.match(pic, fightPic)
            sp = fightPic.shape
            clickFunction(sp, res, box)
            function.randomDelay(0.6, 1)
        elif function.match(pic, bossPic).max() > 0.75:
            print('开始挑战boss！')
            res = function.match(pic, bossPic)
            sp = bossPic.shape
            clickFunction(sp, res, box)
            function.randomDelay(0.6, 1)
        elif function.match(pic, zhunbeiPic).max() > 0.75:
            print('准备！')
            res = function.match(pic, zhunbeiPic)
            sp = zhunbeiPic.shape
            clickFunction(sp, res, box)
        # 结束
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
        # 福袋
        elif function.match(pic, fudaiPic).max() > 0.75:
            res = function.match(pic, fudaiPic)
            sp = fudaiPic.shape
            clickFunction(sp, res, box)
            function.randomDelay(0.3, 0.6)
            clickFunction(sp, res, box)
            function.randomDelay(0.3, 0.6)
        # 战斗图标
        elif function.match(pic, fightPic).max() < 0.70:
            if function.match(pic, floorPic).max() > 0.70:
                es = function.match(pic, floorPic)
                sp = floorPic.shape
                clickFunction(sp, res, box)
                function.randomDelay(0.6, 1)
            if function.match(pic, di28Pic).max() > 0.75:
                res = function.match(pic, di28Pic)
                sp = exitPic.shape
                clickFunction(sp, res, box)
                function.randomDelay(1.5, 2)
            # 退出
            if function.match(pic, exitPic).max() > 0.75:
                res = function.match(pic, exitPic)
                sp = exitPic.shape
                clickFunction(sp, res, box)
                function.randomDelay(0.3, 0.6)
            # 确定
            if function.match(pic, quedingPic).max() > 0.75:
                res = function.match(pic, quedingPic)
                sp = quedingPic.shape
                clickFunction(sp, res, box)
                function.randomDelay(0.6, 1)
            # 探索
            if function.match(pic, tingyuanPic).max() > 0.75:
                res = function.match(pic, tingyuanPic)
                sp = tingyuanPic.shape
                clickFunction(sp, res, box)
                function.randomDelay(0.3, 0.6)


if __name__ == '__main__':
    explore()
