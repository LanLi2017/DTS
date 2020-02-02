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


def column_trans_func(op_name,j):
    # Column transformation means after the transformation,
    # The whole table deducts the old column and plus the new column after the transformation f.
    # paper got typo...need edition
    '''
    
    :param op_name: applied column transformation name ("split the column",etc)
    :param j: index of column
    :return: new value
    '''
    pass


def column_independent(f,g,x,y):
    # Two sequential columns are independent / parallel
    # f(x)'g(y)=g(y)'f(x)
    # change the order of the transformation, the results keep consistant
    '''
    
    :param f: operation history applied on column x
    :param g: operaiton history applied on column y
    :param x: column index x
    :param y: column index y
    :return: true or false
    '''
    return func_compose(column_trans_func(f,x),column_trans_func(g,y))== \
           func_compose(column_trans_func(g,y),column_trans_func(f,x))

















