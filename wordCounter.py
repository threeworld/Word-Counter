# -*- coding: utf-8 -*-  

import re
import os
import glob
import fnmatch
import argparse

parser = argparse.ArgumentParser(description="this is wordCounter")
parser.add_argument("-c", metavar = "--char", dest = "char_arg", help = "return the number of characters" )
parser.add_argument("-w", metavar = "--word", dest = "word_arg", help = "return the number of words")
parser.add_argument("-l", metavar = "--line", dest = "line_arg", help = "return the number of lines")
parser.add_argument("-s", metavar = "--recurve", dest = "recur_arg", help = "Recursive file information under the directory")
args = parser.parse_args()

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
                match = re.findall(r'[a-zA-Z-\']+',line)
                wordsCount += len(match)
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

def Recurve_Dir(dirPath):
    """
    递归查找符合条件的文件
    :param: 
        dirPath: 目录的路径
    :return: 符合条件的文件
    """
    fileList = []
    pathFileInfo = "*.*"
    pathList = glob.glob(os.path.join(dirPath, '*'))
    for mPath in pathList:  
        if fnmatch.fnmatch(mPath, pathFileInfo):
            fileList.append(mPath)
            #print(fileList)
        elif os.path.isdir(mPath):
            #print(mPath)    
            fileList += Recurve_Dir(mPath)
        else:
            pass
    return fileList

def Recurve_Dir_Process(Path):
    fileList =  Recurve_Dir(Path)
    for file in fileList:
        #print(file)
        wordsCount = Word_Count(file)
        linesCount = Line_Count(file)
        charsCount = Char_Count(file)
        print("%s 文件信息：\n文本的字符数目：%s\n文本的单词数目：%s\n文本的行数：%s\n" % (file,charsCount,wordsCount,linesCount))


if args.char_arg:
    charsCount = Char_Count(args.char_arg)
    print("文本的字符数目：%s" % (charsCount))
if args.word_arg:
    wordsCount = Word_Count(args.word_arg)
    print("文本的单词数目：%s" % (wordsCount))
if args.line_arg:
    linesCount = Line_Count(args.line_arg)
    print("文本的行数：%s" % (linesCount))
if args.recur_arg:
    Recurve_Dir_Process(args.recur_arg)