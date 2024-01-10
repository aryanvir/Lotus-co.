import tkinter as tk
from tkinter import ttk
import mysql.connector
import subprocess
import random
import webbrowser

details = {}
with open(r"C:\Users\amrit\Aryan\CS\SQL\project\Lotus Co\project_final\credentials.txt") as file:
    lis = file.read().split(" -|- ")
    details['username'] = lis[0]
    details['password'] = lis[1]
    details['nickname'] = lis[2]


sqldatabase = mysql.connector.connect(
    host="localhost",
    user=details['username'],
    password=details['password']
)
sqlcursor = sqldatabase.cursor()

sqlcursor.execute("create database if not exists lib")
sqlcursor.execute("use lib")

sqlcursor.execute(
    '''
    create table if not exists all_books (
        id int not null primary key,
        name text,
        author text
    )
    '''
)

sqlcursor.execute(
    '''
    create table if not exists available_books (
        id int unique references all_books(id),
        name text,
        author text
    ) engine=InnoDB
    '''
)

sqlcursor.execute(
    '''
    create table if not exists issued_books (
        id int references all_books(id),
        name text,
        author text,
        due_date text,
        email text
    ) engine=InnoDB
    '''
)

bookList = [
    (1, 'A Better India: A Better World', 'Narayana Murthy'),
    (2, "The Pilgrim's Progress", 'John Bunyan'),
    (3, 'Robinson Crusoe', 'Daniel Defoe'),
    (4, "Gulliver's Travels", 'Jonathan Swift'),
    (5, 'Clarissa', 'Samuel Richardson'),
    (6, 'Tom Jones ', 'Henry Fielding'),
    (7, 'The Life and Opinions of Tristram Shandy, Gentleman', 'Laurence Sterne'),
    (8, 'Emma', 'Jane Austen'),
    (9, 'Frankenstein ', 'Mary Shelley'),
    (10, 'Nightmare Abbey', 'Thomas Love Peacock'),
    (11, 'The Narrative of Arthur Gordon Pym of Nantucket', 'Edgar Allan Poe'),
    (12, 'Sybil', 'Benjamin Disraeli'),
    (13, 'Jane Eyre', 'Charlotte Brontë'),
    (14, 'Wuthering Heights', 'Emily Brontë'),
    (15, 'Vanity Fair', 'William Thackeray'),
    (16, 'David Copperfield', 'Charles Dickens'),
    (17, 'The Scarlet Letter ', 'Nathaniel Hawthorne'),
    (18, 'Moby-Dick', 'Herman Melville'),
    (19, "Alice's Adventures in Wonderland", 'Lewis Carroll'),
    (20, 'The Moonstone', 'Wilkie Collins'),
    (21, 'Little Women', 'Louisa May Alcott'),
    (22, 'Middlemarch', 'George Eliot'),
    (23, 'The Way We Live Now', 'Anthony Trollope'),
    (24, 'The Adventures of Huckleberry Finn', 'Mark Twain'),
    (25, 'Kidnapped', 'Robert Louis Stevenson'),
    (26, 'Three Men in a Boa', 'Jerome K Jerome'),
    (27, 'The Sign of Four', 'Arthur Conan Doyle'),
    (28, 'The Picture of Dorian Gray', 'Oscar Wilde'),
    (29, 'New Grub Street', 'George Gissing'),
    (30, 'Jude the Obscure', 'Thomas Hardy'),
    (31, 'The Red Badge of Courage', 'Stephen Crane'),
    (32, 'Dracula', 'Bram Stoker'),
    (33, 'Heart of Darkness', 'Joseph Conrad'),
    (34, 'Sister Carrie', 'Theodore Dreiser'),
    (35, 'Kim', 'Rudyard Kipling'),
    (36, 'The Golden Bowl', 'Henry James'),
    (37, 'Hadrian the Seventh', 'Frederick Rolfe'),
    (38, 'The Wind in the Willows', 'Kenneth Grahame'),
    (39, 'The History of Mr Polly', 'HG Wells'),
    (40, 'Zuleika Dobson', 'Max Beerbohm'),
    (41, 'The Good Soldier', 'Ford Madox Ford'),
    (42, 'The Thirty-Nine Steps', 'John Buchan'),
    (43, 'The Rainbow', 'DH Lawrence'),
    (44, 'Of Human Bondage', 'W Somerset Maugham'),
    (45, 'The Age of Innocence', 'The Age of Innocence'),
    (46, 'Ulysses', 'James Joyce'),
    (47, 'Babbitt', 'Sinclair Lewis'),
    (48, 'A Passage to India', 'EM Forster'),
    (49, 'Gentlemen Prefer Blondes', 'Anita Loos'),
    (50, 'Mrs Dalloway', 'Virginia Woolf'),
    (51, 'The Great Gatsby', 'F Scott Fitzgerald'),
    (52, 'Lolly Willowes', 'Sylvia Townsend Warner'),
    (53, 'The Sun Also Rises', 'Ernest Hemingway'),
    (54, 'The Maltese Falcon', 'Dashiell Hammett'),
    (55, 'As I Lay Dying', 'William Faulkner'),
    (56, 'Brave New World', 'Aldous Huxley'),
    (57, 'Cold Comfort Farm', 'Stella Gibbons'),
    (58, 'Nineteen Nineteen', 'John Dos Passos'),
    (59, 'Tropic of Cancer', 'Henry Miller'),
    (60, 'Scoop', 'Evelyn Waugh'),
    (61, 'Murphy', 'Samuel Beckett'),
    (62, 'The Big Sleep', 'Raymond Chandler'),
    (63, 'Party Going', 'Henry Green'),
    (64, 'At Swim-Two-Birds', 'Flann O Brien'),
    (65, 'The Grapes of Wrath', 'John Steinbeck'),
    (66, 'Joy in the Morning', 'PG Wodehouse'),
    (67, "All the King's Men", 'Robert Penn Warren'),
    (68, 'Under the Volcano', 'Malcolm Lowry'),
]

for i in bookList:
    sqlcursor.execute(f"insert ignore into all_books values {i}")
    sqlcursor.execute(f"insert ignore into available_books values {i}")

sqldatabase.commit()


home = tk.Tk()
style = ttk.Style(home)

home.columnconfigure(0, weight=2)
home.columnconfigure(1, weight=1)
home.columnconfigure(2, weight=1)

home.configure(bg="#1e2124")
style.configure(
    'TLabel',
    background="#1e2124",
    foreground="#fafafa",
)

home.title("Lotus Co")

window_width = 1500
window_height = 800
screen_width = home.winfo_screenwidth()
screen_height = home.winfo_screenheight()
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

home.geometry(
    f'{window_width}x{window_height}+{center_x}+{center_y}'
)



heading = ttk.Label(
    home,
    font=('Poiret One', 40),
    text="Welcome to Lotus Co. " + details["nickname"] + "!",
    )

heading.grid(
    row=0,
    column=0,
    columnspan=3,
    pady=30
)




noticeTitle = ttk.Label(
    home,
    text="Check It Out",
    foreground="#EC9657",
    font=('Montserrat Bold', 50),
)

noticeTitle.grid(
    row=1,
    column=0,
)


noticeText = ttk.Label(
    home,
    text="Deal of The Day : Flat " + str(random.randint(50, 100)) + "% off on select books""\nHurry! " + "Offer valid for " + str(random.randint(2, 10)) + " days!",
    foreground="#7289da",
    font=('Manrope', 20),
    justify=tk.CENTER
)

noticeText.grid(
    row=2,
    column=0
)

ttk.Label(home).grid(row=3, column=0, columnspan=3, pady=20)

infoTitle = ttk.Label(
    home,
    text="IMPORTANT",
    foreground="#39A0ED",
    font=('Montserrat Bold', 50),
)

infoTitle.grid(
    row=4,
    column=0,
)

infoText = ttk.Label(
    home,
    text="New books have been added!!  \nPlease check them out !!! ",
    foreground="#7289da",
    font=('Manrope', 20),
    justify=tk.CENTER
)

infoText.grid(
    row=5,
    column=0
)


ttk.Label(home).grid(row=1, column=1, columnspan=2, pady=20)


def openShow():
    subprocess.call(r'python show_page.py')


showButton = tk.Button(
    home,
    text="Show books",
    font=('Manrope Bold', 15),
    background="#2D8097",
    foreground="#eaeaea",
    command=openShow,
    cursor='dot',
    height=2,
    width=15,
    borderwidth=0,
    activebackground="#2D8097",
    activeforeground="#424549"
)

showButton.grid(
    row=2,
    column=1,
)


def openAdd():
    subprocess.call(r'python add_page.py')


addButton = tk.Button(
    home,
    text="Add books",
    font=('Manrope Bold', 15),
    background="#2D8097",
    foreground="#eaeaea",
    command=openAdd,
    cursor='dot',
    height=2,
    width=15,
    borderwidth=0,
    activebackground="#2D8097",
    activeforeground="#424549"
)

addButton.grid(
    row=2,
    column=2,
)


def openIssue():
    subprocess.call(r'python issue_page.py')


issueButton = tk.Button(
    home,
    text="Issue books",
    font=('Manrope Bold', 15),
    background="#2D8097",
    foreground="#eaeaea",
    command=openIssue,
    cursor="dot",
    height=2,
    width=15,
    borderwidth=0,
    activebackground="#2D8097",
    activeforeground="#424549"
)

issueButton.grid(
    row=4,
    column=1,
)


def openReturn():
    subprocess.call(r'python return_book.py')


returnButton = tk.Button(
    home,
    text="Return books",
    font=('Manrope Bold', 15),
    background="#2D8097",
    foreground="#eaeaea",
    command=openReturn,
    cursor='dot',
    height=2,
    width=15,
    borderwidth=0,
    activebackground="#2D8097",
    activeforeground="#424549"
)

returnButton.grid(
    row=4,
    column=2,
)



quitButton = tk.Button(
    home,
    text="Exit",
    font=('Manrope Bold', 15),
    background="#2D8097",
    foreground="#eaeaea",
    command=lambda: home.quit(),
    cursor='dot',
    height=2,
    width=15,
    borderwidth=0,
    activebackground="#2D8097",
    activeforeground="#424549"
)

quitButton.place(relx=0.5, rely=0.8, anchor='s')

home.mainloop()
