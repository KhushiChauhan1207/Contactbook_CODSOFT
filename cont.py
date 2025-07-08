import tkinter as tk
from tkinter import messagebox
import json
import os


DATA_FILE = "people_data.json"


def fetch_people():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []


def store_people():
    with open(DATA_FILE, "w") as f:
        json.dump(people_list, f, indent=4)


def save_person():
    person_name = entry_name.get().strip()
    person_number = entry_number.get().strip()
    person_mail = entry_mail.get().strip()

    if not person_name or not person_number:
        messagebox.showerror("Missing Info", "Name and Number are mandatory.")
        return

    person = {
        "person_name": person_name,
        "person_number": person_number,
        "person_mail": person_mail
    }

    people_list.append(person)
    store_people()
    refresh_display()
    reset_fields()


def remove_selected():
    selected = display_box.curselection()
    if not selected:
        messagebox.showwarning("No Selection", "Please choose a contact to remove.")
        return
    index = selected[0]
    people_list.pop(index)
    store_people()
    refresh_display()


def reset_fields():
    entry_name.delete(0, tk.END)
    entry_number.delete(0, tk.END)
    entry_mail.delete(0, tk.END)


def search_name():
    keyword = entry_search.get().strip().lower()
    display_box.delete(0, tk.END)
    for person in people_list:
        if keyword in person["person_name"].lower():
            record = f"{person['person_name']} | {person['person_number']} | {person['person_mail']}"
            display_box.insert(tk.END, record)


def refresh_display():
    display_box.delete(0, tk.END)
    for person in people_list:
        formatted = f"{person['person_name']} | {person['person_number']} | {person['person_mail']}"
        display_box.insert(tk.END, formatted)


app = tk.Tk()
app.title("Simple People Tracker")
app.geometry("520x520")
app.configure(bg="#f0f8ff")

people_list = fetch_people()


tk.Label(app, text="Full Name", bg="#f0f8ff").pack()
entry_name = tk.Entry(app, width=45)
entry_name.pack()

tk.Label(app, text="Phone Number", bg="#f0f8ff").pack()
entry_number = tk.Entry(app, width=45)
entry_number.pack()

tk.Label(app, text="Email Address", bg="#f0f8ff").pack()
entry_mail = tk.Entry(app, width=45)
entry_mail.pack()

tk.Button(app, text="Save Entry", command=save_person, bg="#228B22", fg="white", width=20).pack(pady=6)


tk.Label(app, text="Search Contact", bg="#f0f8ff").pack()
entry_search = tk.Entry(app, width=30)
entry_search.pack()
tk.Button(app, text="Find", command=search_name, bg="#FFA500", width=10).pack(pady=4)


display_box = tk.Listbox(app, width=70, height=12)
display_box.pack(pady=10)


tk.Button(app, text="Delete Selected", command=remove_selected, bg="#DC143C", fg="white").pack(pady=5)


refresh_display()

app.mainloop()
