food = input("Please enter a food: ")
name = input("Please enter a name: ")
adjective = input("Please enter an adjective: ")
noun = input("Please enter an animal: ")
noun2 = input("Please enter a noun: ")
verb = input("Please enter a verb: ")
number = int(input("Please enter an amount of dollars: "))
number2 = int(input("Please enter an amount in cents: "))

money = number + number2/100

if money <= 50:
    sentence = f'''Her friends said "yes" and gave her the ${money:.2f}. But they said, "This is a one 
time thing. We can't always do this." They said, "Next time, you should just eat the food that we offer."
And they said jokingly, "Maybe next time you'll pay for us :)'''
elif money > 50 and money <= 100:
    sentence = f'''Her friends said, "Don't you think that's a bit much money for school food?
Here is $20 instead. This should be enough. If it isn't tell us and we'll give you more. You owe us $20 
or as much as you use because we offered you our food and you said noand that hurt our feelings. :("'''
else:
    sentence = f'''Her friends said, "That's way too much money for school food. 
You don't need that much. What do you need that much money for?"'''

print()
story = f'''It was {food} day at school, and {name} was super {adjective} for lunch. 
But when she went outside to eat, a {noun} stole her {food}! {name} chased the {noun}
all over school. She {verb} through the playground. Then she tripped on her {noun2} and 
the {noun} escaped! Luckily, {name}'s friends were willing to share their {food} with her,
but she doesn't want the {food} that they gave her. So she asked if they could give her
${number}.{number2}. {sentence}'''

print(story)