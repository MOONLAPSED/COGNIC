class FailFastException(Exception):
    pass

def fail_fast(condition, message):
    """
    If the condition is False, raise an exception to fail fast.
    """
    if not condition:
        raise FailFastException(message)