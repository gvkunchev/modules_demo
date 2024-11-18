def logged_input(fun):
    def decorated(*args, **kwargs):
        print(f'{fun.__name__} called with {args} and {kwargs}')
        return fun(*args, **kwargs)
    return decorated


def logged_output(fun):
    def decorated(*args, **kwargs):
        result = fun(*args, **kwargs)
        print(f'{fun.__name__} returns {result}')
        return result
    return decorated
