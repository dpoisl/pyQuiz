#!/usr/bin/env python
# -*- coding: utf-8 -*-

import enum

from typing import Iterable, Tuple

class Color(enum.Enum):
    RED = 1
    GREEN = 2 
    BLUE = 3
    YELLOW = 4
    PINK = 5
    PURPLE = 6
    

def master(secret: Iterable[Color], guess: Iterable[Color]) -> Tuple[int]:
    """
    Return the scoring for a guess in mastermind.

    Returns a tuple with the first item being exact matches of the same color in 
    secret and guess and the second item being the number of correct colors in the
    wrong position.
    
    :param secret: the secret to guess
    :param guess: the guess
    :return score with (correct, wrong_position)
    """
    matches = [s == g for (s, g) in zip(secret, guess)]
    unmatched_secrets = [s for (idx, s) in enumerate(secret) if not matches[idx]]
    almost = [1 for (index, item) in enumerate(guess) if not matches[index] and item in unmatched_secrets]
    return (sum(matches), sum(almost))
