#test_processor.py

import unittest
import numpy as np
from keras.models import load_model
from processor import clean_up_sentence, bow, predict_class, get_response
import json

# Load the model
model = load_model('chatbot_model.h5')

# Load the intents file
with open('intents.json', 'r', encoding='utf-8') as file:
    intents = json.load(file)

class TestProcessor(unittest.TestCase):

    def test_clean_up_sentence(self):
        self.assertEqual(clean_up_sentence("Hello, how are you?"), ["hello", "how", "are", "you"])

    def test_bow(self):
        self.assertIsInstance(bow("Hello", ["hello", "world"]), np.ndarray)

    def test_predict_class(self):
        self.assertIsInstance(predict_class("Hello", model), list)

    def test_get_response(self):
        ints = predict_class("Hello", model)
        self.assertIsInstance(get_response(ints, intents), str)

if __name__ == '__main__':
    unittest.main()
