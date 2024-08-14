import re
import sys

from commands.handlers_parser import handler_one_file_parser_min_info, handler_one_file_parser
from commands.print_help import print_help


def main():
    argv = str(sys.argv[1:])

    if re.findall("-h", argv):
        print_help()

    elif re.findall("-m", argv):
        handler_one_file_parser_min_info(argv)

    elif re.findall("-x", argv):
        handler_one_file_parser(argv)

    else:
        print_help()


if __name__ == "__main__":
    main()
