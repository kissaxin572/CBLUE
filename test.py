def quick_sort(arr):
    """
    快速排序函数

    输入:
    arr (list): 需要排序的数组

    输出:
    arr (list): 排序后的数组
    """
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]  # 选择数组的第一个元素作为基准值
        less = [x for x in arr[1:] if x <= pivot]  # 将比基准值小的元素放入less列表中
        greater = [x for x in arr[1:] if x > pivot]  # 将比基准值大的元素放入greater列表中
        return quick_sort(less) + [pivot] + quick_sort(greater)  # 递归调用quick_sort函数对less和greater进行排序，并将排序后的结果合并
    

arr = [3, 6, 8, 10, 1, 2, 1]
sorted_arr = quick_sort(arr)
print(sorted_arr)