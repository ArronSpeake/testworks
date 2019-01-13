# testworks
Simple Python Testing Utility

## Usage
Written test functions must be within a class, and the class' name must be passed into the testwork.test function.
Test functions starting with `DISABLED` will not run.

A normal `assert` statement can be used, or alternatively, the `assertion` class can be imported.

### Assertions

Assertion   | Description
:-----------|:-----------
`is_true`   | Asserts that a value is true.
`is_false`  | Asserts that a value is false.
`are_equal` | Asserts that two values are equal.

An optional `message` argument can also be given, which is displayed when that assertion fails.

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
        assertion.is_false(True, "Should've been false. Whoops.")

    def using_a_new_assertion():
        assertion.is_true(True)

    def DISABLED_this_wont_run():
        zero = 0 / 0

testworks.test(MyTestClass)
input() # Keeps the window open.
```
