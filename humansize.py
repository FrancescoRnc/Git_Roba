SUFFIXES = ['KB', 'MB', 'GB', 'PB', 'EB', 'ZB', 'YB']

def appriximate_size(size = 10000):
    '''
    Convert a file size to a human readable form.
    
    Keyword arguments:
    size -- file size in bytes

    Returns: string
    '''
    multiple = 1024
    for suffix in SUFFIXES:
        size /= multiple
        if size < multiple:
            return '{} {}'.format(size, suffix)
            # format string
    raise ValueError('number too large')