from random import choice, getrandbits
from typing import Optional, List


class CharGenerator:
    ALPHAS = ''.join(map(chr, range(ord('a'), ord('z') + 1)))
    NUMERICS = ''.join(map(str, range(10)))
    SPECS = "!@#$%^&*()_+=-~`][}{\"':?/.,<>\\|"

    def __init__(
        self,
        use_alphas: bool = True,
        use_numerics: bool = True,
        use_specs: bool = True,
        ignore_chars: Optional[List[str]] = None,
        additional_chars: Optional[List[str]] = None,
    ):
        self.chars_set = ""

        if use_alphas:
            self.chars_set += self.ALPHAS

        if use_numerics:
            self.chars_set += self.NUMERICS

        if use_specs:
            self.chars_set += self.SPECS

        if additional_chars is not None:
            self.chars_set += ''.join(additional_chars)

        ignore_chars = [] if ignore_chars is None else ignore_chars

        for char in ignore_chars:
            self.chars_set.replace(char, '')

    def __next__(self) -> str:
        char = choice(self.chars_set)
        char = char.upper() if bool(getrandbits(1)) else char
        return char

    def __iter__(self):
        return self


def demo():
    char_number = 10
    char_generator = CharGenerator()

    print(f"\nNow I will generate {char_number} random characters:")
    print(*[next(char_generator) for _ in range(char_number)], sep='\n', end='\n\n')
