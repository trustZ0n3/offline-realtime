#!/usr/bin/env python
# -*- coding: utf-8 -*-
u'''
第3回 オフラインリアルタイムどう書くの参考問題
http://qiita.com/Nabetani/items/ebd8a56b41711ba459f9

野球のボールカウント・アウトカウントの遷移を計算する。（得点・ランナー・イニング の計算は不要）
ただし、ストライク・ボール・ファウル・ヒット・ピッチャーフライしかない。
細かいルールは下記の通り：

    ストライクが３つになったらアウトが増え、ストライクとボールがゼロになる。
    ボールが4つになったらフォアボールになり、ストライクとボールがゼロになる。アウトは増えない。
    ヒットを打ったらストライクとボールがゼロになる。アウトは増えない。
    ピッチャーフライを打ったらストライクとボールがゼロになり、アウトが増える。
    アウトが3つになったら、アウト・ストライク・ボール全てゼロになる。
    ファウルの場合、もともとストライクが1以下の場合はストライクが増え、ストライクが2の場合には変化なし。
    入力は "sbsfbhsshssbbffbbssbs" のように、ひとつながりの文字列として与えられる。
    s, b, f, h, p がそれぞれ ストライク、ボール、ファウル、ヒット、ピッチャーフライ を意味する。
    出力は、アウト・ストライク・ボールの順にカウントをつなげたものをコンマで区切る。例を参照。
    不正入力には対処しなくてよい。
    最終回を超えることも考慮しなくてよい。
'''

test_inputs = [
    ("s", "010"),
    ("sss", "010,020,100"),
    ("bbbb", "001,002,003,000"),
    ("ssbbbb", "010,020,021,022,023,000"),
    ("hsbhfhbh", "000,010,011,000,010,000,001,000"),
    ("psbpfpbp", "100,110,111,200,210,000,001,100"),
    ("ppp", "100,200,000"),
    ("ffffs", "010,020,020,020,100"),
    ("ssspfffs", "010,020,100,200,210,220,220,000"),
    ("bbbsfbppp", "001,002,003,013,023,000,100,200,000"),
    ("sssbbbbsbhsbppp", "010,020,100,101,102,103,100,110,111,100,110,111,200,000,100"),
    ("ssffpffssp", "010,020,020,020,100,110,120,200,210,000"),
]


import copy

class Count:
    def __init__(self):
        self.o, self.s, self.b = 0, 0, 0

    def __repr__(self):
        return "".join(map(str, [self.o, self.s, self.b]))

    def strike(self):
        self.s += 1
        if self.s == 3:
            self.out()

    def ball(self):
        self.b += 1
        if self.b == 4:
            self.s = self.b = 0

    def foul(self):
        if self.s < 2:
            self.strike()

    def hit(self):
        self.s = self.b = 0

    def pitch(self):
        self.out()

    def out(self):
        self.o += 1
        if self.o == 3:
            self.o = 0
        self.s = self.b = 0

def solve(q):
    hist = []
    count = Count()
    for i in q:
        if i == 's':
            count.strike()
        if i == 'b':
            count.ball()
        if i == 'h':
            count.hit()
        if i == 'f':
            count.foul()
        if i == 'p':
            count.pitch()

        hist.append(str(count))
    return ",".join(hist)


def check(q, result, ans):
    print("{:16}: result: {} ... {}".format(q, result, "OK" if result == ans else "NG:" + ans))

for q, ans in test_inputs:
    check(q, solve(q), ans)


# Local Variables:
# python-indent: 4
# End:
