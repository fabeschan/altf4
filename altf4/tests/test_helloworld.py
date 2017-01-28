from unittest import TestCase

from altf4 import helloworld

class TestHelloWorld(TestCase):
    def test_is_string(self):
        hw = helloworld.HelloWorld()
