#中文数字和阿拉伯数字之间的相互转换：
def 中文转阿拉伯(s):
    if len(a) <= 2:
        a[1] = s[1]
    elif a[2] == '零':
        a[2] = 0
    elif a[2] == '一':
        a[2] = 1
    elif a[2] == '二':
        a[2] = 2
    elif a[2] == '三':
        a[2] = 3
    elif a[2] == '四':
        a[2] = 4
    elif s[2] == '五':
        a[2] = 5
    elif a[2] == '六':
        a[2] = 6
    elif a[2] == '七':
        a[2] = 7
    elif a[2] == '八':
        a[2] = 8
    elif a[2] == '九':
        a[2] = 9
    elif a[2] == '十':
        a[2] = 10
    elif a[3] == '零':
        a[3] = 0
    elif a[3] == '一':
        a[3] = 1
    elif a[3] == '二':
        a[3] = 2
    elif a[3] == '三':
        a[3] = 3
    elif a[3] == '四':
        a[3] = 4
    elif a[3] == '五':
        a[3] = 5
    elif a[3] == '六':
        a[3] = 6
    elif a[3] == '七':
        a[3] = 7
    elif a[3] == '八':
        a[3] = 8
    elif a[3] == '九':
        a[3] = 9
    elif a[3] == '十':
        a[3] = 10
    return a
  
  def 阿拉伯转中文():
    if t[1] == 0:
        t[3] = '零'
    elif t[1] == 1:
        t[3] = '一'
    elif t[1] == 2:
        t[3] = '二'
    elif t[1] == 3:
        t[3] = '三'
    elif t[1] == 4:
        t[3] = '四'
    elif t[1] == 5:
        t[3] = '五'
    elif t[1] == 6:
        t[3] = '六'
    elif t[1] == 7:
        t[3] = '七'
    elif t[1] == 8:
        t[3] = '八'
    elif t[1] == 9:
        t[3] = '九'
    elif t[1] == 10:
        t[3] = '十'
    return a
