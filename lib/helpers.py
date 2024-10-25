from models.state import State
from models.city import City

name = "Alin"

print(f"{name}")

#State functions

def view_all_states():
    all_states = State.get_all()
    for i, state in enumerate(all_states, start=1):
        print(f"{i}. {state.name} | Population {state.population} | Region {state.region}")

def add_a_state(name, population, region):
    name = input("Please enter a name: ")
    region = input ("please enter a region: ")

    while True: 
        try: 
            population = int(input("Please enter the population"))
            break
        except ValueError:
            print("Population must be an integer")
    
    print("You have successfully added the population")

    state_instance = State(name, population, region)
    state_instance.save()
    print(f"State {name} has now been added to the State list")

def delete_a_state(name):
    all_states = State.get_all()
    view_all_states()

    try:
        delete_state = int(input("Please enter the state # that you would like to delete: "))
        if 1<= delete_state <= len(all_states):
            selected_state = all_states[delete_state -1]
            selected_state.delete()
            print(f"The state of {selected_state.name} has been deleted")
        else:
            print(" Please try again")
    except ValueError: 
        print("Invalid selection. Please try again.")
        
def update_a_state(population):
    all_states = State.get_all()
    view_all_states()

    try:
        update_state = int(input("Which state would you like to update?: "))
    except ValueError:
        print("Invalid input. Please try again.")
        return

    selected_state = all_states[update_state - 1]

    if selected_state:
        try:
            population = int(input("Please enter the updated population: "))
        except ValueError:
            print("Population must be a number")
            return

        selected_state.population = population
        selected_state.update()

    else:
        print("State not found. Try again.")

#Cities functions

def view_all_cities_by_state(state_id):
    all_cities = City.find_by_state(state_id)
    for i, city in enumerate(all_cities, start=1):
        print(f"{i}. {city.name} | Population {city.city_population}")
    return all_cities

def get_cities_by_state(state_id):
    all_cities = City.find_by_state(state_id)
    
    if all_cities:
        print("")
        print(f"Cities: ")
        for i, city in enumerate(all_cities, start=1):
            print("")
            print(f"{i}. {city.name} | Population: {city.city_population}")
            print("")
    else:
        print(f"No cities found for this state.")

def add_a_city(state_id):
    name = input("Please enter name of city: ")
    try:
        city_population = int(input("Please enter the population: "))
    except ValueError:
        print("must be a number")
        return 
    
    city_instance = City(name=name, city_population=city_population, state_id=state_id)
    city_instance.save()
    print(f"City {name} has now been added to the City list")

def delete_a_city(state_id):
    all_cites = view_all_cities_by_state(state_id)
    try:
        delete_city = int(input("Select number to delete: "))
        selected_city = all_cites[delete_city - 1]
        selected_city.delete()
        print(f"City {selected_city.name} has been deleted")
    except ValueError:
        print("Selection must be a number")

def update_a_city(state_id): 
    get_cities_by_state(state_id)
    all_cities = City.find_by_state(state_id)

    try:
        city_selection = int(input("Please select the city number to update: "))
        selected_city = all_cities[city_selection - 1]
    except ValueError:
        print("Invalid selection. Please try again.")
        return
    try:
        update_population = int(input(f"Please enter the updated population for {selected_city.name}: "))
    except ValueError:
        print("Population must be a number.")
        
    selected_city.city_population = update_population
    selected_city.update()

    print(f"City {selected_city.name} has been updated with a population of {selected_city.city_population}.")


