import hashlib
secret_key = open('input.txt').readline()
i = 0
while True:
    combined = '{}{}'.format(secret_key, i)
    encoded = combined.encode()
    hashed = hashlib.md5(encoded).hexdigest()
    if hashed[:6] == '000000':
        print(i)
        break
    i += 1
