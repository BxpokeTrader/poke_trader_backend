from django.forms import forms, ModelForm
from djongo import models
from djongo.models import TextField
import json


class Pokemon:
    def __init__(self, name, base_experience):
        self.name = name
        self.base_experience = base_experience

    def __str__(self):
        return str(json.dumps(self.__dict__))


class Trade(models.Model):
    _id = models.ObjectIdField()
    right_side = models.TextField()
    left_side = models.TextField()
    result = TextField()

    def is_fair(self):
        # TODO: improve the logic to define what is fair

        print('nome: ' + str(self.left_side) + str(self.right_side))
        print('nome2: ' + str(self.left_side) + str(self.right_side))
        if self.calculate_diff() < 10:
            return 'This trade is fair!'
        return 'This trade is unfair!'

    def calculate_diff(self):

        experience_amount_right = 0
        items = json.loads(self.right_side.replace('\'', '\"'))
        for item in items:
            print(item)
            experience_amount_right += int(item['base_expecience'])

        experience_amount_left = 0

        items = json.loads(self.left_side.replace('\'', '\"'))
        for item in items:
            experience_amount_left += int(item['base_expecience'])

        return abs(experience_amount_left - experience_amount_right)

