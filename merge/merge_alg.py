# 归并算法

def merge_sort(L):
    if len(L) == 1:
        return L

    # 把这个数列分成两个小的数列
    mid = len(L) // 2
    left = L[:mid]
    right = L[mid:]

    # 把两个小数列 再按照新长度的一半 把每个小数列都分成两个更小的
    L_left = merge_sort(left)
    L_right = merge_sort(right)


    return merge(L_left , L_right)


def merge(L_left, L_right):
    print('L_left:{}   L_right:{}'.format(L_left , L_right))
    result = []
    while len(L_left) > 0 and len(L_right) > 0:
        if L_left[0] <= L_right[0]:
            result.append(L_left.pop(0))
        else:
            result.append(L_right.pop(0))

    result += L_left
    result += L_right
    print('result:{}\n'.format(result))
    return result

if __name__ == '__main__':
    L = [5, 3, 7, 4, 8, 1, 9]
    result = merge_sort(L)
    print(result)