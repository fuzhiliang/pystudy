#!/usr/bin/env python3
# by ysan

import re
import json

'''
    常用正则表达式符号

    '.'     默认匹配除\n之外的任意一个字符，若指定flag DOTALL,则匹配任意字符，包括换行
    '^'     匹配字符开头，若指定flags MULTILINE,这种也可以匹配上(r"^a","\nabc\neee",flags=re.MULTILINE)
    '$'     匹配字符结尾，或e.search("foo$","bfoo\nsdfsf",flags=re.MULTILINE).group()也可以
    '*'     匹配*号前的字符0次或多次，re.findall("ab*","cabb3abcbbac")  结果为['abb', 'ab', 'a']
    '+'     匹配前一个字符1次或多次，re.findall("ab+","ab+cd+abb+bba") 结果['ab', 'abb']
    '?'     匹配前一个字符1次或0次
    '{m}'   匹配前一个字符m次
    '{n,m}' 匹配前一个字符n到m次，re.findall("ab{1,3}","abb abc abbcbbb") 结果'abb', 'ab', 'abb']
    '|'     匹配|左或|右的字符，re.search("abc|ABC","ABCBabcCD").group() 结果'ABC'
    '(...)' 分组匹配，re.search("(abc){2}a(123|456)c", "abcabca456c").group() 结果 abcabca456c

     
    '\A'    只从字符开头匹配，re.search("\Aabc","alexabc") 是匹配不到的
    '\Z'    匹配字符结尾，同$
    '\d'    匹配数字0-9
    '\D'    匹配非数字
    '\w'    匹配[A-Za-z0-9]
    '\W'    匹配非[A-Za-z0-9]
    's'     匹配空白字符、\t、\n、\r , re.search("\s+","ab\tc1\n3").group() 结果 '\t'
    
    '(?P<name>...)' 分组匹配 re.search("(?P<province>[0-9]{4})(?P<city>[0-9]{2})(?P<birthday>[0-9]{4})","371481199306143242").groupdict("city") 结果{'province': '3714', 'city': '81', 'birthday': '1993'}
    
    re.I(re.IGNORECASE): 忽略大小写（括号内是完整写法，下同）
    M(MULTILINE): 多行模式，改变'^'和'$'的行为
    S(DOTALL): 点任意匹配模式，改变'.'的行为
'''

# 从头开始匹配
# re.match('^a', 'abdca')
# 匹配包含
# re.search()
# 把所有匹配到的字符放到以列表中的元素返回
# re.findall()
# 以匹配到的字符当做列表分隔符
# re.split()
# 匹配字符并替换
# re.sub()

s = "adfad asdfasdf asdfas asdfawef asd adsfas "
info = re.findall('(\w+)\s+\w+', s)
com = re.compile('(\w+)\s+\w+')
print(info)
print(com.findall(s))

ss = '1 - 2 * ((60-30 + (-40/(5+6) + (5 + 5)) * (9-2*5/3 + 7 / 3*99/4*2998 + 10 * 568/14)) - (-4*3) / (16-3*2))'
mul_div = re.compile('\d+\.*\d*[\*\/]+[\+\-]?\d+\.*\d*')
aa = mul_div.findall(ss)
print(aa)
print(mul_div.search(ss).group())

print("--------------------------------------04.02 测试一个正则---------------------------------------")

data = [{u'\u5E74\u7EA7'}]
print(data)
ii = "初中精品微课：英语七年级下册"
# pattern = "[\u4e00-\u9fa5]{1}?(?:年级)"
pattern = r'[\u5E74]+'
aa = r'[\u4e00-\u9fff]+'
print("pattern", pattern)
print("a ", aa)
com = re.compile(pattern)
com2 = re.compile(aa)
res = com.match(ii)
print(res)
res2 = com2.match(ii)
print(res2)
