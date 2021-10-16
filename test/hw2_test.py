import unittest
import homework2.mymodule

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEquals(2, 2)

if __name__ == "__main__":
    import rosunit
    rosunit.unitrun(homework2, 'test_class_name', MyTestCase)
