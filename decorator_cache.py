from collections import OrderedDict


def add_to_cache(func):
    cache = OrderedDict()

    def wrapper(invoer):
        r = None
        if len(cache) <= 500:
            if invoer not in cache:
                r = func()
                cache[invoer] = r
                cache.move_to_end(invoer, last=False)
                with open('cache.log', 'a')as cachefile:
                    cachefile.write(invoer+'\n')
            else:
                pass
        else:
            cache.popitem(last=True)

        return r
    return wrapper


@add_to_cache
def show_terminal():
    print(invoer)


if "__main__" == __name__:
    stop = False
    while stop == False:
        invoer = input('Geef iets in, typ stop om te stoppen: ')
        if invoer.lower() != 'stop':
            show_terminal(invoer)
        else:
            stop = True
