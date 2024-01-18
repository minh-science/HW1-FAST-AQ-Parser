# write tests for transcribe functions

from seqparser import (
        transcribe,
        reverse_transcribe)

import pytest


def test_freebie_transcribe_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True


def test_freebie_transcribe_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2


def test_transcribe():
    """
    Write your unit test for the transcribe function here.
    """
    # assert that the transcribe function transcribes properly
    assert transcribe("GCAT") == "CGUA"

    # assert that an error is raised if given something thats not in the dictionary
    with pytest.raises(ValueError):
        transcribe("Z")


def test_reverse_transcribe():
    """
    Write your unit test for the reverse transcribe function here.
    """
    # assert that the reverse transcribe function reverse transcribes properly
    assert reverse_transcribe("GCAT") == "AUGC"

    # assert that an error is raised if given something thats not in the dictionary
    with pytest.raises(ValueError):
        reverse_transcribe("Z")

