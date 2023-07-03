import tkinter as tk
import random
from PIL import Image, ImageTk
import os


# Append agent selected into a list
def append_agent(img):
    if img in selected_agent_list:
        return
    selected_agent_list.append(img)


# Picks random agent from selected agents
def random_agent():
    global selected_agent_list, converted_images, final_agent_result
    # Checks if agent_list is empty
    if selected_agent_list:
        chosen = random.choice(selected_agent_list)
        photo_chosen = Image.open('photos/' + chosen)
        photo_chosen_resize = photo_chosen.resize((100, 100))
        photo_chosen_convert = ImageTk.PhotoImage(photo_chosen_resize)
        converted_images.append(photo_chosen_convert)
        # Removes final button if it already exists
        try:
            final_agent_result.pack_forget()
        except NameError:
            pass
        # Create a button containing the images of the agent that was randomly selected
        final_agent_result = tk.Button(window, image=photo_chosen_convert, width=100, height=100)
        final_agent_result.pack()


def clear_agent_selection():
    global selected_agent_list, agent_button_objects
    # Clear list
    selected_agent_list = []
    # Un-highlights the buttons selected
    for button in agent_button_objects:
        unhighlight(button)
    # Removes previous result
    try:
        global final_agent_result
        final_agent_result.pack_forget()
    except NameError:
        return
    for button in agent_button_objects:
        unhighlight(button)


def highlight(btn):
    btn.configure(bg='Grey')


def unhighlight(btn):
    btn.configure(bg='White')


# Window Settings and Icon
window = tk.Tk()
window.geometry('1280x420')
window.title('Valorant Agents Roulette')

# Frame used to group images
frame = tk.Frame(window)
frame.pack()

# Images contained in the folder
images = os.listdir(r'photos/')
# Names of selected agents in .png format
selected_agent_list = []
# Converted images(to keep them in memory)
converted_images = []
# Contains button objects
agent_button_objects = []
row_count = 0
col_count = 0
for index, image in enumerate(images):
    # Agents in display
    photo = Image.open('photos/' + image)
    photo_resize = photo.resize((100, 100))
    photo_convert = ImageTk.PhotoImage(photo_resize)
    converted_images.append(photo_convert)
    agent_button = tk.Button(frame, image=photo_convert, width=100, height=100,
                             command=lambda img=image: append_agent(img))
    agent_button.grid(row=row_count, column=col_count, padx=5, pady=5)
    agent_button.bind('<Button-1>', lambda event, btn=agent_button: highlight(btn))
    agent_button_objects.append(agent_button)
    agent_button.configure(bg='White')
    row_count += 1
    # 2 rows of 11 buttons
    if row_count == 2:
        row_count = 0
        col_count += 1


# Roll Button
roll_button = tk.Button(text='Roll', font=('Tahoma', 12), width=25, bg='red', fg='white', command=random_agent)
roll_button.pack()

# Clear button
clear_button = tk.Button(text='Clear', font=('Tahoma', 12), width=25, bg='red', fg='white',
                         command=clear_agent_selection)
clear_button.pack()

window.mainloop()
