import bisect
from collections import Counter

class Hand:
    def __init__(self, cards, bid):
        self.cards = cards
        self.bid_amnt = bid
        self.hand_type = Hand.get_hand_type(cards)

    @staticmethod
    def get_hand_type(cards):
        c = Counter(cards)
        label_cnt = len(c)
        if label_cnt == 1:
            return 7  # five of a kind
        if label_cnt == 2:
            vals = c.values()
            if 4 in vals:
                # J J J J 5 vs J 5 5 5 5
                if 'J' in cards:
                    return 7  # five of a kind
                else:
                    return 6  # four of a kind
            else:
                # J J J 4 4 vs J J 4 4 4
                if 'J' in cards:
                    return 7  # five of a kind
                else:
                    return 5  # full house
        elif label_cnt == 3:
            vals = c.values()
            # J 3 4 4 4 vs J 3 3 4 4 vs J J 3 3 4 vs J J J 3 4
            if 'J' in cards:
                if c.get('J') == 3 or c.get('J') == 2:
                    return 6  # four of a kind
                else:  # there must be 1 'J'
                    if 3 in vals:
                        return 6  # four of a kind
                    else:
                        return 5  # full house
            else:
                if 3 in vals:
                    return 4  # three of a kind
                else:
                    return 3  # two pair
        elif label_cnt == 4:
            if 'J' in cards:
                # J J 3 5 6   vs  3 3 5 6 J
                return 4  # three of a kind
            else:
                return 2  # one pair
        elif label_cnt == 5:
            if 'J' in cards:
                return 2  # one pair
            else:
                return 1  # high card

    @staticmethod
    def convert_card(card):
        if card.isdigit():
            return int(card)
        if card == 'T':
            return 10
        elif card == 'J':
            return 0  # now the weakest
        elif card =='Q':
            return 12
        elif card == 'K':
            return 13
        else:
            return 14

    def __lt__(self, other):
        if self.hand_type == other.hand_type:
            i = 0
            while i < 5:
                if self.cards[i] == other.cards[i]:
                    i += 1
                    continue
                card1 = Hand.convert_card(self.cards[i])
                card2 = Hand.convert_card(other.cards[i])
                return card1 < card2
        else:
            return self.hand_type < other.hand_type

        raise Exception  # two hands should never be exactly the same??


def solve():
    # get list of all hands sorted by their strength
    sorted_hands = []
    with open("input.txt", "r") as f:
        for line in f:
            parsed_line = line.rstrip().split()
            hand = Hand(cards=list(parsed_line[0]), bid=int(parsed_line[1]))
            bisect.insort(sorted_hands, hand)

    for h in sorted_hands:
        print(f'Cards {h.cards} with type {h.hand_type} and bid {h.bid_amnt}')

    # determine total winnings
    total_winnings = 0
    for i in range(0, len(sorted_hands)):
        bid = sorted_hands[i].bid_amnt
        rank = i + 1
        total_winnings += (rank * bid)

    return total_winnings

if __name__ == "__main__":
    answer = solve()
    print(answer)


# wrong: 249610219 (too high)
# wrong: 249345525 (too high)
# 249138943
