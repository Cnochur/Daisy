from datetime import datetime
from journal_entry import JournalEntry
import mysql.connector


# CONNECT TO DATABASE
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Password",
    database="daisy"
)

cursor = db.cursor()

def welcome():
    print("\n\n==== Welcome To Daisy ====")
    print("\n==== your CBT journal ====")
def add_entry(new_entry, todays_date):
    
    mood = new_entry.get_mood()
    tolerance_score = new_entry.get_t_score()
    reaction = new_entry.get_reaction()
    
    cursor.execute("INSERT INTO entry (emotion, tol_score, reaction, date_added)VALUES (%s,%s,%s,%s)", 
                               (mood, tolerance_score, reaction, todays_date))
    db.commit()
def view_enteries():
    cursor.execute("SELECT * FROM entry")
    for entry in cursor.fetchall():
        print(f"\nEntry No: {entry[0]}\nMood: {entry[1]}, Tolerance Score: {entry[2]}, Reaction: {entry[3]}\nDate Added: {entry[4]}")
def delete_entry():
    while True:
        try:
            id = int(input("\nEnter the 'Entry ID' to delete: "))
            cursor.execute("DELETE FROM entry WHERE entry_id=%s", (id,))
            db.commit()
            print(f"\nEntry {id} deleted....")
            break
        except ValueError:
            print("ERROR!!!")
        
def main():
    welcome()
    curr_date = datetime.now()
    todays_date = curr_date.strftime("%Y-%m-%d %H:%M:%S")
    new_entry = JournalEntry()
    
    while True:

        try:     
            choice = int(input("\nWhat would you like to do?\n\n1) Add new entry\n2) View entries \n3) Delete entry\n4) Exit \n\nEnter: "))
    
            if choice == 1:
                add_entry(new_entry, todays_date)
            elif choice == 2:
                view_enteries()
            elif choice == 3:
                delete_entry()
            elif choice == 4:
                print(f"\n\n...goodbye!\n")
                break
        except ValueError:
            print("Error...Enter 1, 2, 3, or 4.")
        

if __name__ == "__main__":
    main()
        

