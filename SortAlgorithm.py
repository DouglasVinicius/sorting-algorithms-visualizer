class SortAlgorithm:
    def __init__(self, dataset, sort_algorithm):
        self.__dataset = dataset
        self.__sort_algorithm

    def insertion_sort(self):
        size = len(self.__dataset)

        for first_index in range(1, size):
            current_value = self.__dataset[first_index]
            for second_index in range(first_index-1, 0, -1):
                if(self.__dataset[second_index] < current_value):
                    self.__dataset[second_index+1] = current_value
                    break
                self.swap(second_index, second_index+1)

    def bubble_sort(self):
        size = len(self.__dataset)

        for first_index in range(0, size):
            for second_index in range(0, size-first_index):
                if(self.__dataset[second_index] > self.__dataset[second_index+1]):
                    self.swap(second_index, second_index+1)

    def selection_sort(self):
        size = len(self.__dataset)

        for first_index in range(0, size):
            lower = first_index
            for second_index in range(first_index+1, size):
                if(self.__dataset[second_index] < self.__dataset[lower]):
                    lower = second_index
            self.swap(first_index, lower)

    def merge_sort(self):
        pass

    def quick_sort(self):
        pass

    def swap(self, first_value_index, second_value_index):
        self.__dataset[first_value_index], self.__dataset[second_value_index] = self.__dataset[second_value_index], self.__dataset[first_value_index]

    @property
    def dataset(self):
        return self.__dataset

    @dataset.setter
    def dataset(self, dataset):
        self.__dataset = dataset

    @property
    def sort_algorithm(self):
        return self.__sort_algorithm

    @sort_algorithm.setter
    def sort_algorithm(self, sort_algorithm):
        self.__sort_algorithm = sort_algorithm
