def generate_hashtags(version):
    source = 'data/hashtags_combination.txt'
    if version == "v2":
        source = 'data/hashtags_combination_v2.txt'
    elif version == "foy":
        source = 'data/foy.txt'
    elif version == "swots":
        source = 'data/swots.txt'
    lines = [line.rstrip('\n') for line in open(source)]
    import random
    random.shuffle(lines)
    return " ".join(lines[:26])
