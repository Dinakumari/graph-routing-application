import heapq

class TravelPlanner:
    def __init__(self):
        self.graph = {}  # Adjacency list

    def add_route(self, from_place, to_place, cost):
        self.graph.setdefault(from_place, []).append((to_place, cost))
        self.graph.setdefault(to_place, []).append((from_place, cost))  # Undirected graph

    def display_graph(self):
        print("\n🗺️ Travel Routes:")
        for place in self.graph:
            connections = ", ".join([f"{dest} ({cost})" for dest, cost in self.graph[place]])
            print(f"  {place} => {connections}")
        print()

    def shortest_path(self, start, end):
        queue = [(0, start, [])]
        visited = set()

        while queue:
            cost, current, path = heapq.heappop(queue)

            if current in visited:
                continue

            visited.add(current)
            path = path + [current]

            if current == end:
                return cost, path

            for neighbor, weight in self.graph.get(current, []):
                if neighbor not in visited:
                    heapq.heappush(queue, (cost + weight, neighbor, path))

        return float('inf'), []

def build_sample_data(planner):
    routes = [
        ("JAMSHEDPUR", "JHARKHAND", 300),
        ("SHAHADRA", "NEW DELHI", 500),
        ("BALASORE", "ODISHA", 800),
        ("KOLKATA", "WEST BENGAL", 1000),
        ("BHUBANESHWAR", "ODISHA", 700),
        ("PUNE", "MAHARASTRA", 600),
        ("RANCHI", "JHARKHAND", 900),
        ("MUMBAI", "MAHARASTRA", 1500)
    ]
    for from_loc, to_loc, cost in routes:
        planner.add_route(from_loc, to_loc, cost)

def main():
    planner = TravelPlanner()
    build_sample_data(planner)

    print("✈️ Welcome to the Travel Planner!")
    planner.display_graph()

    while True:
        print("Options:")
        print("1. Plan a route")
        print("2. Show all routes")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            src = input("Enter starting location: ").strip()
            dst = input("Enter destination: ").strip()
            cost, path = planner.shortest_path(src, dst)
            if path:
                print(f"\n✅ Shortest route from {src} to {dst}: {' -> '.join(path)} (Cost: {cost})\n")
            else:
                print("⚠️ No route found.\n")

        elif choice == "2":
            planner.display_graph()

        elif choice == "3":
            print("Thanks for using Travel Planner. Safe travels! 🌍")
            break

        else:
            print("Invalid option. Try again.\n")

if __name__ == "__main__":
    main()
