from datetime import datetime
from journal_entry import JournalEntry

def welcome():
    print("\n\n==== Welcome To Daisy ====")
    print("\n==== your CBT journal ====")
def view_enteries(journal):
    for ind, entry in enumerate(journal, start=1):
        print(f"\n{ind}){entry.date} \nMood: {entry.mood}\nTolerance Score: {entry.tolerance_score}\nHow I reacted: {entry.reaction}")
        print("-----------------------------")
def main():
    welcome()
    curr_date = datetime.now()
    todays_date = curr_date.strftime("%A: %d/%m/%Y (%H:%M)")
    journal = []
    new_entry = JournalEntry
    
    while True:

        try:     
            choice = int(input("\nWhat would you like to do?\n\n1) Add new entry\n2) View entries \n3) Delete entry (Soon)\n4) Exit \n\nEnter: "))
    
            if choice == 1:
                mood = new_entry.get_mood()
                tolerance_score = new_entry.get_t_score()
                reaction = new_entry.get_reaction()
                journal.append(new_entry(mood, tolerance_score, reaction, todays_date))
            elif choice == 2:
                view_enteries(journal)
            elif choice == 3:
                print("....no!")
                pass
            elif choice == 4:
                print(f"\n\n...goodbye!\n")
                break
        except ValueError:
            print("Error...Enter 1, 2, 3, or 4.")
        

if __name__ == "__main__":
    main()
        

