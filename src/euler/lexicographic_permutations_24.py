def fact(n):
    if n <= 1:
        return 1
    return n * fact(n-1)


def nth_lexiperm(atoms, n):
    atoms.sort()
    solution = []

    while atoms:
        size = len(atoms)

        i = 0
        while fact(i) < n:
            i += 1

        if i < size:
            solution.extend(atoms[:size-i])
            atoms = atoms[size-i:]
            continue

        j = 1
        while fact(i - 1) * j < n:
            j += 1
        
        solution.append(atoms.pop(j-1))
        n -= fact(i - 1) * (j -1)
        
    print(''.join(str(x) for x in solution))
