from flask_restful import Resource, reqparse
from gensim.models import KeyedVectors

model = KeyedVectors.load("models/model.pkl")

class Similarity(Resource):

    def post(self):
        '''Outputs a similarity score for two words. 
        Closer to 1 means they are more similar and closer to 0 means they are less similar.'''

        parser = reqparse.RequestParser()
        parser.add_argument('word1')
        parser.add_argument('word2')

        args = parser.parse_args()  # creates dict
        word1 = args['word1']
        word2 = args['word2']

        out = {'Prediction': str(model.similarity(word1, word2))}

        return out, 200


class mostSimilar(Resource):

    def post(self):
        '''Outputs the 10 most similar words and their relative similarity scores for a given word.'''

        parser = reqparse.RequestParser()
        parser.add_argument('word1')

        args = parser.parse_args()  # creates dict
        word1 = args['word1']
      
        out = {'Prediction': str(model.most_similar(word1))}

        return out, 200


class wordAssociation(Resource):

    def post(self):
        '''Given the vector association between two words, given a new word the model projects the new word 
        using the vector association between the two original words and outputs the most similar words in that vector space
         e.g. man is to doctor as women is to...'''

        parser = reqparse.RequestParser()
        parser.add_argument('word1')
        parser.add_argument('word2')
        parser.add_argument('word3')

        args = parser.parse_args()  # creates dict
        word1 = args['word1']
        word2 = args['word2']
        word3 = args['word3']

        out = {'Prediction': str(model.most_similar(positive=[word2, word3], negative=[word1]))}

        return out, 200