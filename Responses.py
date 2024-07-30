from random import choice, randint

def get_response(user_input: str) -> str:
    #the logic of the responses can be greatly improved by learning abt ai chatbots
    lowered: str = user_input.lower()

    if lowered == ' ':
        return "Ok, be like that ◔̯◔ "
    elif 'hello' in lowered:
        return 'Whats up'
    elif 'bye' in lowered:
        return 'Alr see u later gang'
    elif 'how are you' in lowered:
        return 'Been better, due for a win'
    elif 'roll dice' in lowered:
        return f'You rolled: {randint(1,6)}'
    else:
        return choice([
            "Do you really think I'm programmed to respond to that",
            "Hwhat is bro on about",
            "Bros yapping",
            "yeah idc bro",
            "ok but like say something else tho idk how to respond to that",
        ])
    
    