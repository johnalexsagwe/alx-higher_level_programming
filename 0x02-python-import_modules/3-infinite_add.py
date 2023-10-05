#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    num_inputs = len(argv)
    results = 0

    for i in range(1, num_inputs):
        results += int(argv[i])
    print(results)
