import math

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


    def merge_sort(visualizer, ascending, dataset):
        merge_level = 1
        subset_size = (2**merge_level)
        dataset_size = len(dataset)
        
        logtwo_roundup = int(math.log2(dataset_size))
        if(logtwo_roundup < math.log2(dataset_size)):
            logtwo_roundup += 1

        while(merge_level <= logtwo_roundup):
            subset_index, first_subset_index, second_subset_index, first_subset, second_subset = SortAlgorithm.new_subsets_elements()
            for element_index in range(dataset_size):
                if(element_index % subset_size == 0):
                    first_subset_index, second_subset_index, first_subset, second_subset = SortAlgorithm.update_subsets_elements(dataset, subset_index*subset_size, subset_size)
                    subset_index += 1

                if((first_subset_index < len(first_subset)) and (second_subset_index < len(second_subset))):
                    if(((first_subset[first_subset_index] < second_subset[second_subset_index]) and ascending) or ((first_subset[first_subset_index] > second_subset[second_subset_index]) and not ascending)):
                        dataset[element_index] = first_subset[first_subset_index]
                        first_subset_index += 1
                    else:
                        dataset[element_index] = second_subset[second_subset_index]
                        second_subset_index += 1
                elif(first_subset_index < len(first_subset)):
                    dataset[element_index] = first_subset[first_subset_index]
                    first_subset_index += 1
                else:
                    dataset[element_index] = second_subset[second_subset_index]
                    second_subset_index += 1

                visualizer.comparisons += 1
                visualizer.draw_writer(True)
                if(merge_level != logtwo_roundup):
                    visualizer.draw_dataset(color_position_red = subset_index*subset_size+first_subset_index, color_position_blue = subset_index*subset_size+second_subset_index)
                else:
                    visualizer.draw_dataset(subset_index*subset_size+first_subset_index, element_index, subset_index*subset_size+second_subset_index)
                yield True        

            merge_level += 1
            subset_size = (2**merge_level)
    
        return dataset


    def quick_sort(visualizer, ascending, dataset):
        pass  


    def swap(dataset, first_value_index, second_value_index):
        dataset[first_value_index], dataset[second_value_index] = dataset[second_value_index], dataset[first_value_index]


    def update_subsets_elements(dataset, start_of_subset, subset_size):
        end_of_subset = start_of_subset + subset_size
        middle_of_dataset = (start_of_subset + end_of_subset) // 2

        first_subset_index = 0
        second_subset_index = 0
        first_subset = dataset[start_of_subset : middle_of_dataset]
        if(start_of_subset + subset_size > len(dataset)):
            second_subset = dataset[middle_of_dataset : len(dataset)]
        else:
            second_subset = dataset[middle_of_dataset : end_of_subset]

        return first_subset_index, second_subset_index, first_subset, second_subset

    def new_subsets_elements():
        subset_index = 0
        first_subset_index = 0
        second_subset_index = 0
        first_subset = []
        second_subset = []

        return subset_index, first_subset_index, second_subset_index, first_subset, second_subset