import json, math, argparse, sys
from typing import List, Tuple, Dict, Any, Optional

Point = Tuple[int, int]
Path = List[Point]
LEN_LIMIT = 2000.0
MAX_POINTS = 100

# ---------- 基本几何 ----------
def dist(a: Point, b: Point) -> float:
    return math.hypot(a[0]-b[0], a[1]-b[1])

def path_length(p: Path) -> float:
    return sum(dist(p[i], p[i+1]) for i in range(len(p)-1))

def ccw(ax, ay, bx, by, cx, cy) -> int:
    v = (bx-ax)*(cy-ay) - (by-ay)*(cx-ax)
    if v > 0: return 1
    if v < 0: return -1
    return 0

def on_segment(ax, ay, bx, by, px, py) -> bool:
    return min(ax,bx) <= px <= max(ax,bx) and min(ay,by) <= py <= max(ay,by)

def segments_intersect(a: Point, b: Point, c: Point, d: Point) -> bool:
    o1 = ccw(a[0],a[1], b[0],b[1], c[0],c[1])
    o2 = ccw(a[0],a[1], b[0],b[1], d[0],d[1])
    o3 = ccw(c[0],c[1], d[0],d[1], a[0],a[1])
    o4 = ccw(c[0],c[1], d[0],d[1], b[0],b[1])
    if o1 != o2 and o3 != o4:
        return True
    if o1 == 0 and on_segment(a[0],a[1], b[0],b[1], c[0],c[1]): return True
    if o2 == 0 and on_segment(a[0],a[1], b[0],b[1], d[0],d[1]): return True
    if o3 == 0 and on_segment(c[0],c[1], d[0],d[1], a[0],a[1]): return True
    if o4 == 0 and on_segment(c[0],c[1], d[0],d[1], b[0],b[1]): return True
    return False

def path_has_crossing(p: Path) -> bool:
    n = len(p)
    for i in range(n-1):
        a, b = p[i], p[i+1]
        for j in range(i+2, n-1):
            if j == i+1: 
                continue
            c, d = p[j], p[j+1]
            if segments_intersect(a, b, c, d):
                return True
    return False

def validate_path(instance: Dict[str, Any], path: Path) -> bool:
    if not path:
        return True
    starts = set(map(tuple, instance["start_points"]))
    ends   = set(map(tuple, instance["end_points"]))
    if tuple(path[0]) not in starts: return False
    if tuple(path[-1]) not in ends:  return False
    if len(path) > MAX_POINTS:       return False
    if len(set(path)) != len(path):  return False
    if path_has_crossing(path):      return False
    if not (path_length(path) < LEN_LIMIT): return False
    for x, y in path:
        if not (isinstance(x, int) and isinstance(y, int)): return False
        if not (-1000 <= x <= 1000 and -1000 <= y <= 1000): return False
    return True

# ---------- 贪心插入 goals ----------
def greedy_insert_goals(start: Point, end: Point, goals: List[Point]) -> Path:
    path: Path = [start, end]
    current_len = dist(start, end)
    remaining = [g for g in goals if g not in (start, end)]
    while remaining and len(path) < MAX_POINTS:
        best = None
        for g in remaining:
            for i in range(len(path)-1):
                a, b = path[i], path[i+1]
                delta = dist(a, g) + dist(g, b) - dist(a, b)
                new_len = current_len + delta
                if new_len >= LEN_LIMIT:
                    continue
                tmp = path[:i+1] + [g] + path[i+1:]
                if path_has_crossing(tmp):
                    continue
                if best is None or delta < best[0]:
                    best = (delta, i, g)
        if best is None:
            break
        delta, idx, g = best
        path.insert(idx+1, g)
        current_len += delta
        remaining.remove(g)
    return path

# ---------- 解单个实例 ----------
def solve_instance(instance: Dict[str, Any]) -> Path:
    starts = [tuple(p) for p in instance["start_points"]]
    ends   = [tuple(p) for p in instance["end_points"]]
    goals  = [tuple(p) for p in instance.get("goal_points", [])]

    best_path: Optional[Path] = None
    best_key = (-1, float("inf"))

    for s in starts:
        for e in ends:
            if dist(s, e) >= LEN_LIMIT:
                continue
            p = greedy_insert_goals(s, e, goals)
            gcount = sum(1 for g in goals if g in p)
            L = path_length(p)
            if validate_path(instance, p):
                key = (gcount, L)
                if key[0] > best_key[0] or (key[0] == best_key[0] and key[1] < best_key[1]):
                    best_key, best_path = key, p
    return best_path if best_path is not None else []

# ---------- 主函数 ----------
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Path to input JSON with problem instances")
    parser.add_argument("--output", required=True, help="Path to write solution JSON")
    parser.add_argument("--verbose", action="store_true")
    args = parser.parse_args()

    with open(args.input, "r", encoding="utf-8") as f:
        data = json.load(f)

    solutions: Dict[str, List[List[int]]] = {}
    for name, instance in data.items():
        path = solve_instance(instance)
        solutions[name] = [list(p) for p in path]
        if args.verbose:
            goals = instance.get("goal_points", [])
            gcount = sum(1 for g in goals if tuple(g) in path)
            print(f"[{name}] goals={gcount} len={path_length(path):.2f} valid={validate_path(instance, path)}",
                  file=sys.stderr)

    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(solutions, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    main()
