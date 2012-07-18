"""
The Kalah game itself
"""

__version__ = "1.0.0"
__author__ = "David Poisl <david@poisl.at>"


import events


class Ruleset(object):
    """base class for kalaha rules"""
    DEFAULT_RUlES = {"theft": True, 
                     "extra_turns": True, 
                     "score_looser_fields": True, 
                     "seeds_per_field": 3,
                     "field_width": 6,
                     }

    @classmethod
    def new(cls, name=UnnamedRules, **kwargs):
        """
        shortcut to create a ruleset 
        
        for possible arguments see DEFAULT_RULES
        """
        dict_ = cls.DEFAULT_RULES.copy()
        dict_.update(dict((k,kwargs[k]) for k in kwargs if k in cls.DEFAULT_RULES))
        return type(name, (cls,), dict_)()


class Side(object):
    """a side of the game board"""
    def __init__(self, game, side, handicap=0):
        self.fields = [game.ruleset.seeds_per_field] * game.ruleset.field_width
        self.pot = handicap
        self.side = side
        self.game = game
    
    @property
    def other_side(self):
        return self.game.sides[1 - self.side]
    
    @property
    def score(self):
        return self.pot

    @property
    def has_won(self):
        return sum(self.fields) == 0

    def add_pebbles(self, index, count, add_to_pot=True):
        """
        Handle pebble distribution for a move on one board side

        If required it forwards the remaining pebbles to the
        opponents side if required.

        returns True if this move results in a free move!
        """
        if count == 0:
            return False
        
        # optional rule: if the last pebble lands in an empty field of the 
        # active player the pebbles oposite to it are addet to the pot.
        if count == 1 and index < len(self.fields) and self.fields[index] == 0 \
                and self.game.ruleset.theft:
            bonus = self.other_side.fields[index]
            prev = self.other_side.fields[index]
            self.other_side.fields[index] = 0
            self.game.send_event(events.FieldChanged(self.game, self.other_side,
                                                     index, prev, 0))
            prev = self.pot
            self.pot += (bonus + 1)
            self.game.send_event(events.PotChanged(self.game, self.side, 
                                                   prev, self.pot))
            return False
        
        if index < len(self.fields):
            self.fields[index] += 1
            self.game.send_event(events.FieldChanged(self.game, self.side,
                                                     index, 
                                                     self.fields[index] - 1, 
                                                     self.fields[index]))
            return self.add_pebbles(index + 1, count - 1, add_to_pot)
        
        if index == len(self.fields) and add_to_pot:
            self.pot += 1
            self.game.send_event(events.PotChanged(self.game, self.side, 
                                                   self.pot - 1, self.pot))
            if count > 1:
                return self.other_side.add_pebbles(0, count - 1, not add_to_pot)
            else:
                return self.game.ruleset.extra_turns
        
        return self.other_side.add_pebbles(0, count - 1, not add_to_pot) + 1

    def move(self, index):
        """perform a move starting at this side of the board"""
        if self.has_won or self.other_side.has_won:
            raise IndexError("Board is already finished")
        if not 0 <= index < len(self.fields):
            raise IndexError("Field index %d is out of range (0 .. %d)" % (
                             index, len(self.fields) - 1))

        count = self.fields[index]
        if count == 0:
            raise IndexError("invalid move: can not move from empty field")
        
        self.fields[index] = 0
        return self.add_pebbles(index + 1, count, True)
    
    def get_fields(self, reverse=False):
        """get the field counters, if required in reverse order"""
        return self.fields if not reverse else reversed(self.fields)


class Board(events.EventSender):
    """a kalaha game board"""
    def __init__(self, ruleset=Ruleset()):
        """create a new board and its sides according to the given rules"""
        super(Board, self).__init__()
        self.ruleset = ruleset
        self.width = ruleset.field_width
        self.sides = [Side(self, 0), Side(self, 1)]
        self.send_event(events.GameStart(self))

    def move(self, side, index):
        """a game move. player order is NOT checked"""
        self.send_event(events.Move(self, side, index))
        res = self.sides[side].move(index)
        if self.sides[side].has_won:
            self.send_event(events.PlayerWon(self, side))
            return None # no more moves
        elif res:
            self.send_event(events.NextPlayer(self, side))
            return side # side moves again
        else:
            self.send_event(events.NextPlayer(self, 1 - side))
            return 1 - side # other_side moves


class Renderer(object):
    """base renderer"""
    def __init__(self, game, side=0):
        self.game = game
        self.side = side
    
    def _get_data(self):
        """internal function to get all required data from a board"""
        own = self.game.sides[self.side].get_fields()
        own_pot = self.game.sides[self.side].pot
        other = self.game.sides[1 - self.side].get_fields(True)
        other_pot = self.game.sides[1 - self.side].pot
        return (own, other, own_pot, other_pot)


class TextRenderer(Renderer):
    """renderer for text output"""
    def render(self):
        """render the board"""
        (own, other, own_pot, other_pot) = self._get_data()
        return "".join(("    ", "  ".join("%2d" % o for o in other), "\n",
                        "%2d  " % other_pot, 
                        "  ".join("  " for i in range(self.game.width)),
                        "  %2d" % own_pot, "\n"
                        "    ", "  ".join("%2d" % o for o in own), "\n"))
