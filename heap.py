import heapq

'''
Priority Queue is abstract, and a Heap is a concrete implementation of it

Heap is a tree data structure

my_heap = 
T1 - 5
T2 - 4
T3 - 7
T4 - 9
T5 - 2
T6 - 6

lower number -> important task

so...

my_heap.next() = T5
my_heap.next() = T2
my_heap.next() = T1

my_heap = 
T3 - 7
T4 - 9
T6 - 6

also want that, when we add new element, it is structure in proper way

my_heap.add(3)

my_heap = 
T3 - 7
T4 - 9
T6 - 6
T1 - 3

my_heap.next() = T1

'''


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    data = [10, 20, 43, 1, 2, 65, 17, 44, 2, 3, 1]
    print(f'List: ', data)

    heapq.heapify(data)
    print(f'Heapify: ', data)

    heapq.heappop(data)
    print(f'Popping: ', data)

    heapq.heappush(data, 2)
    print(f'Pushing: ', data)


    print('\nMax Heap')
    print('\nNot built into heapq library and should make your own, BUT there are tricks')
    print('\n\t1) Invert/negate all values')
    data_negative = [-x for x in data]
    print(f'Data (Negated) = ', data_negative)
    heapq.heapify(data_negative)
    print(f'Heapify: ', data_negative)
    heapq.heappop(data_negative)
    print(f'Popping: ', data_negative)
    print('\nCan have your own functions for negating result that use heapq functions')

    print('\n\t2) Use undocumented functions')
    heapq._heapify_max(data)
    print(f'heapq._heapify_max(data): ', data)
    heapq._heappop_max(data)
    print(f'heapq._heappop_max(data): ', data)


    print('\nMerge two lists into one heap')
    l1 = [10, 20, 30, 40, 50]
    print(f'l1 = ', l1)
    l2 = [15, 25, 35, 45, 55]
    print(f'l2 = ', l2)

    # need list() because heapq.merge is a generator
    l3 = list(heapq.merge(l1, l2))
    print(f'Heap of merged lists l1 and l2 = ', l3)







