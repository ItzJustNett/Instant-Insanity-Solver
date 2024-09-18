def generate_rotations(cube):
    f, b, l, r, t, bt = cube
    return [
        (f, b, l, r, t, bt),
        (f, b, r, l, t, bt),
        (l, r, b, f, t, bt),
        (l, r, f, b, t, bt),
        (r, l, b, f, t, bt),
        (r, l, f, b, t, bt),
    ]

def is_valid_solution(cube_stack):
    fronts = [cube[0] for cube in cube_stack]
    backs = [cube[1] for cube in cube_stack]
    lefts = [cube[2] for cube in cube_stack]
    rights = [cube[3] for cube in cube_stack]
    
    return len(set(fronts)) == 4 and len(set(backs)) == 4 and len(set(lefts)) == 4 and len(set(rights)) == 4

def permute(arr):
    if len(arr) == 0:
        return [[]]
    permutations = []
    for i in range(len(arr)):
        element = arr[i]
        rest = arr[:i] + arr[i+1:]
        for p in permute(rest):
            permutations.append([element] + p)
    return permutations

def solve_instant_insanity(cubes):
    all_rotations = [generate_rotations(cube) for cube in cubes]
    cube_permutations = permute([0, 1, 2, 3])

    for permutation in cube_permutations:
        for rot1 in all_rotations[permutation[0]]:
            for rot2 in all_rotations[permutation[1]]:
                for rot3 in all_rotations[permutation[2]]:
                    for rot4 in all_rotations[permutation[3]]:
                        cube_stack = [rot1, rot2, rot3, rot4]
                        if is_valid_solution(cube_stack):
                            print("Знайдено рішення! Ось як скласти кубики:")
                            print(f"Кубик 1:\n  Верх: {rot1[4]}\n  Низ: {rot1[5]}\n  Перед: {rot1[0]}\n  Зад: {rot1[1]}\n  Право: {rot1[3]}\n  Ліво: {rot1[2]}")
                            print(f"Кубик 2:\n  Верх: {rot2[4]}\n  Низ: {rot2[5]}\n  Перед: {rot2[0]}\n  Зад: {rot2[1]}\n  Право: {rot2[3]}\n  Ліво: {rot2[2]}")
                            print(f"Кубик 3:\n  Верх: {rot3[4]}\n  Низ: {rot3[5]}\n  Перед: {rot3[0]}\n  Зад: {rot3[1]}\n  Право: {rot3[3]}\n  Ліво: {rot3[2]}")
                            print(f"Кубик 4:\n  Верх: {rot4[4]}\n  Низ: {rot4[5]}\n  Перед: {rot4[0]}\n  Зад: {rot4[1]}\n  Право: {rot4[3]}\n  Ліво: {rot4[2]}")
                            return
    print("Рішення не знайдено.")

cube1 = ("червоний", "синій", "зелений", "жовтий", "червоний", "жовтий")
cube2 = ("синій", "зелений", "червоний", "жовтий", "синій", "червоний")
cube3 = ("зелений", "жовтий", "синій", "червоний", "зелений", "синій")
cube4 = ("жовтий", "червоний", "зелений", "синій", "жовтий", "зелений")

solve_instant_insanity([cube1, cube2, cube3, cube4])
