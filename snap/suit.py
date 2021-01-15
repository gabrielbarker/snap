class Suit:
    @staticmethod
    def char(index):
        return Suit._suit_map[index][0]

    @staticmethod
    def name(index):
        return Suit._suit_map[index][1]

    _suit_map = [["♡", "heart"], ["♢", "diamond"], ["♣", "club"], ["♠", "spade"]]
