import cap
import unittest

class TestCap(unittest.TestCase):

    def test_sentence_cap(self):
        test_sent = 'hello world !'
        result = cap.cap_sentence(test_sent)
        self.assertEqual(result,'Hello World !')

    def test_word_cap(self):
        test_word = 'monty'
        result = cap.cap_sentence(test_word)
        self.assertEqual(result,'Monty')

if __name__ == '__main__':
    unittest.main()