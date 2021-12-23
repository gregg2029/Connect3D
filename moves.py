class Move:

    def arguments(self):
        assert False, "Include in move"


class Place(Move):

    def __init__(self, arg_arr):
        alpha_mapping = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}

        # Parse letter and number
        letter = ""
        number = None
        if len(arg_arr) == 1:
            arg = arg_arr[0]
            if len(arg) == 2:
                letter = arg[0]
                number = int(arg[1])
            else:
                assert False, "Incorrectly formatted"
        elif len(arg_arr) == 2:
            letter = arg_arr[0]
            number = int(arg_arr[1])
        else:
            assert False, "Incorrectly formatted"

        # Check for validity and create Place object
        if letter.upper() in alpha_mapping.keys() and (
                number >= 1 and number <= 5):
            self.x = alpha_mapping[letter]
            self.y = number - 1  # Account for 0 index
        elif letter.upper() not in alpha_mapping.keys():
            assert False, "Invalid file"
        elif (number < 1 and number > 5):
            assert False, "Invalid rank"

    def arguments(self):
        return self.x, self.y


class Peek(Move):
    def __init__(self):
        pass

    def arguments(self):
        return []
