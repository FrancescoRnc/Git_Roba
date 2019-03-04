SUFFIXES = ['KB', 'MB', 'GB', 'PB', 'EB', 'ZB', 'YB']

def appriximate_size(size):
    multiple = 1024
    for suffix in SUFFIXES:
        size /= multiple
        if size < multiple:
            return '{} {}'.format(size, suffix)
            # format string
    raise ValueError('number too large')