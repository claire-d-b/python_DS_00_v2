def ft_filter(function: any, words: list):
    """ applies given function to each item of the list """
    ret = [item for item in words if function(item)]
    return iter(ret)
