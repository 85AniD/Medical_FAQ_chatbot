#f1 score

import sklearn
import unittest
import json
from sklearn.metrics import f1_score
from processor import predict_class
from keras.models import load_model

# Load the model
model = load_model('chatbot_model.h5')

# Load the intents file
with open('intents.json', 'r', encoding='utf-8') as file:
    intents = json.load(file)

# Load test data
with open('test_data.json', 'r', encoding='utf-8') as file:
    test_data = json.load(file)

class TestF1Score(unittest.TestCase):

    def test_f1_score(self):
        y_true = [item['intent'] for item in test_data]
        y_pred = [predict_class(item['question'], model) for item in test_data]

        f1 = f1_score(y_true, y_pred, average='weighted')
        print(f"F1 Score: {f1}")

        # Assert that the F1 score is above a certain threshold
        self.assertGreater(f1, 0.7)

if __name__ == '__main__':
    unittest.main()
