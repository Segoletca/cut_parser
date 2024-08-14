import re

from file_filter import file_filter
from one_file_parser import one_file_parser
from one_file_parser_min_info import one_file_parser_min_info


def handler_one_file_parser_min_info(argv: str):
    if re.findall("-c", argv):
        for file in file_filter():
            one_file_parser_min_info(file, create_one_file=True)
    else:
        for file in file_filter():
            one_file_parser_min_info(file, create_one_file=False)


def handler_one_file_parser(argv: str):
    if re.findall("-c", argv):
        for file in file_filter():
            one_file_parser(file, create_one_file=True)
    else:
        for file in file_filter():
            one_file_parser(file, create_one_file=False)
