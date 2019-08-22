from unittest import TestCase
import unittest

def increment_dictionary_values(di, i):
    d = di.copy()
    for k, v in d.items():
        print(k, " ", v)
        d[k] = v + i
        return d
    
class TestIncrementDictionaryValues(TestCase):
    
    def test_increment_dictionary_values(self):
        d = {'a': 1}
        dd = increment_dictionary_values(d, 1)
        self.assertEqual(dd['a'], 2)
        ddd = increment_dictionary_values(d, -1)
        self.assertEqual(ddd['a'], 0)

unittest.main()

