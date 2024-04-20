from television import Television

def test_power():
    tv = Television()
    assert not tv._Television__status
    '''tv turn off'''


    tv.power()
    assert tv._Television__status
    '''tv turning on'''

    tv.power()
    assert tv._Television__status
    '''tv turning off'''