#!/usr/bin/env python
# -*- coding: utf-8 -*-
u'''
第2回 オフラインリアルタイムどう書くの参考問題
http://qiita.com/Nabetani/items/9d80de41903775296ca6

二値画像の回転

正方形の二値画像を時計回りに回転する。

画像フォーマットは、x:d　のようになっており、x が画像の一辺の長さ（常に正方形）、d は16進表記の画像データ。

例えば、"3:5b8" であれば、3が一辺の長さを表す。
5b8 は ２進数で 0101 1011 1000 となる。
3x3 の画像なので必要なのは 9bit。右端の 3bit を捨ててから三桁ずつに分けて

    010
    110
    111

となる。これが回転前の画像。
これを時計回りに 90度回すと

    110
    111
    100

となる。一列に並べて、16進表記用に末尾に 0 を3つ足すと、

    1101 1110 0000

となるので、もとめる答えは "3:de0" となる。
というのが今回のお題。
ただし：

    : の前にあるのは10進数。
    不正な入力への対処は不要。
    余ったから捨てる bit はゼロとは限らないが、回転後に末尾に足す bit はゼロ。
    少なくとも 9x9 の画像に対処できること。

'''

test_inputs = [
    ("3:5b8",	"3:de0"),
    ("1:8",	"1:8"),
    ("2:8",	"2:4"),
    ("2:4",	"2:1"),
    ("2:1",	"2:2"),
    ("3:5d0",	"3:5d0"),
    ("4:1234",	"4:0865"),
    ("5:22a2a20",	"5:22a2a20"),
    ("5:1234567",	"5:25b0540"),
    ("6:123456789",	"6:09cc196a6"),
    ("7:123456789abcd",	"7:f1a206734b258"),
    ("7:fffffffffffff",	"7:ffffffffffff8"),
    ("7:fdfbf7efdfbf0",	"7:ffffffffffc00"),
    ("8:123456789abcdef1",	"8:f0ccaaff78665580"),
    ("9:112233445566778899aab",	"9:b23da9011d22daf005d40"),
]



def solve_debug(input):
    x, d = input.split(':')
    x = int(x)
    d = [int(n, 16) for n in d]
    print(x, d)
    bits =''.join([format(n, '04b') for n in d])[:x*x]
    print(bits)
    bits = [bits[i:i+x] for i in range(0, len(bits), x)]
    print(bits)
    bits_inv = ''.join([''.join(list(reversed(n))) for n in zip(*bits)])
    print(bits_inv)
    mod = x*x % 4
    rest = 4 - mod if mod > 0 else 0
    bits_inv = bits_inv.ljust(x*x + rest, '0')
    print(bits_inv)
    d_inv = [bits_inv[i:i+4] for i in range(0, len(bits_inv), 4)]
    d_inv = ''.join(["{:x}".format(int(n, base=2)) for n in d_inv])
    print(d_inv)
    return "{}:{}".format(x, d_inv)


def solve(input):
    x, d = input.split(':')
    x = int(x)
    d = [int(n, 16) for n in d]

    bits =''.join([format(n, '04b') for n in d])[:x*x]
    bits = [bits[i:i+x] for i in range(0, len(bits), x)]

    bits_inv = ''.join([''.join(list(reversed(n))) for n in zip(*bits)])

    mod = x*x % 4
    rest = 4 - mod if mod > 0 else 0
    bits_inv = bits_inv.ljust(x*x + rest, '0')

    d_inv = [bits_inv[i:i+4] for i in range(0, len(bits_inv), 4)]
    d_inv = ''.join(["{:x}".format(int(n, base=2)) for n in d_inv])
    return "{}:{}".format(x, d_inv)


def check(inp, result, ans):
    print("{:14}: result: {} ... {}".format(inp, result, "OK" if result == ans else "NG:" + ans))

#print (solve_debug(test_inputs[0][0]))

for inp, ans in test_inputs:
    #check(inp, solve_debug(inp), ans)
    check(inp, solve(inp), ans)


# Local Variables:
# python-indent: 4
# End:
