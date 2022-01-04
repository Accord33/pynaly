#データ分析用ライブラリ

#平均値
def ave(date):
    total = 0
    for i in date:
        total += i
    ave = total/len(date)
    return ave

#約数
def divisor(num):
    divisors = []
    for i in range(1, num+1):
        if num % i == 0:
            divisors.append(i)
    return divisors

#倍数
def multiple(num,multp):
    multiple_num = list()
    for i in range(1,multp+1):
        multiple_num.append(num*i)
    return multiple_num

#円周率
def pi():
    return 3.141592653589793

#ネイピア数
def e():
    return 2.718281828459045

#シグマ+
def sigmap(i,n,k):
    a = 0
    for x in range(i,n+1):
        a+= x+k
    return a

#シグマX
def sigmax(i,n,r):
    a = 0
    for x in range(1,n+1):
        a+= i*(r**(x-1))
    return a