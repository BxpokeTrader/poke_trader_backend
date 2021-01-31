from djongo import models
from djongo.models import TextField
import json


class Pokemon:
    def __init__(self, name, base_experience, image):
        self.name = name
        self.base_experience = base_experience
        self.image = image

    def __str__(self):
        return str(json.dumps(self.__dict__))


class Trade(models.Model):
    _id = models.ObjectIdField()
    right_side = models.TextField()
    left_side = models.TextField()
    result = TextField()

    def is_fair(self):
        # TODO: improve the logic to define what is fair
        if self.calculate_diff() < 10:
            return 'This trade is fair!'
        return 'This trade is unfair!'

    def calculate_diff(self):

        experience_amount_right = 0
        for item in self.right_side:
            experience_amount_right += int(item['base_experience'])

        experience_amount_left = 0

        for item in self.left_side:
            experience_amount_left += int(item['base_experience'])

        return abs(experience_amount_left - experience_amount_right)

    def get_right_side(self):
        return json.loads(self.right_side.replace('\'', '\"'))

    def set_right_side(self, right_side):
        self.right_side = str(right_side)

    def get_left_side(self):
        return json.loads(self.left_side.replace('\'', '\"'))

    def set_left_side(self, left_side):
        self.left_side = left_side

    def toJson(self):
        data = dict()
        data['right_side'] = self.get_right_side()
        data['left_side'] = self.get_left_side()
        data['result'] = self.result
        return data

