our_route = {"LAX", "JFK", "CDG", "DXB"}
comp_route = {"JFK", "CDG", "LHR", "BKK"}


sim_routes = our_route.intersection(comp_route)
print("Both airlines have routes to:", sim_routes)


uni_routes = our_route.difference(comp_route)
print("We are the only ones that can take people to:", uni_routes)


no_route = our_route.symmetric_difference(comp_route)
print("There are no shared routes to:", no_route)
