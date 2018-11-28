from inspect import isclass

def __find_tests(classname):
    print("Looking for tests in class " + classname.__name__ + ".")
    tests = []
    for key in classname.__dict__:
        value = classname.__dict__[key]
        if (not key.startswith("DISABLED")) and callable(value):
            tests.append(value)
    print("Found", len(tests), "tests.")
    return tests

def __perform_test(function):
    print(function.__name__ + ": ", end="")
    try:
        function()
        print("PASSED")
        return True
    except AssertionError as error:
        print("FAILED: " + str(error))
    except Exception as error:
        print("FAILED: An exception was thrown:\n\t" + str(error))
    
    return False

def __display_results(count, passed, failed):
    print(passed + " tests passed out of " + count + ". (" + failed + " failed.)")

def test(classname):
    assert isclass(classname)
    tests = __find_tests(classname)

    passedTests = 0
    testCount = len(tests)

    for i in range(testCount):
        success = __perform_test(tests[i])
        if success: passedTests += 1
    
    failedTests = (testCount - passedTests)

    __display_results(str(testCount), str(passedTests), str(failedTests))

    return failedTests
