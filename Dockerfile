FROM jenkins/jenkins:lts
USER root
RUN apt update && apt install -y python3 && apt install -y python3-pip

COPY ./project_demo/requirements.txt /home/jenkins/project_demo
#RUN mkdir -p /home/jenkins/project_demo

RUN ["/bin/bash","-c","pip3" ,"install", "--upgrade" ,"pip3"]
RUN ["/bin/bash", "-c","pip3","install","-r","/home/jenkins/project_demo/requirements.txt"]
# RUN ["rm" ,"-r", "chromedriver", "chromedriver_linux64.zip"]
# RUN curl https://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_linux64.zip -O && \
#     unzip chromedriver_linux64.zip

USER jenkins