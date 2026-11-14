"""Exact finite checks for null tensor summands; Python standard library only."""

from collections import Counter
from itertools import product
from math import comb as combination


def basis(vectors):
    pivots = {}
    for vector in vectors:
        while vector:
            pivot = vector.bit_length() - 1
            if pivot in pivots:
                vector ^= pivots[pivot]
            else:
                pivots[pivot] = vector
                break
    return tuple(pivots.values())


def rank(vectors):
    return len(basis(vectors))


def kernel(rows, dimension):
    rows = list(rows)
    pivots = []
    height = 0
    for column in range(dimension):
        pivot = next((index for index in range(height, len(rows))
                      if rows[index] >> column & 1), None)
        if pivot is None:
            continue
        rows[height], rows[pivot] = rows[pivot], rows[height]
        for index in range(len(rows)):
            if index != height and rows[index] >> column & 1:
                rows[index] ^= rows[height]
        pivots.append(column)
        height += 1
    return tuple((1 << free) | sum(((rows[index] >> free) & 1) << column
                                  for index, column in enumerate(pivots))
                 for free in range(dimension) if free not in pivots)


def transpose(matrix):
    return tuple(sum(((row >> column) & 1) << index
                     for index, row in enumerate(matrix))
                 for column in range(len(matrix)))


def apply(matrix, vector):
    return sum(((row & vector).bit_count() & 1) << index
               for index, row in enumerate(matrix))


def compose(left, right):
    return transpose(tuple(apply(left, column) for column in transpose(right)))


def tensor_product(left, right):
    dimension = len(right)
    return tuple(sum((right_row if left_row >> index & 1 else 0)
                     << (index * dimension) for index in range(len(left)))
                 for left_row in left for right_row in right)


def tensor_power(matrix, exponent):
    result = (1,)
    for _ in range(exponent):
        result = tensor_product(result, matrix)
    return result


def member(vector, spanning_basis):
    return rank((*spanning_basis, vector)) == len(spanning_basis)


def null_splitting(actions):
    dimension = len(actions[0])
    common_kernel = kernel(tuple(row for action in actions for row in action), dimension)
    common_image = basis(column for action in actions for column in transpose(action))
    intersection_dimension = (len(common_kernel) + len(common_image)
                              - rank((*common_kernel, *common_image)))
    multiplicity = len(common_kernel) - intersection_dimension
    dual_kernel = kernel(tuple(row for action in actions for row in transpose(action)), dimension)
    pairing = tuple(sum(((functional & vector).bit_count() & 1) << index
                        for index, vector in enumerate(common_kernel))
                    for functional in dual_kernel)
    assert rank(pairing) == multiplicity
    null_basis = []
    for vector in common_kernel:
        if rank((*common_image, *null_basis, vector)) > len(common_image) + len(null_basis):
            null_basis.append(vector)
    assert len(null_basis) == multiplicity
    complement_basis = list(common_image)
    for index in range(dimension):
        vector = 1 << index
        if rank((*null_basis, *complement_basis, vector)) > len(null_basis) + len(complement_basis):
            complement_basis.append(vector)
    assert len(null_basis) + len(complement_basis) == dimension
    assert rank((*null_basis, *complement_basis)) == dimension
    assert all(apply(action, vector) == 0 for action in actions for vector in null_basis)
    assert all(member(apply(action, vector), complement_basis)
               for action in actions for vector in complement_basis)
    rank_sum = sum(rank(action) for action in actions)
    assert len(common_image) <= rank_sum
    assert dimension - len(common_kernel) <= rank_sum
    assert multiplicity >= dimension - 2 * rank_sum
    return multiplicity


def fusion_matrix():
    matrix = ((0, 0, 0, 0), (1, 0, 0, 0), (0, 28, 6, 40), (0, 1, 0, 1))
    dimensions = (1, 6, 1, 8)
    assert all(sum(dimensions[row] * matrix[row][column] for row in range(4))
               == 6 * dimensions[column] for column in range(4))
    vector = (1, 0, 0, 0)
    counts = []
    for exponent in range(13):
        assert sum(dimension * count for dimension, count in zip(dimensions, vector)) == 6 ** exponent
        counts.append(sum(vector))
        if exponent >= 2:
            assert vector == (0, 0, 6 ** exponent - 8, 1)
            assert sum(vector) == 6 ** exponent - 7
        vector = tuple(sum(matrix[row][column] * vector[column] for column in range(4))
                       for row in range(4))
    assert counts[:6] == [1, 1, 29, 209, 1289, 7769]
    print('EXAMPLE 4.3: b(0..5)=[1, 1, 29, 209, 1289, 7769]')
    print('EXAMPLE 4.3: null multiplicity 28 at n=2; b(n)=6^n-7 checked for 2<=n<=12')


def binary_families():
    matrices = tuple(tuple(rows) for rows in product(range(4), repeat=2))
    singular = tuple(matrix for matrix in matrices if rank(matrix) < 2)
    assert len(singular) == 10
    lookup = {matrix: index for index, matrix in enumerate(singular)}
    multiplication = tuple(tuple(lookup[compose(left, right)] for right in singular)
                           for left in singular)
    tensors = {(index, exponent): tensor_power(matrix, exponent)
               for index, matrix in enumerate(singular) for exponent in (1, 2, 3)}
    assert all(rank(tensors[index, exponent]) == rank(matrix) ** exponent
               for index, matrix in enumerate(singular) for exponent in (1, 2, 3))
    tensor_cases = closed_families = nonunital_families = 0
    for mask in range(1, 1 << len(singular)):
        indices = tuple(index for index in range(len(singular)) if mask >> index & 1)
        actions = tuple(singular[index] for index in indices)
        closed = all(mask >> multiplication[left][right] & 1 for left in indices for right in indices)
        if closed:
            closed_families += 1
            identity = any(all(multiplication[candidate][index] == multiplication[index][candidate] == index
                               for index in indices) for candidate in indices)
            nonunital_families += not identity
        projections = tuple(projection for projection in matrices
                            if compose(projection, projection) == projection
                            and all(compose(action, projection) == compose(projection, action) == (0, 0)
                                    for action in actions))
        assert null_splitting(actions) == max(rank(projection) for projection in projections)
        for exponent in (1, 2, 3):
            multiplicity = null_splitting(tuple(tensors[index, exponent] for index in indices))
            assert multiplicity >= 2 ** exponent - 2 * sum(rank(action) ** exponent for action in actions)
            tensor_cases += 1
    assert (tensor_cases, closed_families, nonunital_families) == (3069, 92, 79)
    exponent = 1
    while 2 ** exponent <= 2 * sum(rank(matrix) ** exponent for matrix in singular):
        exponent += 1
    multiplicity = null_splitting(tuple(tensor_power(matrix, exponent) for matrix in singular))
    lower_bound = 2 ** exponent - 2 * sum(rank(matrix) ** exponent for matrix in singular)
    assert (exponent, lower_bound, multiplicity) == (5, 14, 28)
    print('GF(2): all 1023 nonempty singular 2x2 matrix families; 3069 tensor cases n=1,2,3')
    print('GF(2): 92 closed families, 79 without identity; all n=1 null projections exhausted')
    print('GF(2) full family: n=5, lower bound=14, maximal null multiplicity=28')


def jordan_chains():
    cases = 0
    for dimension in range(2, 7):
        for exponent in range(1, 6):
            vertices = tuple(product(range(dimension), repeat=exponent))
            successor = {vertex: tuple(coordinate - 1 for coordinate in vertex)
                         for vertex in vertices if all(vertex)}
            starts = set(vertices) - set(successor.values())
            blocks = Counter()
            visited = set()
            for start in starts:
                vertex = start
                length = 1
                visited.add(vertex)
                while vertex in successor:
                    vertex = successor[vertex]
                    assert vertex not in visited
                    visited.add(vertex)
                    length += 1
                blocks[length] += 1
            assert visited == set(vertices)
            assert sum(length * count for length, count in blocks.items()) == dimension ** exponent
            assert len(successor) == (dimension - 1) ** exponent
            assert sum(vertex in successor and successor[vertex] in successor
                       for vertex in vertices) == (dimension - 2) ** exponent
            assert blocks[1] == dimension ** exponent - 2 * (dimension - 1) ** exponent + (dimension - 2) ** exponent
            assert sum(blocks.values()) == dimension ** exponent - (dimension - 1) ** exponent
            for block_size in range(1, dimension + 1):
                expected = ((dimension - block_size + 1) ** exponent
                            - 2 * (dimension - block_size) ** exponent
                            + max(dimension - block_size - 1, 0) ** exponent)
                assert blocks[block_size] == expected
            cases += 1
    assert cases == 25
    print('JORDAN: 25 coordinate-chain decompositions, 2<=d<=6 and 1<=n<=5')
    print('JORDAN: mu=d^n-2(d-1)^n+(d-2)^n; b=d^n-(d-1)^n in every case')
    print('JORDAN: every block-size multiplicity agrees with the second rank difference')


def right_zero_decompositions():
    first_action = (1, 0)
    second_action = (3, 0)
    assert compose(first_action, second_action) == second_action
    assert compose(second_action, first_action) == first_action
    assert compose(first_action, first_action) == first_action
    assert compose(second_action, second_action) == second_action
    for exponent in range(1, 8):
        first = tensor_power(first_action, exponent)
        second = tensor_power(second_action, exponent)
        dimension = 2 ** exponent
        assert rank(first) == rank(second) == 1
        assert rank((*first, *second)) == 2
        assert null_splitting((first, second)) == dimension - 2
        null_vectors = tuple((1 << index) | (1 << (dimension - 1))
                             for index in range(1, dimension - 1))
        distinguished = (1, 1 << (dimension - 1))
        assert rank((*distinguished, *null_vectors)) == dimension
        assert all(apply(action, vector) == 0
                   for action in (first, second) for vector in null_vectors)
        assert apply(first, distinguished[0]) == distinguished[0]
        assert apply(first, distinguished[1]) == 0
        assert apply(second, distinguished[0]) == distinguished[0]
        assert apply(second, distinguished[1]) == distinguished[0]
        assert 1 + len(null_vectors) == dimension - 1
    print('RIGHT-ZERO: explicit GF(2) decompositions V^(tensor n)=V+Z^(2^n-2), 1<=n<=7')
    print('RIGHT-ZERO: b(n)=2^n-1 in those seven cases; the uniform composition-ratio assertion has a written proof')


def earlier_semigroup_example():
    fusion = ((0, 0, 1), (0, 0, 1), (1, 1, 1))
    dimensions = (1, 1, 2)
    vector = (1, 0, 0)
    for exponent in range(1, 13):
        vector = tuple(sum(fusion[row][column] * vector[column]
                           for column in range(3)) for row in range(3))
        assert sum(value * dimension for value, dimension in zip(vector, dimensions)) == 2 ** exponent
        assert sum(vector) == (2 ** (exponent + 1) + (-1) ** exponent) // 3
        null_count = sum(2 ** choices * combination(exponent, choices)
                         for choices in range(1, exponent))
        assert null_count == 3 ** exponent - 2 ** exponent - 1
        total_count = null_count + 1 + sum(vector)
        assert total_count == 3 ** exponent - (2 ** exponent - (-1) ** exponent) // 3
    print('EARLIER EXAMPLE: C2+S3+zero, mu=3^n-2^n-1 and b=3^n-(2^n-(-1)^n)/3, 1<=n<=12')


if __name__ == '__main__':
    fusion_matrix()
    binary_families()
    jordan_chains()
    right_zero_decompositions()
    earlier_semigroup_example()
    print('ALL_CHECKS_OK')
