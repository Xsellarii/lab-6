barsik = {'animal': 'cat', 'owner': 'Jim'}
rex = {'animal': 'dog', 'owner': 'Alex'}
kesha = {'animal': 'parrot', 'owner': 'Elena'}

pets = [barsik, rex, kesha]

for pet in pets:
    print(f"{pet['owner']} is the owner of a pet - a {pet['animal']}.")