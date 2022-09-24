#--------------------------------------
#       Dockerfile de django
#--------------------------------------
FROM python:3.8
#RUN apt-get update \ 
   # && apt-get install git -y \
    # ; apt-get install vim -y  \ 
    # ; apt-get install nano -y

WORKDIR /var/www/html/ 
RUN echo "\n Work directory created ! \n"
COPY . .
RUN echo "\n Copy files from host to container  done ! \n"
#RUN /bin/bash -c "source /var/www/html/.myvenv/bin/activate \
			#&& pip install --upgrade pip \
			#&& pip install -r requirements.txt"
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
