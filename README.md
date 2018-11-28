# testworks
Simple Python Testing Framework

## Usage
Written test functions must be within a class, and the class' name must be passed into the testwork.test function.
Functions starting with 'DISABLED' will not run.

## Example
```python
import testworks
import assertion

class MyTestClass:
    def this_test_passes():
        pass

    def this_test_doesnt():
        assert 1 == 0

    def nor_this_one():
        a = 3 / 0

    def using_a_fancy_assertion():
        assertion.are_equal(1, 4)

    def using_a_new_assertion():
        assertion.is_false(True)

    def using_a_new_assertion():
        assertion.is_true(True)

    def DISABLED_this_wont_run():
        zero = 0 / 0

testworks.test(MyTestClass)
input() # Keep the window the results.
```
