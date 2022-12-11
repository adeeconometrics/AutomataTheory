from typing import List, Set, TypeVar
from dataclasses import dataclass


T = TypeVar('T')


def permute(t_list: List[T], n: int) -> List[List[T]]:
    """Heap's algorithm for finding permuted combinations of `t_list`

    Args:
        t_list (List[T]): List of elements
        n (int): number of spaces to be occupied

    Returns:
        List[List[T]]: list of all permutations of `t_list` in `n`
    """
    
    permutations: List[List[T]] = []
    m_stack: List[int] = [0 for _ in range(n)]
    i: int = 1

    permutations.append(t_list)
    while i < n:
        if m_stack[i] < i:
            if i % 2 == 0:
                t_list[0], t_list[i] = t_list[i], t_list[0]
            else:
                t_list[m_stack[i]], t_list[i] = t_list[i], t_list[m_stack[i]]

            permutations.append(t_list.copy())

            m_stack[i] += 1
            i = 1
        else:
            m_stack[i] = 0
            i += 1
    return permutations

@dataclass
class CombineStack:
    n:int
    k:int
    left:int

def combine(t_list: List[T], n: int, k:int) -> List[List[T]]:
    m_stack:List[CombineStack] = []
    m_combinations:List[List[T]] = []
    index:int = 0

    m_stack.append(CombineStack(n,k,1))
    
    
    return m_combinations


if __name__ == '__main__':
    l = [1, 2, 3, 4]
    print(*[''.join(str(j) for j in i) for i in permute(l, 4)], sep='\n')
