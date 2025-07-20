# test_colorful_curry.py
import unittest
from colorful_curry import *
from colorful_curry import AnsiStyle
import io
import sys

class TestColorfulCurry(unittest.TestCase):

    def test_style_side_effects(self):
        # Capture stdout
        captured_output = io.StringIO()
        sys.stdout = captured_output

        RED(print)("test")

        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        self.assertIn("test", output)
        self.assertIn(AnsiStyle.RED, output)  # ANSI escape sequence present
        self.assertTrue(output.strip().endswith(AnsiStyle.RESET), "Output should end with reset ANSI code")

    def test_style_literal(self):
        # Test that the style literal works as expected
        styled_text = GREEN("This is green text")
        expected = f"{AnsiStyle.GREEN.value}This is green text{AnsiStyle.RESET.value}"
        self.assertEqual(styled_text, expected)

    def test_style_function(self):
        # Test  styling function then calling 
        def sample_function():
            return "test"

        styled_function = GREEN(sample_function)
        result = styled_function()
        expected = f"{AnsiStyle.GREEN.value}test{AnsiStyle.RESET.value}"
        self.assertEqual(result, expected)

    def test_style_invalid_type(self):
        with self.assertRaises(TypeError) as context:
            GREEN(1234)  # Invalid target type, should raise TypeError

        self.assertIn("Cannot apply Style to int", str(context.exception))

    def test_style_composition(self):
        result = BOLD(RED)("important")
        expected = f"{AnsiStyle.BOLD.value}{AnsiStyle.RED.value}important{AnsiStyle.RESET.value}"
        self.assertEqual(result, expected)
    
    def test_prepared_styles(self):
        style = BOLD(BG_YELLOW(CYAN))
        result = style("pipeline")
        expected = f"{AnsiStyle.BOLD.value}{AnsiStyle.BG_YELLOW.value}{AnsiStyle.CYAN.value}pipeline{AnsiStyle.RESET.value}"
        self.assertEqual(result, expected)
    
    def test_function_output_styling(self):
        # call a function that returns a string and apply style
        def message():
            return "hello"
        styled_message = UNDERLINE(message)()
        expected = f"{AnsiStyle.UNDERLINE.value}hello{AnsiStyle.RESET.value}"
        self.assertEqual(styled_message, expected)

    def test_dynamic_style_factory(self):
        def style_for_status(status):
            return {
                "ok": GREEN,
                "warn": CYAN,
                "error": RED
            }.get(status, WHITE)
        
        self.assertEqual(f"{AnsiStyle.GREEN.value}OK{AnsiStyle.RESET.value}", style_for_status("ok")("OK"))
        self.assertEqual(f"{AnsiStyle.CYAN.value}WARNING{AnsiStyle.RESET.value}", style_for_status("warn")("WARNING"))
        self.assertEqual(f"{AnsiStyle.RED.value}ERROR{AnsiStyle.RESET.value}", style_for_status("error")("ERROR"))
        self.assertEqual(f"{AnsiStyle.WHITE.value}DEFAULT{AnsiStyle.RESET.value}", style_for_status("unknown")("DEFAULT"))

    def test_pipeline_with_reduce(self):
        from functools import reduce
        pipeline = [BOLD, BG_MAGENTA, WHITE]
        style = reduce(lambda f, g: g(f), pipeline, lambda s: s)
        result = style("combined")
        expected = f"{AnsiStyle.BOLD.value}{AnsiStyle.BG_MAGENTA.value}{AnsiStyle.WHITE.value}combined{AnsiStyle.RESET.value}{AnsiStyle.RESET.value}{AnsiStyle.RESET.value}"
        self.assertEqual(result, expected)

    def test_list_comprehension_with_inline_conditional(self):
        items = ["ok", "warn", "error", "unknown"]

        styled = [
            (GREEN(item.upper()) if item == "ok" else RED(item.upper()))
            for item in items
        ]

        expected = [
            f"{AnsiStyle.GREEN.value}OK{AnsiStyle.RESET.value}",
            f"{AnsiStyle.RED.value}WARN{AnsiStyle.RESET.value}",
            f"{AnsiStyle.RED.value}ERROR{AnsiStyle.RESET.value}",
            f"{AnsiStyle.RED.value}UNKNOWN{AnsiStyle.RESET.value}",
        ]

        self.assertEqual(styled, expected)

    def test_map_with_style(self):
        items = ["apple", "banana", "cherry"]
        styled_items = list(map(GREEN, items))
        
        expected = [
            f"{AnsiStyle.GREEN.value}apple{AnsiStyle.RESET.value}",
            f"{AnsiStyle.GREEN.value}banana{AnsiStyle.RESET.value}",
            f"{AnsiStyle.GREEN.value}cherry{AnsiStyle.RESET.value}",
        ]
        
        self.assertEqual(styled_items, expected)


## map

if __name__ == "__main__":
    unittest.main()
