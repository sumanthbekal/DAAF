from itertools import permutations

def dist(p1, p2):
    return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**0.5

def total_dist(p, d, toolbox_time):
    return sum(d[p[i]][p[i+1]] for i in range(len(p)-1)) + (len(p) - 1) * toolbox_time

def find_optimal_drilling_time(points, toolbox_time):
    n = len(points)
    d = [[dist(p1, p2) for p2 in points] for p1 in points]
    perms = permutations(range(n))
    optimal_time = min(total_dist(perm, d, toolbox_time) for perm in perms)
    return optimal_time

def main():
    points = [(0, 0, 1), (3, 0, 2), (0, 4, 1), (3, 4, 2)]
    toolbox_time = 5
    print("Optimal Drilling Time:", find_optimal_drilling_time(points, toolbox_time))

if __name__ == "__main__":
    main()
