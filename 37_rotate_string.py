
def rotate_string(s, k):
    if not s:
        return s

    k = k % len(s)
    return s[-k:] + s[:-k] if k else s