from typing import Optional, List

from .char import CharGenerator


class PasswordGenerator:
    def __init__(
        self,
        length: int = 30,
        use_alphas: bool = True,
        use_numerics: bool = True,
        use_specs: bool = True,
        ignore_chars: Optional[List[str]] = None,
        additional_chars: Optional[List[str]] = None,
    ):
        self.char_generator = CharGenerator(use_alphas, use_numerics, use_specs, ignore_chars, additional_chars)
        self.length = length

    def __next__(self) -> str:
        return ''.join([next(self.char_generator) for _ in range(self.length)])

    def __iter__(self):
        return self


def demo():
    passwd_number = 5
    passwd_generator = PasswordGenerator()

    print(f"\nNow I will generate {passwd_number} random passwords:")
    print(*[next(passwd_generator) for _ in range(passwd_number)], sep='\n', end='\n\n')
