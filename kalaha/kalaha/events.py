"""
Kalah Game Events

Events sent by the kalah board engine
"""

__version__ = "1.0.0"
__author__ = "David Poisl <david@poisl.at>"


class Event(object):
    """base class for all events"""
    def __init__(self, board):
        self.board = board

    def __str__(self):
        """simple representation"""
        return "%s(%s)" % (self.__class__.__name__, 
                           ", ".join("%s=%r" % kv for kv in self.__dict__.items()))


class GameStart(Event):
    """board has started"""
    pass


class NextPlayer(Event):
    """
    indicate the next player

    side contains the side of the next player
    """
    def __init__(self, board, side):
        super(NextPlayer, self).__init__(board)
        self.side = side


class ExtraMove(NextPlayer):
    """an extra move for the current player was triggered"""
    pass


class Move(Event):
    """
    a move took place

    side contains the moving side, pot is the index on which
    the move ws played
    """
    def __init__(self, board, side, pot):
        super(Move, self).__init__(board)
        self.side = side
        self.pot = pot


class NextMove(Event):
    """the next move can take place"""
    def __init__(self, board, side):
        super(NextMove, self).__init__(board)
        self.side = side

class FieldChanged(Event):
    """a field changed"""
    def __init__(self, board, side, field, old_count, new_count):
        super(FieldChanged, self).__init__(board)
        self.side = side
        self.field = field
        self.old_count = old_count
        self.new_count = new_count


class PotChanged(Event):
    """the score pot of a player changed"""
    def __init__(self, board, side, old_score, new_score):
        super(PotChanged, self).__init__(board)
        self.side = side
        self.old_score = old_score
        self.new_score = new_score


class GameEnd(Event):
    """the board ended"""
    def __init__(self, board, winner):
        super(GameEnd, self).__init__(board)
        self.winner = winner


class PlayerWon(GameEnd):
    """board ended because a player won"""
    pass


class PlayerGaveUp(GameEnd):
    pass


class Error(Event):
    """something went wrong"""
    pass


class InvalidMove(Error):
    """a player tried an invalid move"""
    def __init__(self, board, position):
        super(InvalidMove, self).__init__(board)
        self.position = position


class EventSender(object):
    """
    A class that can send events

    Callback functions can be registered via add_listener and get notified of 
    all matching events. 
    When calling add_listener you can specify a list of base classes which are
    used to filter which events are sent to this callback.
    """
    def __init__(self):
        self._event_listeners = []
    
    def add_listener(self, listener, event_types=(object,)):
        """
        Add a new event callback

        Adds the callable in listener to the notification queue. If event_types 
        is specified it must be a class or list of classes. The callback will
        only receive events which are a instance of one of the given classes.
        """
        self._event_listeners.append((listener, event_types))

    def send_event(self, event):
        """send a new event to all listeners"""
        cnt = 0
        for (listener, event_types) in self._event_listeners:
            if isinstance(event, event_types):
                listener.__call__(event)
                cnt += 1
        return cnt

