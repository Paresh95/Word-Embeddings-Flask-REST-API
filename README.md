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
    |-- Dockerfile #a list of instructions to build a Docker container
    |-- requirements.txt #a list of python modules to be installed in a Docker container
    |-- /data
    |-- /models
    |-- /test
        |-- practice.ipynb #notebook file used for testing/practice
```

### Set-up steps

In this GitHub repo I have not included the dataset or model as they were too large to upload. Please follow steps outlined to obtain them before using this app.

1) Download the contents of this GitHub repository

2) Download the [Google News data](https://code.google.com/archive/p/word2vec/). It can be found under the section titled `Pre-trained word and phrase vectors`. The file is called `GoogleNews-vectors-negative300.bin.gz`. 

3) Place the Google News data in a folder called `data`. 

4) Create an empty folder called `models`. 

5) Run the `pickleModel.py` script. This will automatically add the model to the `models` folder. 


### How to use without Docker
 
1) `cd` into the `Word-Embeddings-Flask-REST-API` folder on your terminal. 

2) Run the Python command `python app.py` on your terminal. This will run the app on your local server.

3) To call the API use the `requests` module in Python, `curl` command on your terminal or use a platform for testing APIs such as [Postman](https://www.postman.com/)

4) There are 3 predictions you can make - similarity, most similar and word association. Examples of the curl commands for each can be found below. 


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

### How to use with Docker

1) `cd` into the `Word-Embeddings-Flask-REST-API` folder on your terminal. 

2) Install [Docker](https://docs.docker.com/get-docker/)

3) On your terminal run `docker build -t word-embedding-api .`. This tells Docker to build a container called 'word-embedding-api' from set of instructions in the Dockerfile which resides in the current working directory. 

4) Next run `docker run -p 5000:5000 word-embedding-api`. This runs your container on your local server and forwards the request from port 5000 on the host (your computer) to port 5000 in the container. 

5) Follow the steps 3 & 4 in the previous section `How to use without Docker` to use the API. 


NOTE: You can also link Docker Hub with your GitHub to automatically push any changes to build a new image. If so, this will replace steps 3 & 4.  


## Appendix

### Explaination of the Dockerfile 
```
FROM python:3.8.3
WORKDIR /project
ADD . /project
RUN pip3 -q install pip --upgrade
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["flask", "run", "-h", "0.0.0.0", "-p", "5000"]
```

- `FROM` defines the base image. This image can be found on [Docker Hub](https://hub.docker.com/).
- `WORKDIR` creates a work directory called project where the "present working directory" will be set.
- `ADD . /project` adds files from the current working directory to the folder we created in the previous step. 
- `RUN pip3 -q install pip --upgrade` upgrades the version on pip we use to the latest version
- `RUN pip install -r requirements.txt` installs the required Python modules in the container. 
- `EXPOSE 5000` lets us forward the request from port 5000 on the host to port 5000 in the container. 
- `CMD ["flask", "run", "-h", "0.0.0.0", "-p", "5000"]` runs the Flask app on host `0.0.0.0` and port `5000`


## Future improvements 

- Add authorisation token 
- Deploy on Heroku


## Sources: 

- Google News data: pe-trained vectors trained on a Google News dataset (~ 100 billion words). The model contains 300-dimensional vectors for 3 million words and phrases: https://code.google.com/archive/p/word2vec/
- Gender bias article: https://towardsdatascience.com/gender-bias-word-embeddings-76d9806a0e17
- Gensim models: https://www.shanelynn.ie/word-embeddings-in-python-with-spacy-and-gensim/
- Flask restful APIs: https://www.statworx.com/ch/blog/how-to-build-a-machine-learning-api-with-python-and-flask/
- Flask authorisation token: https://dev.to/paurakhsharma/flask-rest-api-part-3-authentication-and-authorization-5935
- Deploying a flask app to Heroku: https://stackabuse.com/deploying-a-flask-application-to-heroku/
- Creating a Docker container: https://www.youtube.com/watch?v=YFl2mCHdv24&ab_channel=JakeWright
