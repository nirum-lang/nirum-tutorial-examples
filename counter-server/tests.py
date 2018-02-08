import os
from tempfile import mkstemp
from unittest import TestCase
from counter_server import CounterImpl

class CounterImplTest(TestCase):
    def setUp(self):
        fd, self.path = mkstemp()
        os.close(fd)  # only path is necessary
        self.counter = CounterImpl(self.path)
    def tearDown(self):
        os.unlink(self.path)
    def test_initial_state(self):
        self.assertEqual(0, self.counter.increment(delta=0))
    def test_increment(self):
        self.assertEqual(1, self.counter.increment(delta=1))
        self.assertEqual(2, self.counter.increment(delta=1))
    def test_increment_by_5(self):
        self.assertEqual(5, self.counter.increment(delta=5))
        self.assertEqual(10, self.counter.increment(delta=5))
