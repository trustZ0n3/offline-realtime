#!/usr/bin/env python
# -*- coding: utf-8 -*-
u'''
Y字路巡り 〜 横へな 2012.9.7
http://nabetani.sakura.ne.jp/hena/ord3ynode/

問題

下図の通りの地図がある。
BからAへ向かう道の途中からスタート。
Y字路に到達するたびに、入力文字列の指示に従って右折/左折/後戻り のいずれかを選択する。
通過したY字路名前を順に出力せよ。

┌───Ｄ───┐
│　　　│　　　│
│　　　Ａ　　　│
│　　／　＼　　│
│　Ｂ───Ｃ　│
│／　　　　　＼│
Ｅ───────Ｆ

 入力は「rrllbrbl」のような形式。各文字の意味は下記の通り：

    r : 右へ曲がる
    l : 左へ曲がる
    b : 元に戻る

例えば入力データが「rbrl」の場合。

    B→A と進むところからスタート。
    A に着いたら右に曲がるので、Cへ向かう。
    C に着いたらAに戻る。
    再び A に着いたら 右に曲がるので、Dへ向かう。
    Dに着いたら 左に曲がるので、Eへ向かう。
    E に着いたらそれ以上指示がないので終了。
    たどった Y字路は順に、「ACADE」となるので、これを出力する。


'''

test_inputs = [
    ("b", "AB"),
    ("l", "AD"),
    ("r", "AC"),
    ("bbb", "ABAB"),
    ("rrr", "ACBA"),
    ("blll", "ABCAB"),
    ("llll", "ADEBA"),
    ("rbrl", "ACADE"),
    ("brrrr", "ABEDAB"),
    ("llrrr", "ADEFDE"),
    ("lrlll", "ADFEDF"),
    ("lrrrr", "ADFCAD"),
    ("rllll", "ACFDAC"),
    ("blrrrr", "ABCFEBC"),
    ("brllll", "ABEFCBE"),
    ("bbrllrrr", "ABACFDEFD"),
    ("rrrrblll", "ACBACABCA"),
    ("llrlrrbrb", "ADEFCADABA"),
    ("rrrbrllrr", "ACBABEFCAD"),
    ("llrllblrll", "ADEFCBCADEB"),
    ("lrrlllrbrl", "ADFCBEFDFCB"),
    ("lllrbrrlbrl", "ADEBCBACFCAB"),
    ("rrrrrrlrbrl", "ACBACBADFDEB"),
    ("lbrbbrbrbbrr", "ADABABEBCBCFE"),
    ("rrrrlbrblllr", "ACBACFCACFDAB"),
    ("lbbrblrlrlbll", "ADADFDABCFDFED"),
    ("rrbbrlrlrblrl", "ACBCBADFEBEFDA"),
    ("blrllblbrrrrll", "ABCFDADEDABEDFE"),
    ("blrllrlbllrrbr", "ABCFDABCBEFDEDA"),
    ("lbrbbrllllrblrr", "ADABABEFCBEDEBCF"),
    ("rrrrbllrlrbrbrr", "ACBACABCFDEDADFC"),
]

direction = {'b': 0, 'l': 1, 'r': 2}
graph = {
    'A': ['B', 'D', 'C'],
    'B': ['A', 'C', 'E'],
    'C': ['A', 'F', 'B'],
    'D': ['A', 'E', 'F'],
    'E': ['B', 'F', 'D'],
    'F': ['C', 'D', 'E'],
}

def solve(q):
    result = []
    before = 'B'
    current = 'A'

    result.append(current)
    for i in q:
        g = graph[current]
        idx = g.index(before)
        nextidx = (idx + direction[i]) % 3
        # print("{}-> {}:{}({},{})=> {}".format(before, current, i, idx, nexti, g[nextidx]))
        current, before = g[nextidx], current
        result.append(current)

    return ''.join(result)


def check(q, result, ans):
    print("{:15}: result:{} ... {}".format(q, result, "OK" if result == ans else "NG:" + ans))

for q, ans in test_inputs:
    check(q, solve(q), ans)


# Local Variables:
# python-indent: 4
# End:
