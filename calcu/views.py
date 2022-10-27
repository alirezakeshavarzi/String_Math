from django.shortcuts import render
from django.template import loader
from django.http import JsonResponse
from django.views import generic


import math


class strmath():
    i = 0
    save = 0
    lste = 0
    ans = [None] * 1
    stack = [None] * 1
    topans = 0
    top = -1


    def __init__(self, st2):
        self.st2 = st2
        self.lste = len(self.st2)
        self.ans = [None] * self.lste
        self.stack = [None] * self.lste
        self.initio(self.ans)
        self.initio(self.stack)

    def initio(self, str):  # set all ans array to zero(string)
        i = 0
        lo = len(str)
        while i < lo:
            str[i] = "00"
            i += 1

    def isempty(se,s):
        if s == '00':
            return True
        else:
            return False
    def getnum(self, str):  # get number of each operator
        i = 0
        l = len(str)
        while i < l:
            if str[i].isdigit():
                return int(str[i])
                break

            i += 1

    def gotohome(self):  # add stack and ans array
        l = self.lste
        while self.i < l:
            if not self.st2[self.i].isdigit():
                sub = self.st2[self.save:self.i]  # cut number that is left side of operator.
                self.save = self.i + 1  # update save to first of right side number of operator.

                self.ans[self.topans] = sub  # the number into ans array.
                self.topans += 1

                if self.st2[self.i] == '+':

                    if self.stack[self.top] == '(':
                        self.top += 1
                        self.stack[self.top] = "+2"
                    else:
                        num = self.getnum(self.stack[self.top])
                        if 2 > num or 2 == num:
                            self.top += 1
                            self.stack[self.top] = "+2"

                        elif 2 < num:
                            self.ans[self.topans] = self.stack[self.top]
                            self.stack[self.top] = "+2"
                            self.topans += 1


                elif self.st2[self.i] == '-':

                    if self.stack[self.top] == '(':
                        self.top += 1
                        self.stack[self.top] = "-1"
                    else:
                        num = self.getnum(self.stack[self.top])
                        if 2 > num or 2 == num:
                            self.top += 1
                            self.stack[self.top] = "-1"

                        elif 2 < num:
                            self.ans[self.topans] = self.stack[self.top]
                            self.stack[self.top] = "-1"
                            self.topans += 1



                elif self.st2[self.i] == '*':

                    if self.stack[self.top] == '(':
                        self.top += 1
                        self.stack[self.top] = "*4"
                    else:
                        num = self.getnum(self.stack[self.top])
                        if 2 > num or 2 == num:
                            self.top += 1
                            self.stack[self.top] = "*4"

                        elif 2 < num:
                            self.ans[self.topans] = self.stack[self.top]
                            self.stack[self.top] = "*4"
                            self.topans += 1


                elif self.st2[self.i] == '/':

                    if self.stack[self.top] == '(':
                        self.top += 1
                        self.stack[self.top] = "/3"
                    else:
                        num = self.getnum(self.stack[self.top])
                        if 2 > num or 2 == num:
                            self.top += 1
                            self.stack[self.top] = "/3"

                        elif 2 < num:
                            self.ans[self.topans] = self.stack[self.top]
                            self.stack[self.top] = "/3"
                            self.topans += 1


                elif self.st2[self.i] == '^':

                    if self.stack[self.top] == '(':
                        self.top += 1
                        self.stack[self.top] = "^5"
                    else:
                        num = self.getnum(self.stack[self.top])
                        if 2 > num or 2 == num:
                            self.top += 1
                            self.stack[self.top] = "^5"

                        elif 2 < num:
                            self.ans[self.topans] = self.stack[self.top]
                            self.stack[self.top] = "^5"
                            self.topans += 1

                elif self.st2[self.i] == '(':

                    self.top += 1
                    self.stack[self.top] = '('

                elif self.st2[self.i] == ')':

                    while 1 == 1:
                        a = self.isempty(self.stack[self.top])
                        if a == False:
                            self.ans[self.topans] = self.stack[self.top]
                            self.top += 1
                            self.topans += 1
                        else:
                            break

            self.i += 1

        sub = self.st2[self.save:self.i]  # lastes number into a sub.
        self.ans[self.topans] = sub  # and then goto ans(answer) array.
        return self.top

    def stackintoArr(self):
        i = 0
        t = self.gotohome()
        l = self.lste

        while i < l:
            if self.ans[i] == '00':
                self.ans[i] = self.stack[t]
                t -= 1
            i += 1

    def isfloat(self, w):  # checking for is float or not.
        w = str(w)
        i = 0
        l = len(w)
        while i < l:
            if w[i] == '.':
                return True
            i += 1

    def cal(self):  # for calculate number and operator that is that are in array.
        i = 0
        l = len(self.ans)
        top = -1

        while i < l:
            if self.ans[i].isdigit():
                top += 1

                self.stack[top] = self.ans[i]

            else:
                if self.ans[i] == '+2':
                    if self.isfloat(self.stack[top - 1]) or self.isfloat(self.stack[top]):
                        self.stack[top - 1] = float(self.stack[top - 1]) + float(self.stack[top])
                        self.stack[top] = 0
                        top -= 1
                    else:
                        self.stack[top - 1] = int(self.stack[top - 1]) + int(self.stack[top])
                        self.stack[top] = 0
                        top -= 1


                elif self.ans[i] == '*4':
                    if self.isfloat(self.stack[top - 1]) or self.isfloat(self.stack[top]):
                        self.stack[top - 1] = float(self.stack[top - 1]) * float(self.stack[top])
                        self.stack[top] = 0
                        top -= 1
                    else:
                        self.stack[top - 1] = int(self.stack[top - 1]) * int(self.stack[top])
                        self.stack[top] = 0
                        top -= 1
                elif self.ans[i] == '-1':
                    if self.isfloat(self.stack[top - 1]) or self.isfloat(self.stack[top]):
                        self.stack[top - 1] = float(self.stack[top - 1]) - float(self.stack[top])
                        self.stack[top] = 0
                        top -= 1
                    else:
                        self.stack[top - 1] = int(self.stack[top - 1]) - int(self.stack[top])
                        self.stack[top] = 0
                        top -= 1
                elif self.ans[i] == '/3':
                    if self.isfloat(self.stack[top - 1]) or self.isfloat(self.stack[top]):
                        self.stack[top - 1] = float(self.stack[top - 1]) / float(self.stack[top])
                        self.stack[top] = 0
                        top -= 1
                        #self.solution = "hi"#str(float(self.stack[top - 1])) + " / " + str(float(self.stack[top])) + " = " + str(self.stack[top - 1])
                    else:
                        self.stack[top - 1] = int(self.stack[top - 1]) / int(self.stack[top])
                        self.stack[top] = 0
                        top -= 1
                elif self.ans[i] == '^5':
                    if self.isfloat(self.stack[top - 1]) or self.isfloat(self.stack[top]):
                        self.stack[top - 1] = math.pow(float(self.stack[top - 1]), float(self.stack[top]))
                        self.stack[top] = 0
                        top -= 1
                    else:
                        self.stack[top - 1] = math.pow(int(self.stack[top - 1]), int(self.stack[top]))
                        self.stack[top] = 0
                        top -= 1

            i += 1
        return self.stack[0]

    def pr(self):
        self.gotohome()
        self.stackintoArr()
        self.cal()
        #self.solution = "222"
        return self.stack[0]


class index(generic.ListView):
    #template_name = 'index.html'

    def get(self,r):
        st2 = r.GET.get('str', False)

        if st2 == False:
            st2 = "0"


        st2 = str(st2)
        m = strmath(st2)
        #print("///////////////solotion : ////////////  =  ",m.solution)
        try:
            res = m.pr()
        except ZeroDivisionError:
            res = "ZeroDivisionError"

        c = {'res': res, 'a': st2}
        return render(r, 'index.html', c)

# Create your views here.
