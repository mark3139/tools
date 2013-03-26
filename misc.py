def str_md5(content):
    import hashlib
    m = hashlib.md5(content)
    return m.hexdigest()
