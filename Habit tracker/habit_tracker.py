import datetime

def get_date():
    """Get the current date."""
    return datetime.date.today().strftime("%Y-%m-%d")

def create_habit():
    """Create a new habit."""
    habit_name = input("Enter the habit name: ")
    return {"name": habit_name, "dates_completed": []}

def display_habits(habits):
    """Display all habits."""
    if not habits:
        print("No habits found.")
    else:
        print("Habits:")
        for habit in habits:
            print(habit["name"])

def track_habit(habit):
    """Track completion of a habit for today."""
    today = get_date()
    if today not in habit["dates_completed"]:
        habit["dates_completed"].append(today)
        print(f"Completed habit: {habit['name']}")
    else:
        print(f"You have already completed the habit: {habit['name']} today.")

def save_habits(habits):
    """Save habits to a file."""
    with open("habits.txt", "w") as file:
        for habit in habits:
            file.write(f"{habit['name']}:{','.join(habit['dates_completed'])}\n")

def load_habits():
    """Load habits from a file."""
    habits = []
    try:
        with open("habits.txt", "r") as file:
            for line in file:
                name, dates_completed = line.strip().split(":")
                habit = {"name": name, "dates_completed": dates_completed.split(",")}
                habits.append(habit)
    except FileNotFoundError:
        pass
    return habits

def main():
    habits = load_habits()
    while True:
        print("\nHabit Tracking App")
        print("1. Create a new habit")
        print("2. Track completion of a habit")
        print("3. Display all habits")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            habit = create_habit()
            habits.append(habit)
            save_habits(habits)
            print(f"Habit '{habit['name']}' created.")
        elif choice == "2":
            display_habits(habits)
            habit_name = input("Enter the habit name to track: ")
            found = False
            for habit in habits:
                if habit["name"] == habit_name:
                    track_habit(habit)
                    found = True
                    break
            if not found:
                print("Habit not found.")
            save_habits(habits)
        elif choice == "3":
            display_habits(habits)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
