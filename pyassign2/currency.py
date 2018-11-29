"""
Exchange.py : this module provides several string parsing functions to implement a 
simple currency exchange routine using an online currency service. 
The primary function in this module is exchange.

__author__ = "张序年"
__pkuid__  = "1800094603"
__email__  = "1800094603@pku.edu.cn"
"""

from urllib.request import urlopen

def exchange(currency_from, currency_to, amount_from):
    """
    
    This function form an url according to the input user typed in and 
    return the value of the targeted currency by analysing
    the output of the url
    
    """
    currency_from2 = currency_from.upper()
    currency_to2 = currency_to.upper()
    doc = urlopen('http://cs1110.cs.cornell.edu/2016fa/a1server.php?from='+currency_from2+'&to='+currency_to2+'&amt='+amount_from)
    docstr = doc.read()
    doc.close()
    jstr = docstr.decode('ascii')
    jstr = jstr.replace("true","True")      #python couldn't define "true"
    jstr = jstr.replace("false","False")    #python couldn't define "false"

    dic = eval(jstr)                        #change the string into a dictionary
    if dic["success"] == True:
        to = dic["to"]
        tolist = to.split()
        a = float(tolist[0])
        return a
    else:
        return "error"

def test_get_from():
    """
    this function check the answer of output for some examples
    
    """
    assert exchange("USD","EUR","2.5") == 2.1589225
    assert exchange("MYR","CNY","1000") == 1654.6789518105
    
def test_B():
    """
    this function check the output of the function if 
    the input of source currency and target currency is wrong
    
    """
    assert exchange("000","EUR","2.5") == "error"
    assert exchange("USD","ILU","2.5") == "error"
    
def test_C():
    """
    this function check the output of the function if
    the input of the amount is wrong
    
    """
    assert exchange("MYR","CNY","USD") == "error"
    assert exchange("USD","EUR","True") == "error"
    
def testAll():
    """
     this function test all cases above
    """
    test_get_from()
    test_B()
    test_C()
    print("All tests passed")
    
def main():
    afrom = input("需转化的货币名称\t: ")
    ato = input("转化成的货币名称\t: ")
    aamt = input("转化的数值\t: ")
    testAll()
    print("转化成的数值\t: "+str(exchange(afrom,ato,aamt)))

if __name__ == '__main__':
    main()