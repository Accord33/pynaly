import pynaly as pn

one = pn.Array([1,2,3])
two = pn.Array([4,5,6])
three = [7,8,9]
one.append(two)
one.append(three)
print(one)