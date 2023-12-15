def main():
    sequences = open('input.txt').readline().strip().split(',')
    total = 0
    for sequence in sequences:
        hash_val = 0
        for char in sequence:
            hash_val += ord(char)
            hash_val *= 17
            hash_val %= 256
        total += hash_val
    print(total)


if __name__ == '__main__':
    main()
