#HW 3
#Due Date: 02/01/2019, 11:59PM
########################################
#                                      
# Name:
# Collaboration Statement: https://docs.python.org/3/library/functions.html  
#
########################################


def findNextOpr(txt):
    """
        >>> findNextOpr('  3*   4 - 5')
        3
        >>> findNextOpr('8   4 - 5')
        6
        >>> findNextOpr('89 4 5')
        -1
    """
    if not isinstance(txt,str) or len(txt)<=0:
        return "error: findNextOpr"

    # --- YOU CODE STARTS HERE
    operators = ['+', '-', '/', '*', '^']
    text = list(filter(lambda c: c != ' ', txt))
    print(text)
    for value, c in enumerate(text, 0):
        if c in operators:
            print(text[value+1])
            return
    print -1

findNextOpr('  3*   4 - 5')
findNextOpr('8   4 - 5')
findNextOpr('89 4 5')

print('_' * 15)

def isNumber(txt):
    """
        >>> isNumber('1   2 3')
        False
        >>> isNumber('-  156.3')
        False
        >>> isNumber('     29.99999999    ')
        True
        >>> isNumber('    5.9999x ')
        False
    """
    if not isinstance(txt, str) or len(txt)==0:
        return "error: isNumber"
    # --- YOU CODE STARTS HERE
    text = filter(lambda c: c != ' ', txt).split()
    items = []
    item = ''
    print(text)
    if len(text) > 1:
        print(False)
        return
    else:
        try:
            float(text[0])
            print(True)
            return
        except ValueError:
            print(False)
            return
        
isNumber('1   2 3')
isNumber('-  156.3')
isNumber('     29.99999999    ')
isNumber('    5.9999x ')

def getNextNumber(expr, pos):
    """
        >>> getNextNumber('8  +    5    -2',0)
        (8.0, '+', 3)
        >>> getNextNumber('8  +    5    -2',4)
        (5.0, '-', 13)
        >>> getNextNumber('4.5 + 3.15         /  -5',20)
        (-5.0, None, None)
        >>> getNextNumber('4.5 + 3.15         /   5',10)
        (None, '/', 19)
    """

    if not isinstance(expr, str) or not isinstance(pos, int) or len(expr)==0 or pos<0 or pos>=len(expr):
        return None, None, "error: getNextNumber"
    # --- YOU CODE STARTS HERE
