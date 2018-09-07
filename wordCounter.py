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
parser.add_argument("-a", metavar = "--CCBcount", dest = "ccb_arg", help = "Counts the number of lines of code, comment lines, blank lines in the file  or files in the directory")
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
        with open(fileName, "r", encoding = 'utf-8') as f:
            for line in f:
                match = re.findall(r'[\s]+', line)
                for i in match:
                    line = line.replace(i, '')
                charsCount += len(line)
        return charsCount
    except IOError:
        print("打开文件失败！请检查路径是否正确")

def WordCount(fileName):
    """
    统计单词数
    :param:
        fileName: 统计的文件
    :return: 单词的数量
    """
    wordsCount = 0
    try:
        with open(fileName, "r", encoding = 'utf-8') as f:
            for line in f:
                match = re.findall(r'[a-zA-Z-\']+',line)
                wordsCount += len(match)
        return wordsCount
    except IOError:
        print("文件打开失败！请检查路径是否正确")

def LineCount(fileName):
    """
    统计行数
    :param:
        fileName: 统计的文件
    :return: 单词的数量
    """
    linesCount = 0
    try:
        with open(fileName, "r", encoding = 'utf-8') as f:
            for line in f:
                linesCount += 1
        return linesCount
    except IOError:
        print("文件打开失败！请检查路径是否正确")

def RecurveDir(dirPath):
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
            fileList += RecurveDir(mPath)
        else:
            pass
    return fileList

def RecurveDirProcess(Path):
    """
    递归处理文件主函数
    :param
        Path: 输入的目录路径
    :return: None
    """
    fileList =  RecurveDir(Path)
    for file in fileList:
        #print(file)
        wordsCount = WordCount(file)
        linesCount = LineCount(file)
        charsCount = Char_Count(file)
        print("%s 文件信息：\n文本的字符数目：%s\n文本的单词数目：%s\n文本的行数：%s\n" % (file,charsCount,wordsCount,linesCount))

def CCBCountMain(fileName):
    """
    统计文本的代码行，空行，注释行主函数
    :param
        fileName：输入的文件
    :return: None
    """
    #支持的后缀
    suffixList = ['.py', '.c', '.java', '.js','.cpp']
    if os.path.isdir(fileName):
        fileList = RecurveDir(fileName)
        for file in fileList:
            suffix = os.path.splitext(file)[1]
            if suffix in suffixList: 
                CodeCommentBlankCount(file)
    else:
        CodeCommentBlankCount(file)	

def CodeCommentBlankCount(fileName):
    """
    统计文本的代码行，空行，注释行处理函数
    :param
        fileName：输入的文件
    :return: None
    """
    blankLines = 0
    commentLines = 0
    codeLines = 0 
    isComment = False
    startComment = 0
    try:
        with open(fileName, 'r', encoding = 'utf-8') as f:
            for index, line in enumerate(f, start=1):
                stripLine = line.strip()
                #判断多行注释是否开始
                if not isComment:
                    if stripLine.startswith("'''") or stripLine.startswith('"""') or stripLine.startswith('/*'):
                        isComment = True
                        startComment = index
                    #单行注释，考虑多种情况
                    elif stripLine.startswith('#') or stripLine.startswith('//') or re.findall('^[}]+[\s\S]+[//]+', stripLine):
                        commentLines += 1
                    elif stripLine == '' or stripLine == '{' or stripLine == '}':
                        blankLines += 1
                    else:
                        codeLines += 1
                #多行注释已经开始
                else:
                    if stripLine.endswith("'''") or stripLine.endswith('"""') or stripLine.endswith('*/'):
                        isComment = False
                        commentLines += index -startComment + 1 
                    else:
                        pass
        print("%s 文件信息：\n文本的代码行数：%s\n文本的空白行数：%s\n文本的注释行数：%s\n" % (fileName,codeLines,blankLines,commentLines))
    except IOError:
        print("文件打开失败！请检查文件路径是否正确")
    
if args.char_arg:
    charsCount = Char_Count(args.char_arg)
    print("文本的字符数目：%s" % (charsCount))
if args.word_arg:
    wordsCount = WordCount(args.word_arg)
    print("文本的单词数目：%s" % (wordsCount))
if args.line_arg:
    linesCount = LineCount(args.line_arg)
    print("文本的行数：%s" % (linesCount))
if args.recur_arg:
    RecurveDirProcess(args.recur_arg)
if args.ccb_arg:
    CCBCountMain(args.ccb_arg)