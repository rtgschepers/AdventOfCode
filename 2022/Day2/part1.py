def get_hand(symbol):
    if symbol in ['A', 'X']:
        return {
            'type': 'rock',
            'value': 1,
            'beats': ['scissors']
        }
    elif symbol in ['B', 'Y']:
        return {
            'type': 'paper',
            'value': 2,
            'beats': ['rock']
        }
    elif symbol in ['C', 'Z']:
        return {
            'type': 'scissors',
            'value': 3,
            'beats': ['paper']
        }


def get_round_score(hand1, hand2):
    if hand1.get('type') == hand2.get('type'):
        return 3
    elif hand2.get('type') in hand1.get('beats'):
        return 6
    return 0


score = 0
f = open('input.txt')
for line in f.readlines():
    [enemy, me] = line.replace('\n', '').split(' ')
    enemy_hand = get_hand(enemy)
    me_hand = get_hand(me)

    score += me_hand.get('value') + get_round_score(me_hand, enemy_hand)
print(score)
