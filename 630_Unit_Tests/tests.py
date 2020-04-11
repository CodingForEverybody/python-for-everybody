import unittest
from my_program import make_it_uppercase, get_first_word, return_a_list


class TestMyProgram(unittest.TestCase):

    def test_hello_world(self):
        result = make_it_uppercase("hello world")
        self.assertEqual(result, 'HELLO WORLD')

    def test_first_word_in_sentence(self):
        sentence = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Veniam laboriosam consequatur saepe. Repellat itaque dolores neque, impedit reprehenderit eum culpa voluptates harum sapiente nesciunt ratione."
        result = get_first_word(sentence)
        self.assertEqual(result, 'Lorem')

    def test_first_word_in_sentence_with_one_word(self):
        sentence = "Lorem"
        result = get_first_word(sentence)
        self.assertEqual(result, 'Lorem')

    def test_return_a_list(self):
        result = return_a_list()
        self.assertListEqual(
            result,
            ['Cats', 'Dogs', 'Birds'],
            "THE LIST WAS WRONG!!",
        )

if __name__ == "__main__":
    unittest.main()
