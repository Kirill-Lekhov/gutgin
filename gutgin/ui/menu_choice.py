from typing import Any, Optional


class MenuChoice:
    def __init__(
        self,
        short_designation: Any,
        title: Any,
        callback: Optional[callable] = None,
        description: Any = '',
        template: str = '{short_designation}) {title}'
    ):
        self._short_designation: str = str(short_designation)
        self._title: str = str(title)
        self._callback: Optional[callback] = callback
        self._description: str = str(description)
        self._template: str = template

    def __str__(self) -> str:
        return self._template.format(
            short_designation=self._short_designation,
            title=self._title,
            description=self._description,
        )

    @property
    def short_designation(self) -> str:
        return self._short_designation

    def run_if_selected(self, choice: Any) -> bool:
        if self.short_designation == str(choice):
            if self._callback is not None:
                self._callback()

            return True

        return False
