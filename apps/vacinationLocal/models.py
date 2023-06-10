from django.db import models

class vacinationLocal:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco

    # Getters e Setters

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_endereco(self):
        return self.endereco

    def set_endereco(self, endereco):
        self.endereco = endereco
