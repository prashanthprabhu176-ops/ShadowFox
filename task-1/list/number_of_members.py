# You have a list of superheroes representing the Justice
# League.
# justice_league = [
#     "Superman",
#     "Batman",
#     "Wonder",
#     "Woman",
#     "Flash",
#     "Aquaman",
#     "Green Lantern",
# ]


justice_league = [
    "Superman",
    "Batman",
    "WonderWoman",
    "Flash",
    "Aquaman",
    "Green Lantern",
]
print("Number of members in Justice League", len(justice_league))

justice_league.append("Batgirl")
justice_league.append("NightWing")
# 2.['Superman', 'Batman', 'WonderWoman', 'Flash', 'Aquaman', 'Green Lantern', 'Batgirl', 'NightWing']

justice_league[0], justice_league[2] = justice_league[2], justice_league[0]
print(justice_league)
# 3. ['WonderWoman', 'Batman', 'Superman', 'Flash', 'Aquaman', 'Green Lantern', 'Batgirl', 'NightWing']

# 4 . Aquaman and Flash are having conflicts, and you need to separate them.
# Choose either "Green Lantern" or "Superman" and move them in between Aquaman and Flash.

justice_league[4], justice_league[5] = justice_league[5], justice_league[4]
print(justice_league)

# new members in the list
justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]

print(justice_league)

# Guess the leader

print(sorted(justice_league))
# ['Cyborg', 'Green Arrow', 'Hawkgirl', 'Martian Manhunter', 'Shazam']
# Cyborg is the new leader of Justice League
