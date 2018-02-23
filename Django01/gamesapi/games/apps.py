from django.apps import AppConfig
import django

#criar uma aplicação
#criar uma pasta com o nome do projeto 
#criar uma pasta com o nome django
#a partir do raiz do pyhton (anaconda) rodar o comando python -m venv apontando para a pasta django
# rodar o comando activate  na pasta scripts
# rodar o comando pip install django
# rodar o comando pip install djangorestframework
# abrir a pasta django
# rodar o script django-admin.py startproject nomedaapi
# abrir a pasta criada
# rodar o comando pyhton manage.py startapp game

class GameConfig(AppConfig):
    name = 'games'
