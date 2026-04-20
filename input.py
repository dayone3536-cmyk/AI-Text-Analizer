#Take the input and dectect Sad or happy or neutral
import requests

class Text_analizer():
    def __init__(self,take_input, mood):    
        self.take_input = take_input #"x"
        self.mood = mood

    def inputing(self): #why self --because when i pass it inputing(the methode)automatically passes the self object to it
        self.take_input = input("Enter a sentence")

    def dectecing_mood(self):
        happy = ["happy", "exited", "enjoying", "enjoyed", "love", "like", "loved", "happiest", "happier", "exiting",
                 "great", "awesome","good","amazing", "fun", "wonderful", "god", "money", "passion", "purpose"] #16
        
        sad = ["not happy","not great","depressed","sad","unhappy","jealous","hate","unactractive","dont love", 
        "dont like", "not awesome","worst", "baddest", "not in love", "life", "intense", "consciousness", "work", "skills"
        "joblessness","relevance","values"] #count == 13

        words = self.take_input

        words = words.split()
        words = set(words)

        #Happy mood 😊😊
        for happy_mood in happy:  
            for word in words:
                if happy_mood == word:
                    return happy_mood

        
        #sad mood 😭😭
        for sad_mood in sad:
            for word in words:
                if sad_mood == word:
                    return sad_mood

class Quotes():
    def __init__(self,take_appropriate_quote):
        self.take_appropriate_quote = take_appropriate_quote
        pass

    def fecting_data(self): #fecth data from the PaperQuotes API
        
        url = "https://api.paperquotes.com/apiv1/quotes/?tags=love,life&curated=1"
        while True:
            data = requests.get(url)

            data = data.json()
                # print(data)

            take_input = Text_analizer("pass", "neutral")

            take_input.inputing()
            mood = take_input.dectecing_mood()

            seen_quotes = {}
                #remove duplicates aand loop 
            seen_quotes = set()

            for quotes in data["results"]:
                if quotes["quote"] not in seen_quotes:
                    seen_quotes.add(quotes["quote"])

                    if mood in quotes["tags"]:
                            print(quotes["quote"])
                            print()
                
            if mood not in quotes["tags"]:
                print(quotes["quote"])
                print()


            ask = input("Do you want to exit?(y/n)").lower()
            if ask in ["y", "yes"]:
                print("Thanks for visiting Text Analizer AI. ")
                break

            else:
                url = data["next"]
                print(url)
                continue

fecting_quotes = Quotes("something")

fecting_quotes.fecting_data()