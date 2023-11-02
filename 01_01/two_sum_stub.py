# 2-Sum Interview Problem

def two_sum_problem(arr, target):
    list = []
    x = -1
    for i in arr:
        y = 0
        x+=1
        for n in arr:
            if i + n == target and x != y:
                sub_list = x, y
                #list.append(sub_list)
            else:
                y +=1
    return sub_list #list.append(sub_list)
                


assert two_sum_problem([1, 2, 3], 4) in [(0, 2), (2, 0)]
assert two_sum_problem([1234, 5678, 9012], 14690) in [(1, 2), (2, 1)]
assert two_sum_problem([2, 2, 3], 4) in [(0, 1), (1, 0)]
assert two_sum_problem([2, 2], 4) in [(0, 1), (1, 0)]
assert two_sum_problem([8, 7, 2, 5, 3, 1], 10) in [(0, 2), (2, 0), (1, 4), (4, 1)]


arr = [1234, 5678, 9012]

target = 14690

print(two_sum_problem(arr, target))