#write function tests here, don't add input('') statements here!
import unittest

#follow this example to add questions b, c, and d for testing including their functions
from src.question_a.question_a import test_config, eval_age


class Test_Config(unittest.TestCase):

    def test_question_a_config(self):
        self.assertEqual(True, test_config())

    def test_eval_age(self):
        self.assertEquals(eval_age(1),"infant")
        self.assertEquals(eval_age(2),"child")

