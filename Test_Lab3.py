import Lab3

print("Test_Lab3")


def test_bubble_sort_ascending():
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [11, 12, 22, 25, 34, 64, 90]

    if len(input_arr)<10 :
        result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)
        assert (result == test_arr)
    else:
        print("Input array more than 10")

def test_bubble_sort_descending():
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [90, 64, 34, 25, 22, 12, 11]

    if len(input_arr)<10 :
        result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)
        assert (result == test_arr)
    else:
        print("Input array more than 10")

def test_dubble_sort_EMto10():
    input_arr = [64, 34, 25, 12, 22, 11, 66,88,90,11,23]
    if len(input_arr) >= 10:
            return 1

def test_dubble_sort_zero():
    input_arr = []
    if len(input_arr) == 0:
        return 0


def test_bubble_sort_invalid():
    result = []
    input_arr = [64, 34, '25', 12, 22, 11, 90]

    result = Lab3.bubble_sort(input_arr, 3)

    assert (result == 2)