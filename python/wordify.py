import requests

print("Wordify!")

api = "https://random-word-api.herokuapp.com/word?length=5&diff=1"

word = requests.get(api)
print(word.json())

ans = input("")

if ['ans'] == word:
    print(f"You won the word was {word}")