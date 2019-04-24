def generate_hashtags():
    lines = [line.rstrip('\n') for line in open('data/hashtags_combination.txt')]
    import random
    random.shuffle(lines)
    return " ".join(lines[:26])
