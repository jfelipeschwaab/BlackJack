Numbers = [2,3,4,5,6,7,8,9,'J', 'Q', 'K', 'A']
Nipes = ['Copa', 'Ouro', 'Espada', 'Paus']
Cards = []

for number in Numbers:
    for nipe in Nipes:
        Cards.append(f'{number} of {nipe}')
print(Cards)
        
