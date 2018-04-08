import functools


def debug(func=None, *, prefix=''):
    if func == None:
        # print("none")
        return functools.partial(debug, prefix=prefix)

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        """this is the warpper function to debug"""
        full_name = prefix + func.__qualname__
        print(full_name)
        return func(*args, **kwargs)

    return wrapper


def debugmethods(cls):
    for k,v in vars(cls).items():
        if callable(v):
            setattr(cls, k, debug(v))
    return cls 


def debugAttributes(cls):
    orig_geattribute = cls.__getattribute__
    def __getattribute__(self, value):
        print("Get: {}".format(value))
        return orig_geattribute(self, value)
    cls.__getattribute__ = __getattribute__
    return cls 