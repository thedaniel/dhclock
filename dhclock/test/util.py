from __future__ import with_statement

def raises(exception, kallable, *a, **kw):
    """
    we need to return the exception, duh
    """
    try:
        kallable(*a, **kw)
    except exception as e:
        return e
    else:
        if hasattr(exception,'__name__'):
            name = exception.__name__
        else:
            name = str(exception)
        raise AssertionError("%s not raised" % name)
