def type_logger(r):
    from functools import wraps
    @wraps(r)
    def tag_wrapper(*num, **nums):
        arr = [i for i in (*num, *nums.values())]
        arr_of_string = [f'type_logger ({arr[i]}:{type(arr[i])})' for i in range(len(arr))]
        print(*arr_of_string, *r(*num, **nums), sep=',\n')
        return tag_wrapper


@type_logger
def calc_cube(*j, **l):
    arr_3 = [_ for _ in (*j, *l.values()) if type(_)==int or type(_)==float]
    return [x ** 3 for x in arr_3]


arr_2 = calc_cube(5)
print(arr_2)
