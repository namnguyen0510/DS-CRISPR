import random


def random_sample(lst):
    return random.choice(lst)

def shuffle_dict_by_key(d):
    keys = list(d.keys())
    random.shuffle(keys)
    new_dict = {k: d[k] for k in keys}
    return new_dict

def sample_from_dict(d):
    key = random.choice(list(d.keys()))
    value = d[key]
    return key, value