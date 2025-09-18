import json
import matplotlib.pyplot as plt

def plot_solution(instance_name, instances_file="instances.json", solution_file="solution_greedy2opt.json"):
    # 读数据
    with open(instances_file, "r", encoding="utf-8") as f:
        instances = json.load(f)
    with open(solution_file, "r", encoding="utf-8") as f:
        solutions = json.load(f)

    inst = instances[instance_name]
    path = solutions[instance_name]

    # 路径点
    xs, ys = zip(*path) if path else ([], [])

    # 原始点集
    starts = [tuple(p) for p in inst["start_points"]]
    ends   = [tuple(p) for p in inst["end_points"]]
    goals  = [tuple(p) for p in inst.get("goal_points", [])]

    # 路径走过的点
    path_set = set(tuple(p) for p in path)

    plt.figure(figsize=(6,6))

    # start: 绿色方块
    if starts:
        sx, sy = zip(*starts)
        plt.scatter(sx, sy, c="green", marker="s", s=80, label="Start")

    # end: 红色叉号
    if ends:
        ex, ey = zip(*ends)
        plt.scatter(ex, ey, c="red", marker="X", s=100, label="End")

    # goals: 区分走过/没走过
    visited_goals = [g for g in goals if g in path_set]
    unvisited_goals = [g for g in goals if g not in path_set]

    if visited_goals:
        vx, vy = zip(*visited_goals)
        plt.scatter(vx, vy, c="black", marker="o", s=60, label="Visited Goals")
    if unvisited_goals:
        ux, uy = zip(*unvisited_goals)
        plt.scatter(ux, uy, facecolors="none", edgecolors="blue", marker="o", s=60, label="Unvisited Goals")

    # 路径折线
    if path:
        plt.plot(xs, ys, "-o", c="black", linewidth=1)

    plt.legend()
    plt.title(f"Instance: {instance_name}")
    plt.axis("equal")
    plt.show()


if __name__ == "__main__":
    # 修改这里的名字，选择要画的实例
    # instances_to_plot = ["instance_100", "instance_021", "instance_051", "instance_081"]
    instances_to_plot = ["instance_090", "instance_100"]
    for name in instances_to_plot:
        plot_solution(name)