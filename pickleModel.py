from gensim.models import KeyedVectors

# download vectors: https://code.google.com/archive/p/word2vec/

# Load vectors directly from the file
# NOTE: Only 1m out of 300m vectors loaded to speed up the model performance

model = KeyedVectors.load_word2vec_format('data/GoogleNews-vectors-negative300.bin.gz', binary=True, limit=1000000)

# Pickle the model 

model.save("models/model.pkl")
