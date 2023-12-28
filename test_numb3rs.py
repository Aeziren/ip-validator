import numb3rs

def test_valid():
    assert numb3rs.validate("192.168.1.0") == True
    assert numb3rs.validate("255.255.255.0") == True
    assert numb3rs.validate("127.0.0.1") == True

def test_long():
    assert numb3rs.validate("192.168.168.0.1") == False

def test_short():
    assert numb3rs.validate("192.0.1") == False

def test_letters():
    assert numb3rs.validate("cat.dog.cat.dog") == False

def test_block():
    assert numb3rs.validate("275.3.1.7") == False
    assert numb3rs.validate("1922.0.10.5") == False

def test_last_blocks():
    assert numb3rs.validate("192.256.256.256") == False
