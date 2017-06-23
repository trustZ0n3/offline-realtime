#!/usr/bin/env python
# -*- coding: utf-8 -*-
u'''
Bit Tetris 〜 横へな 2012.7.25
http://nabetani.sakura.ne.jp/hena/ord2/

問題

ブロックが落ちたあとのテトリスフィールドから、横一列揃っている列を削除する。

フィールドの幅は可変。高さは8。

入力は「 ff-2f-23-f3-77-7f-3b 」のような形式。ハイフン区切りで二桁ずつの16進数となっている。
LSB(つまり、2進数の1の位)が下、MSB(つまり、2進数の大きな桁)が上のブロックを意味する。
したがって、この入力は下図のようなフィールドを意味する。

|■|　|　|■|　|　|　|
|■|　|　|■|■|■|　|
|■|■|■|■|■|■|■|
|■|　|　|■|■|■|■|
|■|■|　|　|　|■|■|
|■|■|　|　|■|■|　|
|■|■|■|■|■|■|■|
|■|■|■|■|■|■|■|
 ff 2f 23 f3 77 7f 3b

見ての通り、下から数えて 1段目、2段目、6段目 が1列揃っているので、これを消す。 消した結果は下図のようになる：
  	  	  	  	  	  	 
|　|　|　|　|　|　|　|
|　|　|　|　|　|　|　|
|　|　|　|　|　|　|　|
|■|　|　|■|　|　|　|
|■|　|　|■|■|■|　|
|■|　|　|■|■|■|■|
|■|■|　|　|　|■|■|
|■|■|　|　|■|■|　|
 1f 03 00 1c 0d 0f 06

というわけで、出力すべきは 1f-03-00-1c-0d-0f-06 という文字列となる。
'''

test_inputs = [
    ("ff-2f-23-f3-77-7f-3b", "1f-03-00-1c-0d-0f-06" ),
    ("01", "00" ),
    ("00", "00" ),
    ("7a-4e", "0c-02" ),
    ("56-b6", "08-14" ),
    ("12-12-12", "00-00-00" ),
    ("de-ff-7b", "0a-0f-05" ),
    ("95-be-d0", "05-1e-20" ),
    ("7c-b0-bb", "1c-20-2b" ),
    ("7a-b6-31-6a", "3a-56-11-2a" ),
    ("32-0e-23-82", "18-06-11-40" ),
    ("ff-7f-bf-df-ef", "0f-07-0b-0d-0e" ),
    ("75-df-dc-6e-42", "35-5f-5c-2e-02" ),
    ("62-51-ef-c7-f8", "22-11-6f-47-78" ),
    ("0c-47-8e-dd-5d-17", "04-23-46-6d-2d-0b" ),
    ("aa-58-5b-6d-9f-1f", "52-28-2b-35-4f-0f" ),
    ("ff-55-d5-75-5d-57", "0f-00-08-04-02-01" ),
    ("fe-fd-fb-f7-ef-df-bf", "7e-7d-7b-77-6f-5f-3f" ),
    ("fd-fb-f7-ef-df-bf-7f", "7e-7d-7b-77-6f-5f-3f" ),
    ("d9-15-b5-d7-1b-9f-de", "69-05-55-67-0b-4f-6e" ),
    ("38-15-fd-50-10-96-ba", "18-05-7d-20-00-46-5a" ),
    ("fe-fd-fb-f7-ef-df-bf-7f", "fe-fd-fb-f7-ef-df-bf-7f" ),
]

def solve_debug(input):
    rhex = input.split('-')
    #print(rhex)
    #rbits = list(map(lambda x: format(int(x, 16), '08b'), rhex))
    rbits = [format(int(x, 16), '08b') for x in rhex] # rows of bits
    print(rbits)
    ibits = [''.join(x) for x in zip(*rbits)] # inverse of rows of bits
    print(ibits)
    new_ibits = [b for b in ibits if not all([x=='1' for x in b])]
    print(new_ibits)
    for i in range(len(ibits) - len(new_ibits)):
        new_ibits.insert(0, '0'*len(ibits[0]))
    print(new_ibits)
    new_rbits = [''.join(x) for x in zip(*new_ibits)]
    print(new_rbits)
    new_rhex = [format(int(x, 2), '02x') for x in new_rbits]
    print(new_rhex)
    return '-'.join(new_rhex)



def solve(input):
    rbits = [format(int(x, 16), '08b') for x in input.split('-')] # rows of bits
    ibits = [''.join(x) for x in zip(*rbits)] # inverse of rows of bits
    new_ibits = [b for b in ibits if not all([x=='1' for x in b])]
    for i in range(len(ibits) - len(new_ibits)):
        new_ibits.insert(0, '0'*len(ibits[0]))
    new_rbits = [''.join(x) for x in zip(*new_ibits)]
    return '-'.join([format(int(x, 2), '02x') for x in new_rbits])


def check(inp, result, ans):
    print("{}: result:{} ... {}".format(inp, result, "OK" if result == ans else "NG:" + ans))

# print (solve_debug(test_inputs[0][0]))

for inp, ans in test_inputs:
    check(inp, solve(inp), ans)


# Local Variables:
# python-indent: 4
# End:
