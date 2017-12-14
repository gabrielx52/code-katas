"""Test parenthetics module."""


def test_parenthetics_with_simple_balanced_seq():
    """Test balanced sequence."""
    from parenthetics import parenthetics
    assert parenthetics('((((()))))') == 0


def test_parenthetics_with_complicated_balanced_seq():
    """Test balanced sequence."""
    from parenthetics import parenthetics
    assert parenthetics('((()((()))())())()()(())') == 0


def test_parenthetics_with_simple_open_seq():
    """Test open sequence."""
    from parenthetics import parenthetics
    assert parenthetics('((((()))))(') == 1


def test_parenthetics_with_complicated_open_seq():
    """Test open sequence."""
    from parenthetics import parenthetics
    assert parenthetics('((()((()))())())()()((())(') == 1


def test_parenthetics_with_simple_broken_seq():
    """Test broken sequence."""
    from parenthetics import parenthetics
    assert parenthetics(')((((()))))') == -1


def test_parenthetics_with_simple_broken_seq_again():
    """Test broken sequence."""
    from parenthetics import parenthetics
    assert parenthetics('((())))') == -1
