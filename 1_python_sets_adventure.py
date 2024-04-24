#   Task 1:


#   Example Code:
our_route = {"LAX", "JFK", "CDG", "DXB"}
comp_route = {"JFK", "CDG", "LHR", "BKK"}



#   1:  Destinations that both airlines fly to.
#  Similar

sim_routes = our_route.intersection(comp_route)
print("Both airlines have routes to:", sim_routes)

#   2:  Destinations unique to your airline.
#  Different

uni_routes = our_route.difference(comp_route)
print("We are the only ones that can take people to:", uni_routes)

#   3:  Whether there are any destinations that neither airline shares.
#  Neither

no_route = our_route.symmetric_difference(comp_route)
print("There are no shared routes to:", no_route)



