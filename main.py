#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author: iami233
# @date: 2022-03-15
# @version: 1.0
# @description: 将石墨文档md文件中的base64图片转换为png图片

import re
import os
import sys
import base64

fileName = sys.argv[1]
dirName = fileName.split('.')[0]
imgList = []

def readFile(fileName):
    try:
        with open(fileName,'r',encoding='utf8') as fin:

            for line in fin.readlines():
                line = line.strip('\n')
                data = re.findall(r'base64,(.*)\)',line)
                if data:
                    imgList.append(data[0])
                else:
                    continue
        return imgList
    except IOError as err:
        print("File Error:"+str(err))

def downloadImg(imgList,dirName):
    try:
        os.mkdir(dirName)
        os.chdir(dirName)
        for i in range(len(imgList)):
            with open(str(i)+'.png','wb') as fout:
                fout.write(base64.b64decode(imgList[i]))
        print("Download Success!")
        os.chdir('..')
    except:
        pass

def writeFile(fileName,dirName):
    num = 0
    try:
        with open(fileName,'r',encoding='utf8') as fin:
            try:
                with open('new.md','w',encoding='utf8') as fout:
                    for line in fin.readlines():
                        line = line.strip('\n')
                        data = re.findall(r'base64,(.*)\)',line)
                        if data:
                            line = re.sub(r'!\[(.*?)\]\((.*?)\)','!['+ str(num) +'](./'+ dirName +'/'+ str(num) +'.png)',line)
                            num += 1
                        fout.write(line+'\n')
                print("Write Success!")
            except IOError as err:
                print("File Error:"+str(err))
        os.rename(fileName,fileName+'.bak')
        os.rename('new.md',fileName)
    except:
        pass
        
if __name__ == '__main__':
    downloadImg(readFile(fileName),dirName)
    writeFile(fileName, dirName)
