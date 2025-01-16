class JournalEntry:
    
    def __init__(self, mood=str, tolerance_score=int, reaction=str, date=str):
        self.mood = mood
        self.tolerance_score = tolerance_score
        self.reaction = reaction
        self.date = date
    

    def get_mood(self):
        mood = input("\nHow are you feeling?: ")
        return mood
    def get_t_score(self):
        while True:
            try: 
                tolerance_score = int(input("\nOn a scale of 0 - 5, with 5 being Intolerable, rate your emotion: "))
                return tolerance_score
            except ValueError:
                print("Please enter a number between 0-5")
    def get_reaction(self):
         reaction = input("\nHow did you handle feeling like this?: ")
         return reaction

    