class Player:
  
  #Player initialization
  def __init__(self, id, name):
    self.id = id
    self.name = name
    self.move_history = list()
