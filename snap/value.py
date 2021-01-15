class Value:
    @staticmethod
    def string(index):
        return Value._values(index)[0]

    @staticmethod
    def name(index):
        return Value._values(index)[1]

    @staticmethod
    def _values(index):
        if index == 0:
            return Value._value_map[0]
        if 0 < index < 9:
            return [str(index + 1) + " ", str(index + 1)]
        return Value._value_map[index - 8]

    _value_map = [
        ["A ", "ace"],
        ["10", "10"],
        ["J ", "jack"],
        ["Q ", "queen"],
        ["K ", "king"],
    ]
