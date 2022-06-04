# 斐波那契数列

"""
a[0] = 0                n = 0
a[1] = 1                n = 1
a[n] = a[n-1] + a[n-2]  n >= 2
"""


def fibs(n):
    result = [0, 1]
    for i in range(n - 2):
        result.append(result[-2] + result[-1])
    return result


lst = fibs(100)
print(lst)


# 参数收集

def test(n, *args):
    print('n=', n)
    print('args=', args)


def test2(n, **args):
    print('double(*)=', args)


test(1, 2, 3, 4)
test2(1, a=2, b=3)
