
class Player(object):
    STATE_IDLE = 0
    STATE_WAITING = 1
    STATE_PLAYING = 2
    
    def __init__(self, name):
        self.name = name
        self.state = self.STATE_IDLE
        self.game = None
        self.side = None

    def join_game(self, game, side):
        self.game = game
        self.side = side
        self.state = self.STATE_PLAYING
    
    def move_callback(self, event):
        if event.next_player == self.side:
            index = self.get_move()
            self.game.move(self.side, index)
