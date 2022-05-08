input_array = [1, 1, 4, 2, 4, 4]
id_id = []


def quick_find_init():
    """
    Big O - O(n) - need to go through whole array
    """
    # id = []
    for i in range(len(input_array)):
        id_id.append(input_array[i])


def union(p: int, q: int):
    """
    Big O - O(n)
    """
    pid = id_id[p]
    qid = id_id[q]
    for i in range(len(id_id)):
        if id_id[i] == pid:
            id_id[i] = qid


def find(p, q) -> bool:
    """
    Big O - O(1) - look up id in the id array
    """
    return id_id[p] == id_id[q]


def quick_union():
    """
    represent elements as trees and if they are in the same tree they are also in the same set.

    """


quick_find_init()
val = find(0, 1)

print(val)
