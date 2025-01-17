from datetime import datetime
from journal_entry import JournalEntry
import mysql.connector
import getpass
import bcrypt 


# CONNECT TO DATABASE
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Password",
    database="daisy"
)
# CREATE A CURSOR TO POINT TO CHOSEN DATABASE
cursor = db.cursor()
#GLOBAL ID TO TRACK USER ID OF LOGGED IN USER
gbl_user_id = None

#FUNCTIONS
def hash_pw(password):
    pw_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_passwd = bcrypt.hashpw(pw_bytes, salt)
    return hashed_passwd
def pw_check(stored_pwhash, password_attempt):
    stored_pwhash = stored_pwhash.encode('utf-8')
    return bcrypt.checkpw(password_attempt.encode('utf-8'), stored_pwhash)
def welcome():
    print("\n\n==== Welcome To Daisy ====")
    print("\n==== your CBT journal ====")
def add_entry(new_entry, todays_date, user_id):
    
    mood = new_entry.get_mood()
    tolerance_score = new_entry.get_t_score()
    reaction = new_entry.get_reaction()
    
    cursor.execute("INSERT INTO entry (emotion, tol_score, reaction, date_added, user_id)VALUES (%s,%s,%s,%s,%s)", 
                               (mood, tolerance_score, reaction, todays_date, user_id))
    db.commit()
def view_entries(user_id):
    cursor.execute("SELECT * FROM entry WHERE user_id=%s", (user_id,))
    for entry in cursor.fetchall():
        print(f"\nEntry No: {entry[0]}\nMood: {entry[1]}, Tolerance Score: {entry[2]}, Reaction: {entry[3]}\nDate Added: {entry[4]}")       
def delete_entry(user_id):
    while True:
        try:
            id = int(input("\nEnter the 'Entry No' to delete: "))
            cursor.execute("DELETE FROM entry WHERE entry_id=%s AND user_id=%s", (id,user_id))
            db.commit()
            print(f"\nEntry {id} deleted....")
            break
        except ValueError:
            print("Error, please enter a valid number!!")            
def register():
    username = input("Enter a username: ")
    email = input("Enter email: ")
    passwd = input("Create a password: ")
    hashed_passwd = hash_pw(passwd)
    
    cursor.execute("INSERT INTO user (username, email, passwd) VALUES (%s,%s,%s)", (username, email, hashed_passwd))
    db.commit()
    print(f"{username} added! Please login!")
    login()   
def login():
    
    global gbl_user_id
    
    while True:
        choice = int(input("\nWelcome, please choose: \n\n1) Login\n2) Register\n\nEnter: "))
        
        if choice == 1:
            print("\nPlease Login")
            
            username = input("\nUsername: ")
            passwd = getpass.getpass("Password: ")

            cursor.execute("SELECT user_id, username, passwd FROM user WHERE username=%s", (username,))
            user = cursor.fetchone()
            
            if user:
                stored_id = user[0]
                stored_pwhash = user[2]
                
                
                if pw_check(stored_pwhash, passwd):
                    gbl_user_id = stored_id  
                    print("\n.....Login Successful")
                    main()
                else:
                    print("\nLogin failed, please try again.")
            else:
                print("\nError logging in....")
        elif choice == 2:
            register()

def main():

    curr_date = datetime.now()
    todays_date = curr_date.strftime("%Y-%m-%d %H:%M:%S")
    new_entry = JournalEntry()
    
    while True:

        try:     
            choice = int(input("\nWhat would you like to do?\n\n1) Add new entry\n2) View entries \n3) Delete entry\n4) Exit \n\nEnter: "))
    
            if choice == 1:
                add_entry(new_entry, todays_date, gbl_user_id)
            elif choice == 2:
                view_entries(gbl_user_id)
            elif choice == 3:
                delete_entry(gbl_user_id)
            elif choice == 4:
                print(f"\n\n...goodbye!\n")
                quit()
        except ValueError:
            print("Error...Enter 1, 2, 3, or 4.")
        

if __name__ == "__main__":
    welcome()
    login()
        

