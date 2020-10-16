from gensim.models import KeyedVectors
from flask import Flask
from flask_restful import Api, Resource, reqparse
from predict import Similarity, mostSimilar, wordAssociation

app = Flask(__name__)
api = Api(app)

# routes to apis 
api.add_resource(Similarity, '/similarity')
api.add_resource(mostSimilar, '/mostSimilar')
api.add_resource(wordAssociation, '/wordAssociation')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)


