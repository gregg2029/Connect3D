class Move:

  def arguments(self):
    assert False, "Include in move"
  
class Place(Move):
  alpha_mapping = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}

  def __init__(self, letter, number):
    if self.letter.upper() in alpha_mapping.keys() and (
    number >= 1 and number <= 5):
      self.x = alpha_mapping[self.letter]
      self.y = number - 1 # Account for 0 index
    else:
      assert False, "Invalid file"
  
  def arguments(self):
    return [self.x, self.y]

class Peek(Move):
  def __init__(self):
    pass

  def arguments(self):
    return []