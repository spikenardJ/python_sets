# Question 1: Python Sets Adventure

# Task 1: Flight Route Comparison


our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

def mutual_route_destinations(our_routes, competitor_routes):
    mutual_routes = our_routes.intersection(competitor_routes)
    print("\nMutual Flight Route Destinations: ")
    for route in mutual_routes:
        print(" -", route)

def our_exclusive_route_destinations(our_routes, competitor_routes):
    our_exclusive_routes = our_routes.difference(competitor_routes)
    print("\nOur Exclusive Flight Route Destinations: ")
    for route in our_exclusive_routes:
        print(" -", route)

def route_destinations_that_neither_share(our_routes, competitor_routes):
    routes_that_neither_share = our_routes.symmetric_difference(competitor_routes)
    print("\nFlight Route Destinations That Neither Airlines Share: ")
    for route in routes_that_neither_share:
        print(" -", route)


while True:
    print("\n1. Flight route destinations that both airlines fly to")
    print("2. Flight route destinations that is unique to our airline")
    print("3. Flight route destinations that neither airlines share")
    print("4. Exit")
    choice = input("Please enter your selection: ")

    if choice == "1":
        mutual_route_destinations(our_routes, competitor_routes)
    elif choice == "2":
        our_exclusive_route_destinations(our_routes, competitor_routes)
    elif choice == "3":
        route_destinations_that_neither_share(our_routes, competitor_routes)
    elif choice == "4":
        print("Exiting program. 👋")
        break
    else:
        print("Invalid choice. Please try again.")