FROM python:latest

ENV WORKSPACE=/project

ENV PATH=$PATH:$WORKSPACE

WORKDIR $WORKSPACE

COPY ./requirements.txt ./

RUN echo "alias jarvis='python $WORKSPACE/src/main.py'" >> ~/.bashrc
RUN pip install -r requirements.txt 

COPY ./ ./

CMD jarvis 
