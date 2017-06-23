#!/usr/bin/env python
# -*- coding: utf-8 -*-
u'''
Tick-Tack-Toe 〜 横へな 2012.7.6
問題

三目並べ( tick-tack-toe )の手を入力とし、勝敗を出力する。

    先攻がo、後攻がx
    すでに打ってある場所に打った場合、反則負け
        x が反則をした場合、「Foul : o won.」と出力
    縦横斜めのいずれかで一列揃ったら、揃えた方の勝ち
        x が揃えた場合、「x won.」と出力
    9マス埋まっても揃わなかったら引き分け
        「Draw game.」と出力
    勝敗が決した後の手は無視する
    入力文字列は、先攻から順に打った位置を示す。盤上の位置と数の対応は下表を参照。
        入力文字列が「91593」の場合、「oが9の位置、xが1の位置、oが5の位置、xが9の位置→xの反則負け(最後の3は無視)」となる。
    以下の様なケースは考慮しなくてよい
        入力が 1〜9 以外の文字を含んでいる
        入力が不足していて、ゲームの勝敗が決まらない

入力と出力の例
#	入力		出力
1	79538246	x won.
2	35497162193	x won.
3	61978543	x won.
4	254961323121	x won.
5	6134278187	x won.
6	4319581		Foul : x won.
7	9625663381	Foul : x won.
8	7975662		Foul : x won.
9	2368799597	Foul : x won.
10	18652368566	Foul : x won.
11	965715		o won.
12	38745796	o won.
13	371929		o won.
14	758698769	o won.
15	42683953	o won.
16	618843927	Foul : o won.
17	36535224	Foul : o won.
18	882973		Foul : o won.
19	653675681	Foul : o won.
20	9729934662	Foul : o won.
21	972651483927	Draw game.
22	5439126787	Draw game.
23	142583697	Draw game.
24	42198637563	Draw game.
25	657391482	Draw game.
'''

test_inputs = [
    ("79538246",	"x won."),
    ("35497162193",	"x won."),
    ("61978543",	"x won."),
    ("254961323121",	"x won."),
    ("6134278187",	"x won."),
    ("4319581",		"Foul : x won."),
    ("9625663381",	"Foul : x won."),
    ("7975662",		"Foul : x won."),
    ("2368799597",	"Foul : x won."),
    ("18652368566",	"Foul : x won."),
    ("965715",		"o won."),
    ("38745796",	"o won."),
    ("371929",		"o won."),
    ("758698769",	"o won."),
    ("42683953",	"o won."),
    ("618843927",	"Foul : o won."),
    ("36535224",	"Foul : o won."),
    ("882973",		"Foul : o won."),
    ("653675681",	"Foul : o won."),
    ("9729934662",	"Foul : o won."),
    ("972651483927",	"Draw game."),
    ("5439126787",	"Draw game."),
    ("142583697",	"Draw game."),
    ("42198637563",	"Draw game."),
    ("657391482",	"Draw game."),
]


win_pattern = [
    {0, 1, 2}, {3, 4, 5}, {6, 7, 8},
    {0, 3, 6}, {1, 4, 7}, {2, 5, 8},
    {0, 4, 8}, {2, 4, 6},
]

player = ['o', 'x']


def win_debug(p):
    p_set = set(p)
    for w_set in win_pattern:
        print("p_set:{} w_set:{} (p_set&w_set):{}".format(p_set, w_set, (p_set & w_set)))
        if w_set == (p_set & w_set):
            return True
    return False


def solve_debug(input):
    board = [ 0 for x in range(9) ]
    input = [int(x)-1 for x in input]
    o_rec = input[::2]
    x_rec = input[1::2]
    print("{}: o:{}({}) x:{}({})".format(input, o_rec, len(o_rec), x_rec, len(x_rec)))

    msg = ""
    p = 0
    for i, a in enumerate(input):
        print(i, a)
        if board[a] == 1:
            msg = "Foul : {} won.".format(player[1 - p])
            break
        board[a] = 1
        if i >= 4:
            if win_debug(input[p:i+1:2]):
                msg = "{} won.".format(player[p])
                break
        p = 1 - p

        if i >= 8:
            msg = "Draw game."
            break

    else:
        msg = "Abort."

    print(i, msg)
    return msg


def win(p):
    return any(w == (set(p) & w) for w in win_pattern)

def solve(input):
    board = [ 0 for x in range(9) ]
    input = [int(x)-1 for x in input]

    p = 0
    for i, a in enumerate(input):
        if board[a] == 1:
            return "Foul : {} won.".format(player[1 - p])
        board[a] = 1
        if i >= 4:
            if win(input[p:i+1:2]):
                return "{} won.".format(player[p])
        if i >= 8:
            return "Draw game."

        p = 1 - p



def check(inp, result, ans):
    print("{:14}: result: {} ... {}".format(inp, result, "OK" if result == ans else "NG:" + ans))

# print (solve_debug(test_inputs[0][0]))

for inp, ans in test_inputs:
    check(inp, solve(inp), ans)


# Local Variables:
# python-indent: 4
# End:
