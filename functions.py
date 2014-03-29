def count(name1, name2):
    '''
        Takes two strings and returns the numbers of chatacters
        that doesnot match in both the strings

        Eg:
        >>> count('abc', 'bc')
        2
        >>> count('', 'defg')
        0
    '''
    name1 = name1.lower()
    name2 = name2.lower()
    count_arr = {}
    length1 = 0
    length2 = 0

    for i in "abcdefghijklmnopqrstuvwxyz ":
        count_arr.update({i: 0})

    for i in name1:
        if i == ' ':
            continue
        length1 = length1 + 1
        count_arr[i] = count_arr[i] + 1

    ct = 0
    for i in name2:
        if i == ' ':
            continue
        length2 = length2 + 1
        if count_arr[i] > 0:
            ct = ct + 1
            count_arr[i] = count_arr[i] - 1
    
    return length1 + length2 - 2 * ct


def flames_calc(count):
    '''
        Takes the count and returns the result value after
        computation of flames

        Eg:
        >>> flames_calc(4)
        e
        >>> flames_calc(7)
        s
    '''
        
    flames = ['f', 'l', 'a', 'm', 'e', 's']
    a = len(flames)
    i = 0

    while a > 1:
        l1 = len(flames)
        i = (count + i - 1)%l1
        flames.pop(i)
        a = a - 1
    return flames[0]


def result(a):
    '''
         Takes a characters and returns a string related to it

         Eg:
         >>> result(e)
         You are Enemies. Don't kill each other
    '''
    
    dict = { 'f': "Great, you are friends",
             'l': "Oho, Lovers",
             'a': "Aquaintances ",
             'm': "Married ... !!",
             'e': "You are Enemies. Don't kill each other",
             's': "Sisters.. oh or brothers!!" }
    return dict[a]

