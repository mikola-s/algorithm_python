def insertion_sort(enter_list=list):
    """ сотрировщик одномерного списка объектов методом сдвига """
    for add_elem in range(1, len(enter_list)):
        while add_elem > 0 and enter_list[add_elem - 1] > enter_list[add_elem]:
            enter_list[add_elem - 1], enter_list[add_elem] = enter_list[add_elem], enter_list[add_elem - 1]
            add_elem -= 1
    return enter_list
