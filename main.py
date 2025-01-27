# ijaw-English Dictonary

# Dictonary data
ijaw_dictonary = {
     "ame": "water",
     "anj": "land",
     "bere": "fish",
     "diro": "tree",
     "eke": "house",
     "feru": "sky",
     "ibe": "boat",
     "ine": "food",
     "kpereke": "moon",
     "kpo": "stone",
     "moto": "man",
     "oku": "sun",
     "ola": "gold",
     "piri": "river",
     "temo": "bird",
     "wuo": "forest",
     "yin": "love",
     "ziri": "peace"
     }
def main():
     print("welcome to the Ijaw-English Dictonary!")
     print("Type a word in ijaw to get its English meaning.")
     print("Type 'exit' to quit the dictonary.\n")

     while True:
           #Get user input
           word = input("Enter an ijaw word: ").strip().lower()

           if word== "exit":
               print("Thank you for using the Ijaw-English Dictonary. Goodbye!")
               break
           elif word in ijaw_dictonary:
                print(f"The English meaning of the '{word}' is '{ijaw_dictonary[word]}'.\n")
           else:
               print(f"sorry. '{word}' is not in the dictonary.\n")
if __name__ == "__main__":
     main()