def get_first_from_sorted(args, key, reverse):
    if len(args) == 1:
        args = iter(args[0])
    return sorted(args, key=key, reverse=reverse)[0]
    
def min(*args, **kwargs):
    key = kwargs.get("key", None)
    return get_first_from_sorted(args, key, False)
    return None


def max(*args, **kwargs):
    key = kwargs.get("key", None)
    return get_first_from_sorted(args, key, True)
    return None
