def ft_filter(function: any, words: list):
    """filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""
    ret = [item for item in words if function(item)]
    return iter(ret)
