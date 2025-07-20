from enum import Enum

from enum import StrEnum

class AnsiStyle(StrEnum):
    """
    An enumeration of ANSI escape codes for text styling, grouped by kind.
    Value format: (kind, code).
    """

    def __new__(cls, kind, code):
        obj = str.__new__(cls)
        obj._value_ = code      # The enum "value" is the ANSI code string
        obj.kind = kind         # Additional attribute for kind
        return obj

    # Control Codes
    RESET = ("control", "\033[0m")

    # Text Colors
    BLACK = ("text", "\033[30m")
    RED = ("text", "\033[31m")
    GREEN = ("text", "\033[32m")
    YELLOW = ("text", "\033[33m")
    BLUE = ("text", "\033[34m")
    MAGENTA = ("text", "\033[35m")
    CYAN = ("text", "\033[36m")
    WHITE = ("text", "\033[37m")

    # Bright Text Colors
    BRIGHT_BLACK = ("bright text", "\033[90m")
    BRIGHT_RED = ("bright text", "\033[91m")
    BRIGHT_GREEN = ("bright text", "\033[92m")
    BRIGHT_YELLOW = ("bright text", "\033[93m")
    BRIGHT_BLUE = ("bright text", "\033[94m")
    BRIGHT_MAGENTA = ("bright text", "\033[95m")
    BRIGHT_CYAN = ("bright text", "\033[96m")
    BRIGHT_WHITE = ("bright text", "\033[97m")

    # Background Colors
    BG_BLACK = ("background", "\033[40m")
    BG_RED = ("background", "\033[41m")
    BG_GREEN = ("background", "\033[42m")
    BG_YELLOW = ("background", "\033[43m")
    BG_BLUE = ("background", "\033[44m")
    BG_MAGENTA = ("background", "\033[45m")
    BG_CYAN = ("background", "\033[46m")
    BG_WHITE = ("background", "\033[47m")

    # Text Decorations
    BOLD = ("decoration", "\033[1m")
    ITALIC = ("decoration", "\033[3m")
    UNDERLINE = ("decoration", "\033[4m")
    MARKTHROUGH = ("decoration", "\033[9m")

    @classmethod
    def _members_by_kind(cls, kind):
        return tuple(member for member in cls if member.kind == kind)

    @classmethod
    def text(cls):
        return cls._members_by_kind("text")

    @classmethod
    def bright_text(cls):
        return cls._members_by_kind("bright text")

    @classmethod
    def background(cls):
        return cls._members_by_kind("background")

    @classmethod
    def decoration(cls):
        return cls._members_by_kind("decoration")

    @classmethod
    def styles(cls):
        """All styles except control/reset ones (exclude 'reset')."""
        return tuple(
            member
            for member in cls
            if member.kind != "reset"
        )


class Style:
    def __init__(self, code):
        self.code = code

    def __call__(self, target):
        if isinstance(target, Style):
            # If target is another Style, concatinate them
            return Style(self.code + target.code)
        elif callable(target):
            # If target is a callable, try to wrap it with a style
            def wrapped(*args, **kwargs):
                # if target accepts a string, apply style to the first argument
                if args and isinstance(args[0], str):
                    return target(self(args[0]))
                # target doesn't accept a string, call it and wrap the result
                else:
                    return self(target(*args, **kwargs))
            return wrapped
        elif isinstance(target, str):
            # If target is a string, apply style directly
            return f"{self.code}{target}{AnsiStyle.RESET.value}"
        else:
            # If target is not a string, callable, or style, raise an error
            raise TypeError(f"Cannot apply Style to {type(target).__name__}")


def make_style(style_enum):
    return Style(style_enum.value)

# Dynamically inject into globals() and __all__
__all__ = []
for style_enum in AnsiStyle.styles():
    globals()[style_enum.name] = make_style(style_enum)
    __all__.append(style_enum.name)

