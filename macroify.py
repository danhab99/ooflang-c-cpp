import sys
import os
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Replaces the tokens in your C/C++ project with macros that decrease readibility')
    parser.add_argument('-f --file', nargs='+',
                        help='File(s) to process', required=True)
    parser.add_argument('-p --process-dependencies',
                        help='Process dependencies listed in each C/C++ file', action='store_true')
    # parser.add_argument('')
    args = parser.parse_args()
