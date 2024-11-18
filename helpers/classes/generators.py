class InheritanceGenerator:

    def __call__(self, name, *args):
        return type(name, args, {})


class DynamicContextManager:

    def __init__(self, enter, exit):
        self._enter = enter
        self._exit = exit

    def __enter__(self):
        return self._enter(self)

    def __exit__(self, *args):
        return self._exit(*args)
