from tkinter import * # biblioteka pozwalająca utworzyć GUI

root = Tk() # Utworzenie podstawowego obiektu okna naszego programy
root.title('MyGUIApp') # Nadanie tutułu okna
canvas = Canvas(root, height=800, width=600) # Utworzenie obiektu canvas, który będzie zawierał wszystkie elementy GUI
canvas.pack() # Umieszczenie canvas w oknie

background_image = PhotoImage(file='altum.png') # Utworzenie obiektu PhotoImage, który będzie zawierał obrazek
background_label = Label(root, image=background_image) # Utworzenie obiektu Label, który będzie zawierał obrazek opakowany w obiekt PhotoImage
background_label.place(relwidth=1, relheight=1) # Umieszczenie obiektu Label z obrazkiem w canvas czyli w oknie naszego programu
# relwidth oznacza że szerokość obiektu Label będzie równa szerokości canvas czyli okna naszego programu
# relheight oznacza że wysokość obiektu Label będzie równa wysokości canvas czyli okna naszego programu

frame = Frame(root, bg='#ffffff') # Utworzenie obiektu Frame, który będzie zawierał elementy GUI ułatwiający ich pozycjonowanie
frame.place(relx=0.5, rely=0.6, relwidth=0.75, relheight=0.1, anchor='n') # Umieszczenie obiektu Frame w canvas
# relx oznacza pozycję względem osi x, gdzie 0.5 oznacza połowę szerokości canvas
# rely oznacza pozycję względem osi y, gdzie 0.6 oznacza 60% wysokości canvas
# relwidth oznacza szerokość względem canvas, gdzie 0.75 oznacza 75% szerokości canvas
# relheight oznacza wysokość względem canvas, gdzie 0.1 oznacza 10% wysokości canvas
# anchor oznacza punkt odniesienia, gdzie 'n' oznacza górny punkt

labelOne = Label(frame) # Utworzenie obiektu Label, który będzie zawierał tekst, który będzie wyświetlany na ekranie
labelOne.place(relx=0.05, rely=0.15, relwidth=0.18, relheight=0.3) # Umieszczenie obiektu Label w obiekcie Frame wraz z jego pozycjonowaniem
# relx oznacza pozycję względem osi x, gdzie 0.05 oznacza 5% szerokości obiektu Frame
# rely oznacza pozycję względem osi y, gdzie 0.15 oznacza 15% wysokości obiektu Frame
# relwidth oznacza szerokość względem obiektu Frame, gdzie 0.18 oznacza 18% szerokości obiektu Frame
# relheight oznacza wysokość względem obiektu Frame, gdzie 0.3 oznacza 30% wysokości obiektu Frame

labelOne.configure(text="Label One") # Nadanie obiektowi Label tekst

entryOne = Entry(frame, font=40) # Utworzenie obiektu Entry, który będzie zawierał tekst, który będzie można wpisać
entryOne.place(relx=0.25, rely=0.15, relwidth=0.3, relheight=0.3) # Umieszczenie obiektu Entry w obiekcie Frame wraz z jego pozycjonowaniem

labelTwo = Label(frame) # Utworzenie obiektu Label, który będzie zawierał tekst, który będzie wyświetlany na ekranie
labelTwo.place(relx=0.05, rely=0.55, relwidth=0.18, relheight=0.3) # Umieszczenie obiektu Label w obiekcie Frame wraz z jego pozycjonowaniem
labelTwo.configure(text="Label One")

entryTwo = Entry(frame, font=40) # Utworzenie obiektu Entry, który będzie zawierał tekst, który będzie można wpisać
entryTwo.place(relx=0.25, rely=0.55, relwidth=0.3, relheight=0.3) # Umieszczenie obiektu Entry w obiekcie Frame wraz z jego pozycjonowaniem

entryOne.insert(0, "Hello") # Wstawienie tekstu do obiektu Entry o nazwie entryOne
entryTwo.insert(0, "Hi") # Wstawienie tekstu do obiektu Entry o nazwie entryTwo


def printTextEnteredInEntryOne(): # Funkcja, która wyświetli tekst wpisany w obiekcie Entry o nazwie entryOne
    print(entryOne.get()) # Wyświetlenie tekstu wpisanego w obiekcie Entry o nazwie entryOne


printInputButton = Button(frame, text="Print Text", command=printTextEnteredInEntryOne) # Utworzenie obiektu Button oraz przypisanie do niego funkcji o nazwie printTextEnteredInEntryOne
printInputButton.place(relx=0.6, rely=0.16, relwidth=0.35, relheight=0.7) # Umieszczenie obiektu Button w obiekcie Frame wraz z jego pozycjonowaniem

secondFrame = Frame(root, bg='#ffffff') # Utworzenie kolejnego obiektu Frame, który będzie zawierał elementy GUI ułatwiający ich pozycjonowanie
secondFrame.place(relx=0.5, rely=0.8, relwidth=0.75, relheight=0.1, anchor='n') # Umieszczenie obiektu Frame w canvas

selectedOption = StringVar(root, 'FIRST_OPTION') # Utworzenie obiektu StringVar, który będzie zawierał wybraną opcję z listy


def printSelectedOption(): # Funkcja, która wyświetli wybraną opcję z listy
    print(selectedOption.get()) # Wyświetlenie wybranej opcji z listy


optionOne = Radiobutton(secondFrame, text="Option One", variable=selectedOption, value='FIRST_OPTION') # Utworzenie obiektu Radiobutton, który będzie zawierał opcję z listy oraz podpięcie jej do obiektu StringVar o nazwie selectedOption
optionOne.place(relx=0.1, rely=0.15, relwidth=0.3, relheight=0.3) # Umieszczenie obiektu Radiobutton w obiekcie Frame wraz z jego pozycjonowaniem
optionTwo = Radiobutton(secondFrame, text="Option Two", variable=selectedOption, value='SECOND_OPTION') # Utworzenie obiektu Radiobutton, który będzie zawierał opcję z listy oraz podpięcie jej do obiektu StringVar o nazwie selectedOption
optionTwo.place(relx=0.1, rely=0.55, relwidth=0.3, relheight=0.3) # Umieszczenie obiektu Radiobutton w obiekcie Frame wraz z jego pozycjonowaniem
printSelectButton = Button(secondFrame, text="Button One", command=printSelectedOption) # Utworzenie obiektu Button oraz przypisanie do niego funkcji o nazwie printSelectedOption
printSelectButton.place(relx=0.6, rely=0.16, relwidth=0.35, relheight=0.7) # Umieszczenie obiektu Button w obiekcie Frame wraz z jego pozycjonowaniem
# relx oznacza pozycję względem osi x, gdzie 0.1 oznacza 10% szerokości obiektu Frame
# rely oznacza pozycję względem osi y, gdzie 0.15 oznacza 15% wysokości obiektu Frame
# relwidth oznacza szerokość względem obiektu Frame, gdzie 0.3 oznacza 30% szerokości obiektu Frame
# relheight oznacza wysokość względem obiektu Frame, gdzie 0.3 oznacza 30% wysokości obiektu Frame44

root.mainloop() # Uruchomienie głównej pętli programu GUI w Pythonie 3 z biblioteką Tkinter (tkinter) oraz wyświetlenie okna GUI na ekranie komputera użytkownika
