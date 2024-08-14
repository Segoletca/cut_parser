import os
import re


def file_filter(path="./raw_logs/") -> list:
    files = []
    for file in os.listdir(path):
        if re.findall("log", file):
            files += [path + file]
    return files
