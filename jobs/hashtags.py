def generate_hashtags(version):
    source = 'data/hashtags_combination.txt'
    if version == "v2":
        source = 'data/hashtags_combination_v2.txt'
    lines = [line.rstrip('\n') for line in open(source)]
    import random
    random.shuffle(lines)
    return " ".join(lines[:26])
