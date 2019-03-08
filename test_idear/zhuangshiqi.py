def canshu(times):
    def fun(function):
        def fun_in(*args):
            new = []
            for arg in args:
                print(arg, times)
                arg *= times
                new.append(arg)
            return function(new)

        return fun_in

    return fun


@canshu(10)
def test(*args):
    for arg in args:
        print(arg)


test(1, 2)
# 1 2 10
# 11
# 12
