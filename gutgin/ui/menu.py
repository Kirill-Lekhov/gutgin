from typing import Sequence

from .menu_choice import MenuChoice


class Menu:
    def __init__(
        self,
        choices: Sequence[MenuChoice],
        prompt_for_input: str = "Enter your choice",
        invalid_choice_message: str = "Invalid choice. Try again.",
    ):
        self.choices: Sequence[MenuChoice] = choices
        self.prompt_for_input: str = prompt_for_input
        self.invalid_choice_message: str = invalid_choice_message

    def __str__(self) -> str:
        return ';\n'.join(map(str, self.choices)) + '.'

    def interact(self):
        while True:
            print(self)
            selected_choice = input(self.prompt_for_input + ': ')
            choice_trigger = any(map(lambda x: x.run_if_selected(selected_choice), self.choices))

            if not choice_trigger:
                print(self.invalid_choice_message)
