from suman import Guvi 


def test_Name_Upper():
    data = 'suman'
    assert Guvi().NameUpper(data) == 'SUMAN'

def test_Name_Lower():
    data = 'suman'
    assert Guvi().NameLower(data) == data 