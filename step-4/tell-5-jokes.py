#!/usr/local/bin/python3
# tell-5-adult-jokes.py
from pyjokes import get_joke

if __name__ == '__main__':
    import sys
    for i in range(1,6):
        print(get_joke(language=sys.argv[1], category='neutral'))
