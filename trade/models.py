from django.db import models
import json

from trade.fairness import Fairness


class Pokemon:
    def __init__(self, name, base_experience, image):
        self.name = name
        self.base_experience = base_experience
        self.image = image

    def __str__(self):
        return str(json.dumps(self.__dict__))


class Trade(models.Model):
    right_side = models.TextField()
    left_side = models.TextField()
    result = models.TextField()

    def is_fair(self):
        """
        Verify if this Trade is fair. It returns a string message about the fairness
        """
        fairness = Fairness(experience_weight=1)
        if fairness.is_fair(self):
            return 'This trade is fair!'
        return 'This trade is unfair!'

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

