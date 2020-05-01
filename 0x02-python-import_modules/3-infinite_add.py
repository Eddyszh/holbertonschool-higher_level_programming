#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    for i in sys.argv[1:]:
        if i.isdigit() == False:
            sys.exit("All the arguments must be integers")
    num = [int(i) for i in sys.argv[1:]]
    sum = sum(num)
    print("{:d}".format(sum))
