from .ui import Menu, MenuChoice
from .generators import char, password
from .datetime import time


MENU = Menu(
    [
        MenuChoice(1, char.__name__, char.demo),
        MenuChoice(2, password.__name__, password.demo),

        MenuChoice(3, time.__name__, time.demo),

        MenuChoice(0, 'Exit', lambda: exit(0)),
    ],
    prompt_for_input="Just tell me what do you want",
    invalid_choice_message="I didn't hear you, please repeat.",
)

print("Welcome to little house of Gutgin!")
print("How can i help you?")
MENU.interact()
