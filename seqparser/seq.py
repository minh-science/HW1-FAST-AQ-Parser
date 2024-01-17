# DNA -> RNA Transcription
from typing import Union

TRANSCRIPTION_MAPPING = {"A": "U", "C": "G", "T": "A", "G": "C"}
ALLOWED_NUC = TRANSCRIPTION_MAPPING.keys()


def transcribe(seq: str, reverse: bool = False) -> str:
    """
    Write a function that will transcribe (replace DNA sequence to RNA
    by replacing all 'T' to 'U') in an input sequence
    """
    RNA = ""
    for i in seq:
        if i in ALLOWED_NUC:
            RNA += TRANSCRIPTION_MAPPING[i]
        else:
            return f"uhoh, {i} is not an allowed nucleotide "
    return RNA
    
    # pass

def reverse_transcribe(seq: str) -> str:
    """
    Write a function that will transcribe an input sequence and reverse
    the sequence
    """
    # Hey this is my comment
    # Again!
    RT_str = ""
    RT_list = [i for i in transcribe(seq)][::-1]
    for i in RT_list:
        RT_str += i
    return RT_str
    # pass