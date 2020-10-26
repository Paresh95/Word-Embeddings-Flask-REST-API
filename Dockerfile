FROM python:3.8.3
WORKDIR /project
ADD . /project
RUN pip3 -q install pip --upgrade
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["flask", "run", "-h", "0.0.0.0", "-p", "5000"]


