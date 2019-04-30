#Imagen Base
FROM python:3.5.7-jessie

#Actualización e instalación 
ADD requirements.txt
RUN pip3 install -r requirements.txt

