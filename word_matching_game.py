import random
import tkinter as tk
from tkinter import messagebox

# Globális toplista
toplist = []

# Funkciók
def generate_pairs(difficulty):
    word_pool = {
        "könnyű": {
            "kutya": "dog", "macska": "cat", "asztal": "table", "szék": "chair",
            "autó": "car", "ház": "house", "fa": "tree", "alma": "apple", "könyv": "book"
        },
        "közepes": {
            "telefon": "phone", "iskola": "school", "számítógép": "computer",
            "cipő": "shoe", "körte": "pear", "füzet": "notebook", "ablak": "window",
            "kávé": "coffee", "tükör": "mirror"
        },
        "nehéz": {
            "zongora": "piano", "mikrohullámú sütő": "microwave", "repülőtér": "airport",
            "értekezlet": "meeting", "művészet": "art", "történelem": "history",
            "környezetvédelem": "environmental protection", "műanyag": "plastic",
            "fenntarthatóság": "sustainability"
        }
    }
    return random.sample(list(word_pool[difficulty].items()), 7)

def shuffle_options(pairs):
    magyar = [pair[0] for pair in pairs]
    angol = [pair[1] for pair in pairs]
    random.shuffle(angol)
    return magyar, angol

def check_answers():
    correct = 0
    incorrect = 0
    for i, magyar_word in enumerate(magyar_words):
        selected_option = selected_options[i].get()
        if selected_option == correct_pairs[magyar_word]:
            correct += 1
        else:
            incorrect += 1
    show_results(correct, incorrect)

def show_results(correct, incorrect):
    total = correct + incorrect
    messagebox.showinfo("Eredmény", f"Helyes válaszok: {correct}/{total}\n"
                                    f"Helytelen válaszok: {incorrect}/{total}")
    if correct == total:
        messagebox.showinfo("Gratuláció", "Kiváló! Minden helyes! 🎉")
    elif correct > incorrect:
        messagebox.showinfo("Bátorítás", "Nagyon jó munka, csak így tovább! 💪")
    else:
        messagebox.showinfo("Motiváció", "Ne csüggedj, gyakorolj még egy kicsit! 😊")

# GUI létrehozása
def start_game(difficulty):
    global magyar_words, correct_pairs, selected_options
    pairs = generate_pairs(difficulty)
    correct_pairs = dict(pairs)
    magyar_words, angol_words = shuffle_options(pairs)

    # Játékablak
    game_window = tk.Toplevel(root)
    game_window.title("Játék - Kösd össze a megfelelőket!")
    tk.Label(game_window, text="Kösd össze a megfelelő magyar és angol szavakat:", font=("Arial", 14)).pack(pady=10)

    frame = tk.Frame(game_window)
    frame.pack()

    selected_options = []
    for i, magyar_word in enumerate(magyar_words):
        tk.Label(frame, text=f"{i+1}. {magyar_word}", font=("Arial", 12)).grid(row=i, column=0, padx=10, pady=5)
        selected_option = tk.StringVar(value="")
        selected_options.append(selected_option)
        dropdown = tk.OptionMenu(frame, selected_option, *angol_words)
        dropdown.grid(row=i, column=1, padx=10, pady=5)

    tk.Button(game_window, text="Eredmény kiértékelése", command=check_answers, font=("Arial", 12)).pack(pady=10)

# Fő ablak
root = tk.Tk()
root.title("Kösd össze a megfelelőket!")
root.geometry("500x300")

tk.Label(root, text="Üdvözöllek a 'Kösd össze a megfelelőket!' játékban!", font=("Arial", 16)).pack(pady=10)
tk.Label(root, text="Válaszd ki a nehézségi szintet:", font=("Arial", 14)).pack(pady=10)

frame = tk.Frame(root)
frame.pack(pady=10)

tk.Button(frame, text="Könnyű", command=lambda: start_game("könnyű"), font=("Arial", 12)).grid(row=0, column=0, padx=10)
tk.Button(frame, text="Közepes", command=lambda: start_game("közepes"), font=("Arial", 12)).grid(row=0, column=1, padx=10)
tk.Button(frame, text="Nehéz", command=lambda: start_game("nehéz"), font=("Arial", 12)).grid(row=0, column=2, padx=10)

tk.Button(root, text="Kilépés", command=root.quit, font=("Arial", 12)).pack(pady=20)

# Alkalmazás indítása
root.mainloop()

