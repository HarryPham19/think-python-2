import string

index_of = dict(zip(string.ascii_lowercase, range(26)))
letter_of = dict(enumerate(string.ascii_lowercase))


def rotate_word(s, r):
    """ Rotate the given word by r units.

    Args:
        s : a string.
        r: an integer.

    Returns:
        a rotated - by - r word.
    """
    result = []
    for c in s:
        new_index = (index_of[c] + r) % 26
        result.append(letter_of[new_index])

    return ''.join(result)


