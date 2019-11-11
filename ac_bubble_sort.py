def bubble_sort(enter_list=list):
    """ сортировщик одномерного списка объектов пузырьковым методом """
    stop_cycle = len(enter_list)
    for sort_round in range(stop_cycle):
        for sorted_item in range(1, stop_cycle - sort_round):
            if enter_list[sorted_item - 1] > enter_list[sorted_item]:
                enter_list[sorted_item - 1], enter_list[sorted_item] = \
                    enter_list[sorted_item], enter_list[sorted_item - 1]
    return enter_list
