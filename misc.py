def str_md5(content):
    import hashlib
    m = hashlib.md5(content)
    return m.hexdigest()


def setlog(logname='', filename=None, console=True):
    import logging
    logger = logging.getLogger(logname)
    logger.setLevel(logging.DEBUG)

    fmt = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s')
    #file handler
    if filename:
        fh = logging.FileHandler(filename)
        fh.setLevel(logging.INFO)
        fh.setFormatter(fmt)
        logger.addHandler(fh)

    #console handler
    if console:
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(fmt)
        logger.addHandler(ch)
    return logger
