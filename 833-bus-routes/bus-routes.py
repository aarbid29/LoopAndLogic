class Solution:
    def numBusesToDestination(self, routes: list[list[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        stops_to_routes = defaultdict(set)
        dq = deque()
        for  i ,route in enumerate(routes):
            for stop in route:
                stops_to_routes[stop].add(i)
        
        visited_routes = set()
        visited_stops = {source}
        #this is such that source is connected to multiple routes/busroutes
        for route in stops_to_routes[source]:
            visited_routes.add(route)
            dq.append((route,1))

        while dq:
            route , bus_used = dq.popleft()

            for stop in routes[route]:
                if stop == target:
                    return bus_used
                if stop in visited_stops:
                    continue
                visited_stops.add(stop)

                for route in stops_to_routes[stop]:
                    if route in visited_routes:
                        continue
                    
                    if route not in visited_routes:
                        visited_routes.add(route)
                        dq.append((route,bus_used+1))
        return -1


        

