import requests
from bs4 import BeautifulSoup
import tkinter as tk


def search_films():
    genre = genre_entry.get()
    url = "https://www.imdb.com/search/title?genres=" + genre
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    film_list= soup.find_all("div", {"class": "lister-item mode-advanced"})
    film_titles = [film.find("h3", {"class": "lister-item-header"}).find("a").text for film in film_list]
    film_display.delete(0, tk.END)
    for title in film_titles:
        film_display.insert(tk.END, title)


root = tk.Tk()
root.title("Film Arama")
root.geometry("400x400")

genre_label = tk.Label(root, text="Hangi türde filmler izlemek istersiniz?")
genre_label.pack(pady=10)

genre_entry = tk.Entry(root, width=30)
genre_entry.pack()

search_button = tk.Button(root, text="Ara", command=search_films)
search_button.pack(pady=10)

film_display = tk.Listbox(root, width=50)
film_display.pack(pady=10)

root.mainloop()
