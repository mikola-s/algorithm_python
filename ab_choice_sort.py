def choice_sort(enter_list=list):
    """ сортировщик одномерного списка объектов методом выбора """
    stop_cycle = len(enter_list)
    for min_pos in range(stop_cycle - 1):
        for other_elem in range(min_pos + 1, stop_cycle):
            if enter_list[min_pos] > enter_list[other_elem]:
                enter_list[min_pos], enter_list[other_elem] = \
                    enter_list[other_elem], enter_list[min_pos]
    return enter_list
