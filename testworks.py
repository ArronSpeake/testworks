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

def test(classname):
    assert isclass(classname)
    tests = __find_tests(classname)
    testCount = len(tests)
    passedTests = 0
    for i in range(testCount):
        fx = tests[i]
        print(fx.__name__ + ": ", end="")
        try:
            fx()
            print("PASSED")
            passedTests += 1
        except AssertionError:
            print("FAILED")
        except Exception as error:
            print("FAILED - An exception was thrown.")
    print(str(passedTests) + " tests passed out of " + str(testCount) + ". (" + str(testCount - passedTests) + " failed.)")
