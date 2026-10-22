laugh_emoji = "😍"
smile_emoji = "😊"


def create_character(character_name, strength, intelligence, charisma):
    if not isinstance(character_name, str):
        return 'The character name should be a string'
    if character_name == '':
        return 'The character should have a name'
    if len(character_name) > 10:
        return 'The character name is too long'
    if ' ' in character_name:
        return 'The character name should not contain spaces'
    if not isinstance(strength, int) or not isinstance(intelligence, int) or not isinstance(charisma, int):
        return 'The character attributes should be integers'
    if strength < 1 or intelligence < 1 or charisma < 1 :
        return 'The character strenght should be no less than 1'
    if strength > 4 or intelligence > 4 or charisma > 4:
        return 'The character attributes should be no more than 4'
    if sum([strength, intelligence, charisma]) > 7:
        return 'The total of the character should start with 7'
    
    return (
        f'{character_name}\n'
        f'STR: {laugh_emoji * strength}{smile_emoji * (10 - strength)}\n'
        f'INT: {laugh_emoji * intelligence}{smile_emoji * (10 - intelligence)}\n'
        f'CHA: {laugh_emoji * charisma}{smile_emoji * (10 - charisma)}'
        )
kassim_character = create_character('Ever', 2, 2, 3) 
print(kassim_character)