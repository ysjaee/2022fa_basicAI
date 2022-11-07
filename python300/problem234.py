def pickup_even(lists):
    result = []
    for i in lists:
        if i % 2 == 0:
            result.append(i)
    print(result)
pickup_even([3, 4, 5, 6, 7, 8])