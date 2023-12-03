#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    sorted_names = dir(hidden_4)
    for name in sorted_names:
        if name[:2]!= "__":
            print(name)
