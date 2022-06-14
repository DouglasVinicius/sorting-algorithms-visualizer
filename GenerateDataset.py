import random

class GenerateDataset:
    
    def __init__(self, number_of_values, max_value, min_value):
        self.__number_of_values = 1 if (number_of_values < 1) else number_of_values
        self.__min_value = min_value
        self.__max_value = self.__min_value + self.__number_of_values if (max_value < (self.__min_value + self.__number_of_values)) else max_value

    def generate_random_dataset(self):
        dataset = []
        for element in range(self.__number_of_values):
            value = random.randint(self.__min_value, self.__max_value)
            dataset.append(value)

        return dataset