import questionary

country = questionary.rawselect("Choose a foreign country", ["Brazil", "China", "USA", "France", "Sweden", "Egypt", "Germany"]).ask()
adverb1 = questionary.rawselect("Choose an adverb", ["safely", "carefully", "elegantly", "immediately"]).ask()
adjective1 = questionary.rawselect("Choose an adjective", ["crazy", "gorgeous", "calm", "aggressive"]).ask()
animal = questionary.rawselect("Choose an animal", ["cow", "tiger", "elephant", "mouse"]).ask()
verb_ing1 = questionary.rawselect("Choose a verb ending in ing", ["lurking", "waiting", "laughing", "dancing"]).ask()
verb1 = questionary.rawselect("Choose a verb", ["eat", "help", "catch", "smell"]).ask()
verb_ing2 = questionary.rawselect("Choose a verb ending in ing", ["crossing", "jumping over", "drinking", "throwing"]).ask()
adverb2 = questionary.rawselect("Choose an adverb", ["quickly", "carefully", "terribly", "well"]).ask()
adjective2 = questionary.rawselect("Choose an adjective", ["angry", "happy", "sad", "scared"]).ask()
place = questionary.rawselect("Choose a place", ["barn", "house", "farm", "field"]).ask()
liquid = questionary.rawselect("Choose a liquid", ["water", "seltzer", "soda", "apple juice"]).ask()
body_part = questionary.rawselect("Choose a body part", ["foot", "leg", "arm", "stomach"]).ask()
verb2 = questionary.rawselect("Choose a verb", ["swim", "splash", "jump", "dive"]).ask()

story = f"""If you are traveling in {country} and find yourself having to cross a piranha-filled river, here's how to do it {adverb1}: 
    - Piranhas are more {adjective1} during the day, so cross the river at night.
    - Avoid areas with netted {animal} traps - piranhas may be {verb_ing1} there looking to {verb1} them!
    - When {verb_ing2} the river, swim {adverb2}. You don't want to wake them up and make them {adjective2}.
    - Whatever you do, if you have an open wound, try to find another way to get back to the {place}. Piranhas
    are attracted to fresh {liquid} and will most likely take a bite out of your {body_part} if you {verb2} in the water!
"""

print(story)