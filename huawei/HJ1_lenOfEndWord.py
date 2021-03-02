"""
华为机试
HJ1 字符串最后一个单词长度
题目描述
计算字符串最后一个单词的长度，单词以空格隔开。

输入描述:
输入一行，代表要计算的字符串，非空，长度小于5000。

输出描述:
输出一个整数，表示输入字符串最后一个单词的长度。
"""

word = input().split(" ")
words = [word[i] for i in range(len(word)) if word[i] != ""]
print(len(words[-1]))
