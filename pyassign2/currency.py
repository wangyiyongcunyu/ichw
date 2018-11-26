def exchange(currency_from,\
currency_to, amount_from):
    """In this exchange, the user
is changing amount_from money in 
    currency currency_from to the 
currency currency_to. 
    The value returned represents 
the amount in currency currency_to.
    Parameter currency_from: 
the currency on hand
    Precondition: currency_from is 
a string for a valid currency code
    Parameter currency_to:
the currency to convert to
    Precondition: currency_to is
a string for a valid currency code
    Parameter amount_from: 
amount of currency to convert
    Precondition: amount_from 
is a float
    Returns: amount of currency、 
received in the given exchange."""
    from urllib.request import urlopen

    doc = urlopen\
    ('http://cs1110.cs.cornell.\
edu/2016fa/a1server.php?from='\
+currency_from+'&to='+currency\
_to+'&amt={0}'.format(amount_from))
    docstr = doc.read()
    doc.close()
    jstr = docstr.decode('ascii')
    jstr = jstr.replace('true','True')\
and jstr.replace('false','False')
    dic =eval(jstr)
    if dic['success']==True:
        s=dic['to']
        t=s.split(' ')
        end=float(t[0])
        return end
    else:
        return dic['error']
currency_from = input()
currency_to = input()
amount_from = input()
print(exchange(currency_from,\
currency_to, amount_from))    

def test_currency():
    """verify types of the currency 
    users input are valid"""
    assert('Source currency code is invalid.' == exchange\
           ('AAA','BBB',2.5),'validity verification error')
def test_amount_from():
    """verify that the values 
    entered by user are valid"""
    assert('Currency amount is invalid' == exchange\
           ('USD','EUR','q'),'validity verification error')
def test_output():
    """verify that output is correct and 
    the type of it is float"""
    assert(2.15828 == exchange\
           ('USD','EUR',2.5),'output error')
def testAll():
    """test all cases"""
    test_currency()
    test_amount_from()
    test_output()
    print("All tests passed")
testAll()
