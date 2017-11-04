if __name__ == '__main__':
    n = int(raw_input())
    seq = raw_input()
    integer_list = map(int, seq.split()) """The map(aFunction, aSequence)
    #function applies a passed-in function to each item in an iterable
    #object (say a list) and returns a list containing all the function call results.
    """
    mytup = tuple(integer_list)
    print hash(mytup)
