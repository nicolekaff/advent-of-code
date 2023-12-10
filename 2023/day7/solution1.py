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
        elif label_cnt == 2:
            vals = c.values()
            if 4 in vals:
                return 6  # four of a kind
            else:
                return 5  # full house
        elif label_cnt == 3:
            vals = c.values()
            if 3 in vals:
                return 4  # three of a kind
            else:
                return 3  # two pair
        elif label_cnt == 4:
            return 2  # one pair
        elif label_cnt == 5:
            return 1  # high card
        
    @staticmethod
    def convert_card(card):
        if card.isdigit():
            return int(card)
        if card == 'T':
            return 10
        elif card == 'J':
            return 11
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
