import tkinter as tk
from datetime import datetime
import requests
from bs4 import BeautifulSoup

#WINDOW
window = tk.Tk()
window.title("Quote of the Day")
window.geometry("800x170")
window.resizable(width=0,height=0)

#Date
date = datetime.today().strftime("%a, %d.%m.%Y")
lbl_date = tk.Label(window,text=date, padx = 12, pady= 12)
lbl_date.pack(anchor="e")


#Quote
URL = "https://zenquotes.io/"
response = requests.get(URL)
soup = BeautifulSoup(response.content,"html.parser")
quote = soup.blockquote.text
lbl_quote = tk.Label(window,text=quote, padx = 12, pady= 25)
lbl_quote.pack()




window.mainloop()