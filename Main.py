""" circular doubly linked list """


length_of_circular_linked_list = int(input())

circular_linked_list = list(map(int,input().strip().split(" ")))


actual_list = []

index = 0
while len(actual_list) < length_of_circular_linked_list and index < len(circular_linked_list):
    element = circular_linked_list[index]
    if element not in actual_list:
        actual_list.append(element)
    index += 1

print(len(actual_list))
print(" ".join(str(num) for num in actual_list))
