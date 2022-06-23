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
        merge_level = 0
        subset_size = (2**merge_level)*2
        dataset_size = len(dataset)

        while(subset_size < dataset_size):
            for subset_init in range(0, dataset_size, subset_size):
                middle = (subset_init + (subset_init + subset_size)) // 2
                first_subset_part = dataset[subset_init : middle]
                first_subset_index = 0
                second_subset_part = dataset[middle : (subset_init + subset_size)]
                second_subset_index = 0

                for subset_index in range(subset_init, subset_init+subset_size):
                    if((first_subset_index < subset_size // 2) and (second_subset_index < subset_size - subset_size // 2)):
                        if((first_subset_part[first_subset_index] < second_subset_part[second_subset_index] and ascending) or (first_subset_part[first_subset_index] > second_subset_part[second_subset_index] and not ascending)):
                            dataset[subset_index] = first_subset_part[first_subset_index]
                            first_subset_index += 1
                        else:
                            dataset[subset_index] = second_subset_part[second_subset_index]
                            second_subset_index += 1
                    elif(first_subset_index < subset_size // 2):
                        dataset[subset_index] = first_subset_part[first_subset_index]
                        first_subset_index += 1
                    else:
                        dataset[subset_index] = second_subset_part[second_subset_index]
                        second_subset_index += 1
                    

            merge_level += 1
            subset_size = (2**merge_level)*2


    def quick_sort(visualizer, ascending, dataset):
        pass


    def swap(dataset, first_value_index, second_value_index):
        dataset[first_value_index], dataset[second_value_index] = dataset[second_value_index], dataset[first_value_index]


    # def merge_sort_test(ascending, dataset):
    #     merge_level = 0
    #     subset_size = (2**merge_level)*2
    #     dataset_size = len(dataset)

    #     while(subset_size < dataset_size):
    #         for subset_init in range(0, dataset_size, subset_size):
    #             if(subset_init + subset_size < dataset_size):
    #                 max_subset_size = (subset_init + subset_size)
    #             else:
    #                 max_subset_size = dataset_size
    #                 #if(((subset_init + max_subset_size) // 2) - subset_init == 0):
    #                 #    continue

    #             # middle = (subset_init + max_subset_size) // 2
    #             middle = (subset_init + max_subset_size) / 2
    #             if(middle > (subset_init + max_subset_size) // 2):
    #                middle = int(middle)+1
    #             else:
    #                middle = int(middle)
    #             first_subset_part = dataset[subset_init : middle]
    #             first_subset_index = 0
    #             second_subset_part = dataset[middle : (subset_init + subset_size)]
    #             second_subset_index = 0

    #             for subset_index in range(subset_init, max_subset_size):
    #                 print(f"{first_subset_index}, {second_subset_index}, {subset_index}")
    #                 print(f"{dataset}\n")
    #                 print(f"{first_subset_part}\n")
    #                 print(f"{second_subset_part}\n")
    #                 # print(f"{first_subset_part[first_subset_index]}, {second_subset_part[second_subset_index]}")
    #                 if((first_subset_index < subset_size // 2) and (second_subset_index < max_subset_size - middle) and (len(second_subset_part) != 0) and (len(first_subset_part) != 0)):
    #                     if((first_subset_part[first_subset_index] < second_subset_part[second_subset_index] and ascending) or (first_subset_part[first_subset_index] > second_subset_part[second_subset_index] and not ascending)):
    #                         dataset[subset_index] = first_subset_part[first_subset_index]
    #                         first_subset_index += 1
    #                     else:
    #                         dataset[subset_index] = second_subset_part[second_subset_index]
    #                         second_subset_index += 1
    #                 elif((first_subset_index < subset_size // 2) and len(first_subset_part) != 0):
    #                     dataset[subset_index] = first_subset_part[first_subset_index]
    #                     first_subset_index += 1
    #                 elif(len(second_subset_part)):
    #                     dataset[subset_index] = second_subset_part[second_subset_index]
    #                     second_subset_index += 1
                    

    #         merge_level += 1
    #         subset_size = (2**merge_level)*2

    #     return dataset

#dataset = []
#with open("random_file.dat", "r") as file:
#    for value in file.readlines():
#        dataset.append(int(value))

#print(dataset)
#print(SortAlgorithm.merge_sort_test(True, dataset))