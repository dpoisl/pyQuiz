from mastermind import master, Color


def test_module_loaded():
    import mastermind
    assert mastermind is not None


def test_module_has_a_function():
    assert master is not None


def test_has_colors():
    assert Color.RED is not None
    assert Color.GREEN is not None


def test_different_colors():
    assert Color.RED != Color.GREEN


def test_empty_list():
    assert master([] ,[]) == (0, 0)


def test_one_correct():
    assert master([Color.RED], [Color.RED]) == (1, 0)


def test_different_colors():
    assert master([Color.RED],[Color.BLUE]) == (0, 0)


def test_longer_Lists_Are_Equal():
    secret = [Color.GREEN, Color.BLUE]
    guess = [Color.GREEN, Color.BLUE]
    result = master(secret, guess)
    assert result == (2, 0)


def test_one_correct_one_wrong():
    secret = [Color.GREEN, Color.BLUE]
    guess = [Color.GREEN, Color.PINK]
    result = master(secret, guess)
    assert result == (1, 0)


def test_one_wrong_position():
    secret = [Color.GREEN, Color.BLUE]
    guess = [Color.RED, Color.GREEN]
    result = master(secret, guess)
    assert result == (0, 1)


def test_one_wrong_repeating_guess():
    secret = [Color.RED, Color.BLUE]
    guess = [Color.RED, Color.RED]
    result = master(secret, guess)
    assert result == (1, 0)


def test_one_wrong_repeating_guess_two():
    secret = [Color.RED, Color.RED]
    guess = [Color.RED, Color.BLUE]
    result = master(secret, guess)
    assert result == (1, 0)


def test_match_with_repeated_wrong_guess():
    secret = [Color.PINK, Color.RED, Color.BLUE]
    guess = [Color.PINK, Color.RED, Color.RED]
    result = master(secret, guess)
    assert result == (2, 0)


def test_match_with_switched_guess():
    secret = [Color.PINK, Color.RED, Color.BLUE]
    guess = [Color.PINK, Color.BLUE, Color.RED]
    result = master(secret, guess)
    assert result == (1, 2)


def test_match_with_all_switched_guess():
    secret = [Color.RED, Color.PINK, Color.BLUE]
    guess = [Color.PINK, Color.BLUE, Color.RED]
    result = master(secret, guess)
    assert result == (0, 3)

