#Staycia930 数値計算用自作ライブラリ Pynaly

#Int型
class Int:
    def __init__(self, num=None):
        self.num = int(num)

    def __add__(self, other):
        if isinstance(other,Int):
            return Int(self.num+ other.num)
        elif isinstance(other, Float):
            return Float(self.num+other.num)
        else:
            raise TypeError('different object type')

    def __sub__(self, other):
        if isinstance(other,Int):
            return Int(self.num - other.num)
        elif isinstance(other, Float):
            return Float(self.num - other.num)
        else:
            raise TypeError('different object type')

    def __mul__(self, other):
        if isinstance(other,Int):
            return Int(self.num * other.num)
        elif isinstance(other, Float):
            return Float(self.num * other.num)
        else:
            raise TypeError('different object type')

    def __truediv__(self, other):
        if isinstance(other,Int):
            return Int(self.num / other.num)
        elif isinstance(other, Float):
            return Float(self.num / other.num)
        else:
            raise TypeError('different object type')

    def flootdiv(self, other):
        if isinstance(other,Int):
            return Int(self.num // other.num)
        elif isinstance(other, Float):
            return Float(self.num // other.num)
        else:
            raise TypeError('different object type')

    def __repr__(self):
        return repr(self.num)

    #Float型に変換
    def _float(self):
        return Float(self.num)


#Float型
class Float:
    def __init__(self, num):
        self.num = float(num)

    def __add__(self, other):
        if isinstance(other, Int) or isinstance(other, Float):
            return Float(self.num + other.num)
        else:
            raise TypeError('different object type')

    def __sub__(self, other):
        if isinstance(other, Int) or isinstance(other, Float):
            return Float(self.num - other.num)
        else:
            raise TypeError('different object type')

    def __mul__(self, other):
        if isinstance(other, Int) or isinstance(other, Float):
            return Float(self.num * other.num)
        else:
            raise TypeError('different object type')

    def __truediv__(self, other):
        if isinstance(other, Int) or isinstance(other, Float):
            return Float(self.num / other.num)
        else:
            raise TypeError('different object type')

    def flootdiv(self, other):
        if isinstance(other, Int) or isinstance(other, Float):
            return Float(self.num // other.num)
        else:
            raise TypeError('different object type')

    def __repr__(self):
        return repr(self.num)

    #Int型に変換
    def _int(self):
        return Int(self.num)


class Array:
    def __init__(self,data):
        self.array = data
        self.Mode()
        self.Median()
        self.Average()
        self.min = sorted(self.array)[0]
        self.max = sorted(self.array)[-1]
        
    def __add__(self,other):
        if type(other) == int:
            x = [i for i in range(len(self.array))]
            for i in range(len(self.array)):
                x[i] = self.array[i] + other
        else:
            x = [i for i in range(len(other.array))]
            if len(self.array) == len(other.array):
                for i in range(len(other.array)):
                    x[i] = self.array[i] + other.array[i]
            else:
                raise ValueError('Arrays must be the same length.')   
        return x
    
    def __sub__(self,other):
        if type(other) == int:
            x = [i for i in range(len(self.array))]
            for i in range(len(self.array)):
                x[i] = self.array[i] - other
        else:
            x = [i for i in range(len(other.array))]
            if len(self.array) == len(other.array):
                for i in range(len(other.array)):
                    x[i] = self.array[i] - other.array[i]
            else:
                raise ValueError('Arrays must be the same length.')   
        return x
    
    def __mul__(self,other):
        if type(other) == int:
            x = [i for i in range(len(self.array))]
            for i in range(len(self.array)):
                x[i] = self.array[i] * other
        else:
            x = [i for i in range(len(other.array))]
            if len(self.array) == len(other.array):
                for i in range(len(other.array)):
                    x[i] = self.array[i] * other.array[i]
            else:
                raise ValueError('Arrays must be the same length.')   
        return x
    
    def __repr__(self):
        return repr(self.array)
    
    def __len__(self):
        return len(self.array)
    
    def __eq__(self, other):
        return self.array==other.array
     
    #最頻値       
    def Mode(self):
        _x = dict()
        for i in self.array:
            if i in _x:
                _x[i] += 1
            else:
                _x[i] = 1
        self.mode = [i[0] for i in [kv for kv in _x.items() if kv[1] == max(_x.values())]]
       
    #中央値     
    def Median(self):
        harf_len = (len(self.array)/2)
        if not harf_len.is_integer():
            self.median = self.array[int(harf_len-0.5)]
        else:
            self.median = (self.array[int(harf_len-1)]+self.array[int(harf_len-1)])/2
     
    #平均値        
    def Average(self):
        ave = 0
        for i in self.array:
            ave += i
        self.ave = ave/len(self.array)
    
    #範囲
    def range(self):
        return sorted(self.array)[-1]-sorted(self.array)[0]
    
    #listの追加
    def append(self,add_data):
        if isinstance(add_data,list):
            for i in add_data:
                self.array.append(i)
        elif isinstance(add_data, Array):
            for i in add_data.array:
                self.array.append(i)
        else:
            raise TypeError('Can append only pynaly.Array or list')
        self.Mode()
        self.Median()
        self.Average()
        
    #偏差
    def dist(self):
        s = 0
        for i in self.array:
            s += (self.ave-i)**2
        return s/len(self.array)
    
    #四分位Q1&Q3
    def quar(self):
        if len(self.array)/2 == 0:
            q1_list = self.array[int(len(self.array)/2)-1]
            q3_list = self.array[int(len(self.array)/2)]
        return (q1_list,q3_list)
    
    #偏差値
    def adjusted(x=None):
        if not x==None:
            x = int(input('Score'))
        return (x-self.ave)/self.dist()*100+50


class Matrix:
    def __init__(self):
        pass

    
#共分散
def covary(arg1, arg2):
    arg1_ave = arg1.ave
    arg2_ave = arg2.ave
    if not arg1.len() == arg2.len():
        raise SyntaxError('Arrays must be the same length.')
    Sxy = 0
    for i in range(arg1.len()):
        Sxy += (arg1_ave-arg1.array[i])*(arg2_ave-arg2.array[i])
    return Sxy/arg1.len()

#相関係数
def coeffy(arg1, arg2):
    return covary(arg1, arg2)/((arg1.dist()**0.5)*(arg2.dist()**0.5))

#ゼロ配列生成   
def zeroArray(arg):
    return Array([0 for i in range(arg)])

#イチ配列生成

def oneArray(arg):
    return Array([1 for i in range(arg)])

pi = 3.14169265358979
e = 2.71828182845904