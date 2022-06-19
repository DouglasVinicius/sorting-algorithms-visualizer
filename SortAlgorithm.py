class SortAlgorithm:

    def bubble_sort(visualizer, ascending, dataset):
        size = len(dataset)

        for first_index in range(size-1):
            for second_index in range(size-first_index-1):
                visualizer.comparisons += 1
                visualizer.draw_writer(True)
                visualizer.draw_dataset(second_index+1, size-1-first_index, second_index, False)
                yield True

                if((dataset[second_index] > dataset[second_index+1] and ascending) or (dataset[second_index] < dataset[second_index+1] and not ascending)):
                    SortAlgorithm.swap(dataset, second_index, second_index+1)

        return dataset


    def insertion_sort(visualizer, ascending, dataset):
        size = len(dataset)

        for first_index in range(1, size):
            current_value = dataset[first_index]
            for second_index in range(first_index-1, -1, -1):
                visualizer.comparisons += 1
                visualizer.draw_writer(True)
                visualizer.draw_dataset(second_index, first_index+1, second_index+1, True)
                yield True

                if((dataset[second_index] < current_value and ascending) or (dataset[second_index] > current_value and not ascending)):
                    dataset[second_index+1] = current_value
                    break
                SortAlgorithm.swap(dataset, second_index, second_index+1)

        return dataset


    def selection_sort(visualizer, ascending, dataset):
        size = len(dataset)

        for first_index in range(0, size):
            lower = first_index
            for second_index in range(first_index+1, size):
                visualizer.comparisons += 1
                visualizer.draw_writer(True)
                visualizer.draw_dataset(second_index, first_index, lower, True)
                yield True

                if((dataset[second_index] < dataset[lower] and ascending) or (dataset[second_index] > dataset[lower] and not ascending)):
                    lower = second_index
            SortAlgorithm.swap(dataset, first_index, lower)

        return dataset


    def merge_sort(self):
        pass


    def quick_sort(self):
        pass


    def swap(dataset, first_value_index, second_value_index):
        dataset[first_value_index], dataset[second_value_index] = dataset[second_value_index], dataset[first_value_index]