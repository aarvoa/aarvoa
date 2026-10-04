import requests

resp = requests.get("https://api.github.com/repos/backstage/backstage/releases")

count = 0

emoji = input("Enter a reaction from laugh, hooray, confused, heart, rocket, eyes!: ")

for i in resp.json():
    reactions = i.get("reactions")
    if reactions != None:
        count = count + int(reactions.get(emoji))
        
    
print(f"There are {count} Emojis of {emoji}")