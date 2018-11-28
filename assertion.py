def is_true(actual, message = ""):
    if actual:
        raise AssertionError("is_true: " + message)

def is_false(actual, message = ""):
    if not actual:
        raise AssertionError("is_false: " + message)

def are_equal(expected, actual, message = ""):
    if not actual:
        raise AssertionError("are_equal: " + message)
