import re


class Day4:
    rooms = []

    def __init__(self):
        for line in [x.rstrip() for x in open('input.txt')]:
            result = re.search(r'([a-z]+.*)-(\d+)\[(\w+)]', line)
            name = ''.join(result.groups(1)[0].split('-'))
            sector = int(result.group(2))
            checksum = result.group(3)

            self.rooms.append({
                'hash': name,
                'sector': sector,
                'checksum': checksum
            })

    def solve(self):
        real_rooms = []
        for room in self.rooms:
            if self.is_real_room(room):
                real_rooms.append(room)

        for room in real_rooms:
            name = self.decrypt(room['hash'], room['sector'])
            if 'northpole' in name:
                print(room)

    def is_real_room(self, room):
        uniques = list(set(room['hash']))
        counts = {x: room['hash'].count(x) * -1 for x in uniques}
        counts = sorted(counts.items(), key=lambda item: (item[1], item[0]))
        top5 = [x[0] for x in counts[:5]]
        for c in top5:
            if c not in room['checksum']:
                return False
        return True

    def decrypt(self, cypher, shift):
        decrypted = ''
        shift %= 26
        for c in cypher:
            x = ord(c) + shift
            if x > ord('z'):
                x = ord('a') + (x - ord('z')) - 1
            decrypted += chr(x)
        return decrypted


if __name__ == '__main__':
    Day4().solve()
