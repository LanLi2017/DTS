def get_cell_value(i,j):
    pass


def identity_func(i,j):
    '''
    
    :param i: index of row
    :param j: index of column
    :return: the value doesn't get changed
    '''
    return get_cell_value(i,j)


def constant_func(value):
    '''
    
    func(c(i,j))=value
    '''

    return value


def func_compose(f,g):
    # a function that takes two functions as arguments (f and g) and returns
    # a function representing their composition
    return lambda x: f(g(x))


def func_invertible(f,g):
    # The function can be reversed
    # f'g(x)=g'f(x)
    # return true or false
    return func_compose(f,g)==func_compose(g,f)


def column_trans_func():

    pass


def column_independent():
    pass
















