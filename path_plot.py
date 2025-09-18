import json
import matplotlib.pyplot as plt

def plot_solution(instance_name, instances_file="instances.json", solution_file="solution_greedy2opt.json"):
    # read data
    with open(instances_file, "r", encoding="utf-8") as f:
        instances = json.load(f)
    with open(solution_file, "r", encoding="utf-8") as f:
        solutions = json.load(f)

    inst = instances[instance_name]
    path = solutions[instance_name]

    # path points
    xs, ys = zip(*path) if path else ([], [])

    # original points
    starts = [tuple(p) for p in inst["start_points"]]
    ends   = [tuple(p) for p in inst["end_points"]]
    goals  = [tuple(p) for p in inst.get("goal_points", [])]

 
    path_set = set(tuple(p) for p in path)

    plt.figure(figsize=(6,6))

    # start: green
    if starts:
        sx, sy = zip(*starts)
        plt.scatter(sx, sy, c="green", marker="s", s=80, label="Start")

    # end: red cross
    if ends:
        ex, ey = zip(*ends)
        plt.scatter(ex, ey, c="red", marker="X", s=100, label="End")

    # goals: 
    visited_goals = [g for g in goals if g in path_set]
    unvisited_goals = [g for g in goals if g not in path_set]

    if visited_goals:
        vx, vy = zip(*visited_goals)
        plt.scatter(vx, vy, c="black", marker="o", s=60, label="Visited Goals")
    if unvisited_goals:
        ux, uy = zip(*unvisited_goals)
        plt.scatter(ux, uy, facecolors="none", edgecolors="blue", marker="o", s=60, label="Unvisited Goals")


    if path:
        plt.plot(xs, ys, "-o", c="black", linewidth=1)

    plt.legend()
    plt.title(f"Instance: {instance_name}")
    plt.axis("equal")
    plt.show()


if __name__ == "__main__":

    # instances_to_plot = ["instance_100", "instance_021", "instance_051", "instance_081"]
    instances_to_plot = ["instance_090", "instance_100"]
    for name in instances_to_plot:
        plot_solution(name)