#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    names = dir(hidden_4)
    names.sort()
    for w in names:
            if w.find('__') == -1:
                print("{}".format(w))
