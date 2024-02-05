# coding: [utf8]

import sys

def main():
    fn = sys.argv[1]
    with open(fn) as f:
        d = f.read()
    print(d)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(-1)
    main()
