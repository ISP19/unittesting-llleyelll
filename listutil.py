def unique(lst):
    """Return a list containing only the first occurence of each distint
       element in list.  That is, all duplicates are omitted.

    Arguments:
        lst: a list of elements (not modified)
    Returns:
        a new list containing only distinct elements from list

    Examples:
    >>> unique([5])
    [5]
    >>> unique(["b","a","a","b","b","b","a","a"])
    ['b', 'a']
    >>> unique([])
    []
    """
    if not isinstance(lst, list):
        raise TypeError
    new_lst = []
    for ele in lst:
        if ele not in new_lst:
            new_lst.append(ele)
    return new_lst

def average( lst ):
    """Return a average of the list
    
    Arguments:
        lst: a list of number
    Returns:
        a average of numbers in the list

    Examples:
    >>> average([5])
    5.0
    >>> average([1, 4, 4, 4, 5])
    3.6
    >>> average([])
    Traceback (most recent call last):
        ...
    ValueError
    """
    if len(lst) == 0:
        raise ValueError
    return sum(lst)/len(lst)

if __name__ == "__main__":
    """Run the doctests in all methods."""
    import doctest
    doctest.testmod(verbose=True)
