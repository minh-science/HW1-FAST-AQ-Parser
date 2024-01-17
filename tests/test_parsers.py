# write tests for parsers

from seqparser import (
        FastaParser,
        FastqParser)

import pytest


def test_freebie_parser_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True # things after the assert are true statements


def test_freebie_parser_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_FastaParser():
    """
    Write your unit test for your FastaParser class here. You should generate
    an instance of your FastaParser class and assert that it properly reads in
    the example Fasta File.

    Some example of "good" test cases might be handling edge cases, like Fasta
    files that are blank or corrupted in some way. Two example Fasta files are
    provided in /tests/bad.fa and /tests/empty.fa
    """
    
    # test if raises ValueError for bad.fa
    with pytest.raises(ValueError):
        next( iter( FastaParser("./tests/bad.fa") ) )

    # positive control for pytest.raises(ValueError) on something that shouldn't raise a ValueError
    # with pytest.raises(ValueError):
    #     next( iter( FastaParser("./data/test.fa") ) )

    # test if raises ValueError for blank.fa
    with pytest.raises(ValueError):
        next( iter( FastaParser("./tests/blank.fa") ) )


def test_FastaFormat():
    """
    Test to make sure that a fasta file is being read in 
    if a fastq file is read, the first item is None
    """
    # test if FastaParser raises ValueError for fastq instead of fasta 
    # with pytest.raises(ValueError):
    #     next( iter( FastaParser("./data/test.fq") ) ) 

    # assert the correct sequence if fasta file is read in properly
    assert next( iter( FastaParser("./data/test.fa"))) == ('seq0', 'TGATTGAATCTTTTGAGGGTCACGGCCCGGAAGCCAGAATTTCGGGGTCCTCTGTGGATATTAATCGAGCCCACACGGTGTGAGTTCAGCGGCCCCCGCA')

    # assert None if a fastq file is read in instead of a fasta file
    assert next( iter( FastaParser("./data/test.fq")))[0] == None

# print(next( iter( FastaParser("./data/test.fa"))))

def test_FastqParser(): # test proper fq files 
    """
    Write your unit test for your FastqParser class here. You should generate
    an instance of your FastqParser class and assert that it properly reads 
    in the example Fastq File.
    """
    # assert the correct sequence and quality if the fastq file is read in properly
    assert next( iter( FastqParser("./data/test.fq"))) == ('seq0', 'TGTGGTCGTATAGTTATTGTCATAAATTACACAGAATCGCGATTCTCCGCGTCCACCAATCTTAGTGCACCACAGCATCGACCCGATTTATGACGCTGAG', '*540($=*,=.062565,2>\'487\')!:&&6=,6,*7>:&132&83*8(58&59>\'8!;28<94,0*;*.94**:9+7"94(>7=\'(!5"2/!%"4#32=')

    # assert None if a fastq file is read in instead of a fasta file 
    assert next( iter( FastqParser("./data/test.fa")))[0] == None 

print( next( iter( FastqParser("./data/test.fa")))[0])

def test_FastqFormat():
    """
    Test to make sure fastq file is being read in. If this is a fasta file, the
    first line is None
    """
    # assert None if a fasta file is read in instead of a fastq file 
    assert next( iter( FastqParser("./data/test.fa")))[0] == None 