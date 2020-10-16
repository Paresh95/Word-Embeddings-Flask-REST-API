# Word-Embeddings-Flask-REST-API

This Flask REST API allows you to extract predictions from a word embeddings model pre-trained on a Google News dataset (about 100 billion words). 

The predictions you can obtain include: 
- A similarity score between 2 words
- The top 10 most similar words and scores for a given word
- The top 10 word associations and scores for a new word given the vector association between two other words e.g. e.g. man is to doctor as women is to...
         


### Folder structure

```
~/Word-Embeddings-Flask-REST-API
    |-- pickleModel.py #python file to pickle the trained model
    |-- app.py #python file containing the flask app
    |-- predict.py #python file containing helper functions to make predictions
    |-- /data
    |-- /models
    |-- /test
        |-- practice.ipynb #notebook file used for testing/practice
```

### Set-up steps

In this GitHub repo I have not included the dataset or model as they were too large to upload. Please follow steps outlined to use this app.

1) Download the contents of this repository. 

2) Download the [Google News data](https://code.google.com/archive/p/word2vec/). It can be found under the section titled `Pre-trained word and phrase vectors`. The file is called `GoogleNews-vectors-negative300.bin.gz`. 

3) Place the Google Newsd data in the `data` folder. 

4) Run the `pickleModel.py` script. This will automatically add the model to the `models` folder. 


### How to use
 
5) `cd` into the `Word-Embeddings-Flask-REST-API` folder on your terminal. 

6) Run the Python command `python app.py` on your terminal. This will run the app on your local server.

7) To call the API use the `requests` module in Python, `curl` command on your terminal or use a platform for testing APIs such as [Postman] (https://www.postman.com/)

8) There are 3 predictions you can make - simialrity, most similar and word association. Examples of the curl commands for each can be found below. 


**Similarity:**

```
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"word1": "man", "word2": "woman"}' \
  http://0.0.0.0:5000/similarity
```

Output: 

```
{"Prediction": "0.76640123"}
```


**Most Similiar:**

```
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"word1": "man"}' \
  http://0.0.0.0:5000/mostSimilar
```

Output:

```
{"Prediction": "[('woman', 0.7664012908935547), ('boy', 0.6824870109558105), ('teenager', 0.6586930155754089), ('teenage_girl', 0.6147903800010681), ('girl', 0.5921714305877686), ('robber', 0.5585119128227234), ('Robbery_suspect', 0.5584409236907959), ('teen_ager', 0.5549196600914001), ('men', 0.5489763021469116), ('guy', 0.5420035123825073)]"}

```


**Word Association:**

```
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"word1": "man", "word2": "doctor", "word3": "woman"}' \
  http://0.0.0.0:5000/wordAssociation
```

Output:

```
{"Prediction": "[('gynecologist', 0.7093892097473145), ('nurse', 0.647728681564331), ('doctors', 0.6471461057662964), ('physician', 0.64389967918396), ('pediatrician', 0.6249487996101379), ('nurse_practitioner', 0.6218314170837402), ('obstetrician', 0.6072014570236206), ('ob_gyn', 0.5986712574958801), ('midwife', 0.5927063226699829), ('dermatologist', 0.5739566087722778)]"}
```


## Future improvements 

- add authorisation token 
- Deploy on Heroku
- Deploy on Docker 


## Sources: 

- Google News data.pre-trained vectors trained on part of Google News dataset (about 100 billion words). The model contains 300-dimensional vectors for 3 million words and phrases: https://code.google.com/archive/p/word2vec/
- Gender bias article: https://towardsdatascience.com/gender-bias-word-embeddings-76d9806a0e17
- Gensim models: https://www.shanelynn.ie/word-embeddings-in-python-with-spacy-and-gensim/
- Flask restful APIs: https://www.statworx.com/ch/blog/how-to-build-a-machine-learning-api-with-python-and-flask/
- Flask authorisation token: https://dev.to/paurakhsharma/flask-rest-api-part-3-authentication-and-authorization-5935
- Deploying a flask app to Heroku: https://stackabuse.com/deploying-a-flask-application-to-heroku/
