def build_heap(data):
    swaps = []
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    size = len(data)
    
    def sift_down(i):
    
        nonlocal swaps
        max_index = i
        left_child = 2 * i + 1
        right_child = 2 * i + 2
    
        if left_child < size and data[left_child] < data [max_index]:
            max_index = left_child
        if right_child < size and data[right_child] < data [max_index]:
            max_index = right_child
        if i != max_index :
            data[i], data[max_index] = data[max_index], data[i]
            swaps.append((i, max_index))
            sift_down(max_index)
            
    for i in range(size // 2, -1, -1):
        sift_down(i)
    return swaps
        
     
def main():
    
    n = int(input().strip())
    data = list(map(int, input().split()))

  
    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
