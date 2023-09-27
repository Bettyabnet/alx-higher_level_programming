#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []

    try:
        for i in range(list_length):
            try:
                a = my_list_1[i]
                b = my_list_2[i]

                if isinstance(a, (int, float)) and isinstance(b, (int, float)):
                    try:
                        division_result = a / b
                        result.append(division_result)
                    except ZeroDivisionError:
                        result.append(0)
                        print("division by 0")
                else:
                    result.append(0)
                    print("wrong type")

            except IndexError:
                result.append(0)
                print("out of range")
    finally:
        return result
