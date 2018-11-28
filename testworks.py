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
        except AssertionError as error:
            print("FAILED: " + str(error))
        except Exception as error:
            print("FAILED: An exception was thrown:\n\t" + str(error))
    print(str(passedTests) + " tests passed out of " + str(testCount) + ". (" + str(testCount - passedTests) + " failed.)")
