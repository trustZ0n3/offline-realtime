#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
第一回 オフラインリアルタイムどう書くの参考問題
http://qiita.com/Nabetani/items/cbc3af152ee3f50a822f

ポーカー

5枚のカードを示す文字列を入力とし、ポーカーの役を出力せよ。
ただし:

 - 一枚のカードは、スートを表す文字＋ランクを表す文字列 で構成される。
 - スートを表す文字は、S, H, D, C のいずれか
 - ランクを表す文字列は、2, 3, ..., 9, 10, J, Q, K, A のいずれか
 - 下表の役に対応すること。下表の役に該当しない場合は '--' を出力すること。
 - カードはジョーカーを含まない52枚から5枚が選ばれる。
 - 不正な入力への対応は不要。

対応すべき役と、その役だった場合に出力する文字列は以下のとおり：

    フォーカード : 4K
    フルハウス : FH
    スリーカード : 3K
    ツーペア : 2P
    ワンペア : 1P
    上記のいずれにも該当しない : --

'''

import re, itertools
from collections import Counter

test_inputs = [
    ("D3C3C10D10S3",  "FH"),
    ("S8D10HJS10CJ",  "2P"),
    ("DASAD10CAHA",   "4K"),
    ("S10HAD10DAC10", "FH"),
    ("S3S4H3D3DA",    "3K"),
    ("SASJDACJS10",   "2P"),
    ("CKH10D10H3HJ",  "1P"),
    ("S3SJDAC10SQ",   "--"),
]

hands = { '11111':'--',
          '1112': '1P',
          '122':  '2P',
          '113':  '3K',
          '23':   'FH',
          '14':   '4K',
}

def solve(card_str):
    return hands[''.join(sorted([str(len(list(v))) for k, v in itertools.groupby(sorted(re.split('[SHDC]', card_str)[1:]))]))]


for card_str, ans in test_inputs:
    ret = solve(card_str)
    print('{:15} => ret:{} ans:{} ... {}'.format(card_str, ret, ans, 'OK' if ret == ans else 'NG'))


''' 参考
https://yhpg.doorkeeper.jp/

https://atnd.org/events/30285

'''


# Local Variables:
# tab-width: 4
# End:
