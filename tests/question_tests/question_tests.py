#write function tests here, don't add input('') statements here!
import unittest

#follow this example to add questions b, c, and d for testing including their functions
from src.question_a.question_a import test_config, eval_age
from src.question_b.question_b import is_prime
from src.question_c.question_c import get_sum_of_evens

class Test_Config(unittest.TestCase):

    def test_question_a_config(self):
        self.assertEqual(True, test_config())

    def test_eval_age(self):
        self.assertEquals(eval_age(1),"infant")
        self.assertEquals(eval_age(2),"child")
        self.assertEquals(eval_age(14),"teenager")
        self.assertEquals(eval_age(20),"adult")

    def test_is_prime(self):
        self.assertEquals(is_prime(4),False)
        self.assertEquals(is_prime(5),True)
        self.assertEquals(is_prime(11),True)

    def test_get_sum_of_evens(self):
        self.assertEquals(get_sum_of_evens(11),30)
        self.assertEquals(get_sum_of_evens(10),30)
        self.assertEquals(get_sum_of_evens(8),20)