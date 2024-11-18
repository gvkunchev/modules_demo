def truthy_input(fun):
    def decorated(*args, **kwargs):
        return fun(*filter(bool, args),
                   **dict(filter(lambda kwarg: kwarg[1], kwargs.items())))
    return decorated


def string_output(fun):
    def decorated(*args, **kwargs):
        result = fun(*args, **kwargs)
        if isinstance(result, str):
            return result
    return decorated
