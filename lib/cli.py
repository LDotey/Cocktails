from helpers import (
    view_all_states, 
    add_a_state, 
    delete_a_state, 
    update_a_state, 
    get_cities_by_state,
    add_a_city,
    delete_a_city,
    update_a_city,

)

def main(): 
    while True:
        print("")
        view_all_states()
        print("")
        print("")
        main_menu()
        print("")
        
        choice = input("Enter your choice: ")
        print("")

        if choice == "1":
            view_all_states()
        elif choice == "2":
            add_a_state("name", "population", "region")
        elif choice == "3":
            delete_a_state("name")
        elif choice == "4":
            update_a_state("population")
        elif choice == "5":
            try:
                stars()
                view_all_states()
                stars()
                state_id = int(input("Enter the state # you would like to see: "))
                handle_city_menu(state_id)
            except ValueError:
                print("Invalid choice - try again")    
        else:
            if choice == "e":
                exit_program()
                break
        



def handle_city_menu(state_id):
   get_cities_by_state(state_id)
   
   while True:
    print("")
    city_menu()
    print("")
    choice = input("What would you like to do - select a number:  ")
    print("")
    
    try:  
        if choice == "1":
            update_a_city(state_id)
            return
        if choice == "2":
            delete_a_city(state_id)
            break
        elif choice == "3":
            add_a_city(state_id)
            break
        elif choice == "4":
            print("----------Main Menu----------")
            return
        else:
            print("Invalid choice")
                
    except ValueError:
        print("Invalid input. Please try again.")





def exit_program():
    print("You are now leaving - Goodbye!")

def main_menu():
    print("-----------States Menu-----------")
    stars()
    print("1. View all states")
    print("2. Add a state")
    print("3. Delete a state")
    print("4. Update a state")
    print("5. Select State to view its cities")
    print("To exit press (e)")
    stars()

def city_menu():
    stars()
    print("1. Update a city")
    print("2. Delete a city")
    print("3. Add a city")
    print("4. Go back to main menu")
    stars()

def stars():
    print("******************")

if __name__ == "__main__":
    main()


