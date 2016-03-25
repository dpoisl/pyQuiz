#!/usr/bin/env python

"""
A cheating mastermind player
"""


import sys


PATTERN_LENGTH = 4
ALLOW_REPITITIONS = False
SEARCH_INT = False
CANDIDATE_BLACKLIST = [getattr(__builtins__, x) for x in dir(__builtins__)]  # can't modify builtins
ATTRIBUTE_REPR_BLACKLIST = [  # list of attribute repr() strings to ignore
    '<slot-wrapper',
    '<method-wrapper \'',
    '<built-in method ',
    'ABCMeta',
    ]

# have stuff here for tests
c1="12345"
c2="1234"
c3="1111"


def is_valid_guess(candidate):
    """5432"""
    if SEARCH_INT and isinstance(candidate, int):
        return is_valid_guess(str(candidate))

    if isinstance(candidate, str):
        if not candidate.isdigit() or len(candidate) != PATTERN_LENGTH:
            return False
        if not ALLOW_REPITITIONS and len(set(candidate)) != len(candidate):
            return False
        return True

    return False


def scan_dict(obj):
    for (key, value) in list(obj.items()):
        yield key
        yield value


def scan_iterable(obj):
    try:
        for attribute in obj:
            yield attribute
    except Exception:
        pass

def scan_object(obj):
    for attribute_name in dir(obj):
        attribute = getattr(obj, attribute_name)
        attribute_repr = repr(attribute)
        if not any(entry for entry in ATTRIBUTE_REPR_BLACKLIST if attribute_repr.startswith(entry)):
            yield attribute


def find_guesses(obj, visited=None):
    if visited is None:
        visited = set()

    if is_valid_guess(obj) and id(obj) not in visited:  # first try the object itself
        yield obj

    if id(obj) not in visited and obj not in CANDIDATE_BLACKLIST:  # store visited objects by id
        visited.add(id(obj))

        # special case dictionaries
        if isinstance(obj, dict):
            for item in scan_dict(obj):
                yield from find_guesses(item, visited)

        # non-dictionary iterables
        elif isinstance(obj, (list, set, tuple)):
            for item in scan_iterable(obj):
                yield from find_guesses(item, visited)

        # always try attributes
        if obj not in CANDIDATE_BLACKLIST and obj.__class__ not in CANDIDATE_BLACKLIST:
            for attribute in scan_object(obj):
                yield from find_guesses(attribute, visited)


def cheat(root_object):
    guesses = set()
    for candidate in find_guesses(root_object):
        print('new candidate: %r' % candidate)
        guesses.add(candidate)
    return guesses

def cheating_interface(player):
    guesses = set()
    guesses.update(cheat(sys.modules))
    guesses.update(cheat(globals()))

    for guess in guesses:
        print('guess: %r', guess)
        answer = player.send(guess)
        print('  -> %s' % answer)
        if answer.startswith('success'):
            print('i won!')
            break



if __name__ == '__main__':
    print("globals: %r" % cheat(globals()))
    print("sys.modules: %r" % cheat(sys.modules))
