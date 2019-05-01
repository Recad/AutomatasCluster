#Imagen Base
FROM python:3.5.7-jessie

#Actualización e instalación 
ADD requirements.txt /home
RUN pip3 install -r /home/requirements.txt

