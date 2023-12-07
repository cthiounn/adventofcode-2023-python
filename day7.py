import re
import functools
from collections import Counter
with open('data/my_input/7.in') as f:
    lines = f.read().split("\n")


dict_values={"A":14,"K":13,"Q":12,"J":11,"T":10}

dict_values2={"A":14,"K":13,"Q":12,"J":1,"T":10}


def values_card(card):
    if card.isdigit():
        return int(card)
    else:
        return dict_values2[card]

def most_common_best_card(hand):
    counter=Counter(hand)
    max_card=max(counter.values())

    return sorted([card for card in counter if counter[card]==max_card],key=values_card)[0]

def value_hands_poker_with_counter_with_joker(hand):
    counter=Counter(hand)
    if "J" in counter:
        if len(counter)==1:
            return [8,"A"]
        else:
            return value_hands_poker_with_counter(hand.replace("J",most_common_best_card(hand.replace("J",""))))
    else:
        return value_hands_poker_with_counter(hand)

def value_hands_poker_with_counter(hand):
    counter=Counter(hand)
    if len(counter)==1:
        return [8,counter.most_common()[0][0]]
    elif len(counter)==2:
        if counter.most_common()[0][1]==4:
            return [7,counter.most_common()[0][0]]
        else:
            return [6,counter.most_common()[0][0]]
    elif len(counter)==3:
        if counter.most_common()[0][1]==3:
            return [3,counter.most_common()[0][0]]
        else:
            return [2,counter.most_common()[0][0]]
    elif len(counter)==4:
        return [1,counter.most_common()[0][0]]
    else:
        return [0,counter.most_common()[0][0]]


def compare_hands(hand1, hand2):
    if value_hands_poker_with_counter(hand1)[0]>value_hands_poker_with_counter(hand2)[0]:
        return 1
    elif value_hands_poker_with_counter(hand1)[0]<value_hands_poker_with_counter(hand2)[0]:
        return -1
    else:
        for i,card in enumerate(hand1):
            card2=hand2[i]
            if card!=card2:
                card = int(card) if card.isdigit() else dict_values[card]
                card2 = int(card2) if card2.isdigit() else dict_values[card2]
                if card>card2:
                    return 1
                else:
                    return -1
        return 0


def compare_hands2(hand1, hand2):
    if value_hands_poker_with_counter_with_joker(hand1)[0]>value_hands_poker_with_counter_with_joker(hand2)[0]:
        return 1
    elif value_hands_poker_with_counter_with_joker(hand1)[0]<value_hands_poker_with_counter_with_joker(hand2)[0]:
        return -1
    else:
        for i,card in enumerate(hand1):
            card2=hand2[i]
            if card!=card2:
                card = int(card) if card.isdigit() else dict_values2[card]
                card2 = int(card2) if card2.isdigit() else dict_values2[card2]
                if card>card2:
                    return 1
                else:
                    return -1
        return 0        

def part1(vlines):
    dict_hands={line.split(" ")[0]:int(line.split(" ")[1]) for line in vlines   }
    list_hands=sorted(dict_hands.keys(),key=functools.cmp_to_key(compare_hands))
    return sum([(i+1)*dict_hands[hand] for i,hand in enumerate(list_hands)])


def part2(vlines):
    dict_hands={line.split(" ")[0]:int(line.split(" ")[1]) for line in vlines   }
    list_hands=sorted(dict_hands.keys(),key=functools.cmp_to_key(compare_hands2))
    return sum([(i+1)*dict_hands[hand] for i,hand in enumerate(list_hands)])

print(part1(lines))
print(part2(lines))