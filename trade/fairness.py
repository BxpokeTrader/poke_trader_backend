import requests


class Fairness:
    def __init__(self, experience_weight=0.8):
        self.experience_weight = experience_weight
        self.rarity_weight = 1 - self.experience_weight

    def is_fair(self, trade):
        """
        This method verify if a Trade is fair or not. To do it, is used a weight data related to the amount experience
        of the Trade sides. The weight has a maximum value of 1, which means that justice will be defined exclusively
        based on the base_experience attribute. On the other hand, if experience_weight is less than 1, the remaining
        value defines the degree of importance of the number of places where the pokemon can be found (The harder it
        is to find, the more valuable!).
        """
        right_experience_amount = self.get_experience_amount(trade.right_side)
        left_experience_amount = self.get_experience_amount(trade.left_side)

        right_experience_value = right_experience_amount * self.experience_weight
        left_experience_value = left_experience_amount * self.experience_weight

        if self.rarity_weight > 0:
            right_rarity = self.get_rarity_amount(trade.right_side) * self.rarity_weight
            left_rarity = self.get_rarity_amount(trade.left_side) * self.rarity_weight
            right_final_value = right_experience_value - right_rarity
            left_final_value = left_experience_value - left_rarity
        else:
            right_final_value = right_experience_value
            left_final_value = left_experience_value

        return abs(right_final_value - left_final_value) < 20

    def get_experience_amount(self, pokemons):
        experience_sum = 0

        for pokemon in pokemons:
            experience_sum += pokemon['base_experience']

        return experience_sum

    def get_rarity_amount(self, pokemons):
        locals_count = 0
        for pokemon in pokemons:
            locals_count += self.count_locals(pokemon)
        return locals_count

    @staticmethod
    def count_locals(pokemon):
        result = requests.get('https://pokeapi.co/api/v2/pokemon/' + pokemon['name']).json()
        result = requests.get(result['location_area_encounters']).json()

        return len(result)
