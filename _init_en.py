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
                            print("Solution found! Here's how to stack the cubes:")
                            print(f"Cube 1:\n  Top: {rot1[4]}\n  Bottom: {rot1[5]}\n  Front: {rot1[0]}\n  Back: {rot1[1]}\n  Right: {rot1[3]}\n  Left: {rot1[2]}")
                            print(f"Cube 2:\n  Top: {rot2[4]}\n  Bottom: {rot2[5]}\n  Front: {rot2[0]}\n  Back: {rot2[1]}\n  Right: {rot2[3]}\n  Left: {rot2[2]}")
                            print(f"Cube 3:\n  Top: {rot3[4]}\n  Bottom: {rot3[5]}\n  Front: {rot3[0]}\n  Back: {rot3[1]}\n  Right: {rot3[3]}\n  Left: {rot3[2]}")
                            print(f"Cube 4:\n  Top: {rot4[4]}\n  Bottom: {rot4[5]}\n  Front: {rot4[0]}\n  Back: {rot4[1]}\n  Right: {rot4[3]}\n  Left: {rot4[2]}")
                            return
    print("No solution found.")

cube1 = ("red", "blue", "green", "yellow", "red", "yellow")
cube2 = ("blue", "green", "red", "yellow", "blue", "red")
cube3 = ("green", "yellow", "blue", "red", "green", "blue")
cube4 = ("yellow", "red", "green", "blue", "yellow", "green")

solve_instant_insanity([cube1, cube2, cube3, cube4])
