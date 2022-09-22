from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

import math

def index(r):
    st2 = r.GET.get('str', False)
    temp = loader.get_template('index.html')

    def initio(str):
        i = 0
        lo = len(str)
        while i < lo:
            str[i] = "00"
            i += 1

    def getnum(str):
        i = 0
        l = len(str)
        while i < l:
            if str[i].isdigit():
                return int(str[i])
                break

            i += 1
    st2 = str(st2)
    lstr = len(st2)

    ans = [None] * lstr
    initio(ans)
    topans = 0

    stack = [None] * 8
    initio(stack)
    top = -1
    stack[top] = "00"

    def gotohome(st2, topans, top):  # add stack and ans array
        save = 0
        i = 0
        l = len(st2)
        while i < l:
            if not st2[i].isdigit():

                sub = st2[save:i]  # cut number that is left side of operator.
                save = i + 1  # update save to first of right side number of operator.

                ans[topans] = sub  # the number into ans array.

                topans += 1

                if st2[i] == '+':
                    num = getnum(stack[top])
                    if 2 > num or 2 == num:
                        top += 1
                        stack[top] = "+2"

                    elif 2 < num:
                        ans[topans] = stack[top]
                        stack[top] = "+2"
                        topans += 1
                elif st2[i] == '-':
                    num = getnum(stack[top])
                    if 1 > num or 1 == num:
                        top += 1
                        stack[top] = '-1'

                    elif 1 < num:
                        ans[topans] = stack[top]
                        stack[top] = '-1'
                        topans += 1
                elif st2[i] == '*':
                    num = getnum(stack[top])
                    if 4 > num or 4 == num:
                        top += 1
                        stack[top] = '*4'

                    elif 4 < num:
                        ans[topans] = stack[top]
                        stack[top] = '*4'
                        topans += 1
                elif st2[i] == '/':
                    num = getnum(stack[top])
                    if 3 > num or 3 == num:
                        top += 1
                        stack[top] = '/3'

                    elif 3 < num:
                        ans[topans] = stack[top]
                        stack[top] = '/3'
                        topans += 1
                elif st2[i] == '^' or 5 == num:
                    num = getnum(stack[top])
                    if 5 > num:
                        top += 1
                        stack[top] = '^5'

                    elif 5 < num:
                        ans[topans] = stack[top]
                        stack[top] = '^5'
                        topans += 1

            i += 1

        sub = st2[save:i]  # lastes number into a sub.
        ans[topans] = sub  # and then goto ans(answer) array.
        return top

    def stackintoArr(s2, stack3, t):
        i = 0
        t = t
        l = len(s2)
        while i < l:
            if s2[i] == '00':
                s2[i] = stack3[t]
                t -= 1
            i += 1

    def isfloat(w):
        w = str(w)
        i = 0
        l = len(w)
        while i < l:
            if w[i] == '.':
                return True
            i += 1

    def cal(arr, stack2):
        i = 0
        l = len(arr)
        top = -1
        #zero(stack2)
        while i < l:
            if arr[i].isdigit():
                top += 1
                stack[top] = arr[i]

            else:
                if arr[i] == '+2':
                    if isfloat(stack2[top - 1]) or isfloat(stack2[top]):
                        stack2[top - 1] = float(stack2[top - 1]) + float(stack2[top])
                        stack2[top] = 0
                        top -= 1
                    else:
                        stack2[top - 1] = int(stack2[top - 1]) + int(stack2[top])
                        stack2[top] = 0
                        top -= 1


                elif arr[i] == '*4':
                    if isfloat(stack2[top - 1]) or isfloat(stack2[top]):
                        stack2[top - 1] = float(stack2[top - 1]) * float(stack2[top])
                        stack2[top] = 0
                        top -= 1
                    else:
                        stack2[top - 1] = int(stack2[top - 1]) * int(stack2[top])
                        stack2[top] = 0
                        top -= 1
                elif arr[i] == '-1':
                    if isfloat(stack2[top - 1]) or isfloat(stack2[top]):
                        stack2[top - 1] = float(stack2[top - 1]) - float(stack2[top])
                        stack2[top] = 0
                        top -= 1
                    else:
                        stack2[top - 1] = int(stack2[top - 1]) - int(stack2[top])
                        stack2[top] = 0
                        top -= 1
                elif arr[i] == '/3':
                    if isfloat(stack2[top - 1]) or isfloat(stack2[top]):
                        stack2[top - 1] = float(stack2[top - 1]) / float(stack2[top])
                        stack2[top] = 0
                        top -= 1
                    else:
                        stack2[top - 1] = int(stack2[top - 1]) / int(stack2[top])
                        stack2[top] = 0
                        top -= 1
                elif arr[i] == '^5':
                    if isfloat(stack2[top - 1]) or isfloat(stack2[top]):
                        stack2[top - 1] = math.pow(float(stack2[top - 1]), float(stack2[top]))
                        stack2[top] = 0
                        top -= 1
                    else:
                        stack2[top - 1] = math.pow(int(stack2[top - 1]), int(stack2[top]))
                        stack2[top] = 0
                        top -= 1
            i += 1
        return stack[0]

    stackintoArr(ans, stack, top)

    try:
        res = cal(ans, stack)
    except ZeroDivisionError:
        res = "Undefined"



    c = {'res':res, 'a':st2}
    return HttpResponse(temp.render(c,r))
# Create your views here.
