hands = [{
    'type': 'rock',
    'value': 1,
    'beats': 'scissors'
}, {
    'type': 'paper',
    'value': 2,
    'beats': 'rock'
}, {
    'type': 'scissors',
    'value': 3,
    'beats': 'paper'
}]


def get_enemy_hand(symbol):
    if symbol == 'A':
        return hands[0]
    elif symbol == 'B':
        return hands[1]
    elif symbol == 'C':
        return hands[2]


def get_me_hand(symbol, enemy_hand):
    if symbol == 'X':  # lose
        return [x for x in hands if x.get('type') == enemy_hand.get('beats')][0]
    elif symbol == 'Y':  # draw
        return hands[hands.index(enemy_hand)]
    elif symbol == 'Z':  # win
        return [x for x in hands if x.get('beats') == enemy_hand.get('type')][0]


def get_round_score(hand1, hand2):
    if hand1.get('type') == hand2.get('type'):
        return 3
    elif hand2.get('type') == hand1.get('beats'):
        return 6
    return 0


score = 0
f = open('input.txt')
for line in f.readlines():
    [enemy, me] = line.replace('\n', '').split(' ')
    enemy_hand = get_enemy_hand(enemy)
    me_hand = get_me_hand(me, enemy_hand)

    score += me_hand.get('value') + get_round_score(me_hand, enemy_hand)
print(score)
