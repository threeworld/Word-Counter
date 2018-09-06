# -*- coding: utf-8 -*-  

import re
import argparse

parser = argparse.ArgumentParser(description="this is wordCounter")
parser.add_argument("-c", metavar = "--char", dest = "char_arg", help = "return the number of characters" )
parser.add_argument("-w", metavar = "--word", dest = "word_arg", help = "return the number of words")
parser.add_argument("-l", metavar = "--line", dest = "line_arg", help = "return the number of lines")
args = parser.parse_args()
#print(args.char_arg)


def Char_Count(fileName):
    """
    统计字符数,不包括空白字符，包括空格、制表符、换页符等
    :param: 
        fileName: 统计的文件 
    :return: 字符的数量
    """
    charsCount = 0
    try:
        with open(fileName, "r") as f:
            for line in f:
                match = re.findall(r'[\s]+', line)
                for i in match:
                    line = line.replace(i, '')
                charsCount += len(line)
        return charsCount
    except IOError:
        print("打开文件失败！")

def Word_Count(fileName):
    """
    统计单词数
    :param:
        fileName: 统计的文件
    :return: 单词的数量
    """
    wordsCount = 0
    try:
        with open(fileName, "r") as f:
            for line in f:
                linesList = line.split()
                wordsCount += len(linesList)
        return wordsCount
    except IOError:
        print("文件打开失败！")

def Line_Count(fileName):
    """
    统计行数
    :param:
        fileName: 统计的文件
    :return: 单词的数量
    """
    linesCount = 0
    try:
        with open(fileName, "r") as f:
            for line in f:
                linesCount += 1
        return linesCount
    except IOError:
        print("文件打开失败！")

if args.char_arg:
    charsCount = Char_Count(args.char_arg)
    print("文本的字符数目：%s" % (charsCount))
if args.word_arg:
    wordsCount = Word_Count(args.word_arg)
    print("文本的单词数目：%s" % (wordsCount))
if args.line_arg:
    linesCount = Line_Count(args.line_arg)
    print("文本的行数：%s" % (linesCount))

