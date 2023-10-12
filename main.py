#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author: iami233
# @date: 2023-10-12
# @version: 1.1
# @description: Convert base64 images in a Markdown file to PNG images

import re
import os
import sys
import base64
import argparse

def read_base64_images(filename):
    img_list = []
    try:
        with open(filename, 'r', encoding='utf8') as fin:
            for line in fin:
                data = re.findall(r'base64,(.*)\)', line)
                if data:
                    img_list.append(data[0])
        return img_list
    except IOError as err:
        print(f"File Error: {err}")

def download_images(img_list, directory):
    try:
        if not os.path.exists(directory):
            os.mkdir(directory)
        os.chdir(directory)
        for i, img_data in enumerate(img_list):
            with open(f'{i}.png', 'wb') as fout:
                fout.write(base64.b64decode(img_data))
        print("Download Success!")
        os.chdir('..')
    except Exception as e:
        print(f"Download Error: {e}")


def update_markdown_file(filename, directory):
    try:
        num = 0
        with open(filename, 'r', encoding='utf8') as fin, open('new.md', 'w', encoding='utf8') as fout:
            for line in fin:
                data = re.findall(r'base64,(.*)\)', line)
                if data:
                    line = re.sub(r'!\[(.*?)\]\((.*?)\)', f'![{num}](./{directory}/{num}.png)', line)
                    num += 1
                fout.write(line)
        print("Write Success!")
        os.rename(filename, f"{filename}.bak")
        os.rename('new.md', filename)
    except Exception as e:
        print(f"Write Error: {e}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert base64 images in a Markdown file to PNG images.')
    parser.add_argument('file', help='Input Markdown file')
    args = parser.parse_args()
    input_filename = args.file
    directory_name = 'images'

    img_list = read_base64_images(input_filename)
    download_images(img_list, directory_name)
    update_markdown_file(input_filename, directory_name)
