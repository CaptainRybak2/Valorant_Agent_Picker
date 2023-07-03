import tkinter as tk
import datetime

def get_date():
    """Get the current date."""
    return datetime.date.today().strftime("%Y-%m-%d")

def create_habit():
    """Create a new habit."""
    habit_name = habit_entry.get()
    if habit_name:
        habit = {"name": habit_name, "dates_completed": []}
        habits.append(habit)
        habit_listbox.insert(tk.END, habit_name)
        habit_entry.delete(0, tk.END)
        save_habits()
    else:
        display_message("Please enter a habit name.")

def display_habits():
    """Display all habits."""
    habit_listbox.delete(0, tk.END)
    if not habits:
        display_message("No habits found.")
    else:
        for habit in habits:
            habit_listbox.insert(tk.END, habit["name"])

def track_habit():
    """Track completion of a habit for today."""
    selected_habit = habit_listbox.curselection()
    if selected_habit:
        habit_index = selected_habit[0]
        habit = habits[habit_index]
        today = get_date()
        if today not in habit["dates_completed"]:
            habit["dates_completed"].append(today)
            display_message(f"Completed habit: {habit['name']}")
            save_habits()
        else:
            display_message(f"You have already completed the habit: {habit['name']} today.")
    else:
        display_message("Please select a habit to track.")

def save_habits():
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

def display_message(message):
    """Display a message in the message label."""
    message_label.config(text=message)

# Load habits from the file
habits = load_habits()

# Create the main window
window = tk.Tk()
window.title("Habit Tracker")

# Habit entry and create button
habit_label = tk.Label(window, text="Habit:")
habit_label.pack()
habit_entry = tk.Entry(window)
habit_entry.pack()
create_button = tk.Button(window, text="Create Habit", command=create_habit)
create_button.pack()

# Habit listbox
habit_listbox = tk.Listbox(window)
habit_listbox.pack()

# Track button
track_button = tk.Button(window, text="Track Habit", command=track_habit)
track_button.pack()

# Display button
display_button = tk.Button(window, text="Display Habits", command=display_habits)
display_button.pack()

# Message label
message_label = tk.Label(window, text="")
message_label.pack()

# Start the Tkinter event loop
window.mainloop()
