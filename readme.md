# 🎨 Colorful Curry

**Colorful Curry** is a lightweight Python utility for styling terminal output using composable callables. It allows you to apply terminal styles like colors, bolding, italics, and more—through clean, functional syntax. Colorful Curry is flexible enough for simple printing, advanced log parsing, and batch data processing.

---

## ✨ Overview

Colorful Curry is built around two main ideas:

- **Composable styling functions** that can wrap `print()` or any callable.
- **Flexible application of styles** based on context—whether you're iterating over lists, filtering logs, or formatting strings.

With Colorful Curry, you can chain styles together in a natural way:

```python
>>> BOLD(PURPLE)(print)("my bold purple text")
```

results in:

<span style="color: purple; font-weight: bold;">my bold purple text</span>

---

## Getting Started

It's super easy, barely an inconvience:

```python
from colorful_curry import *
```

Now you can wrap callables with ANSI styles!

## ✅ Use Cases

---

# Terminal Printing

At its simplest, Colorful Curry can wrap `print()` for quick, styled output. This is useful for scripts, CLI tools, or simple demos where you want visual differentiation without extra dependencies.

---

# Prepared Styles

It's easy to style a function for future use:

```python
log_info = GREEN(logger.info)

# and then...

log_info("log this info")
```

## Comprehensions and Bulk Output

Colorful Curry works seamlessly in list comprehensions or loops. You can apply the same style across a collection of data without writing repetitive code. This is helpful when processing lists of items or displaying formatted summaries in the terminal.

---

### Filtering Data with Styling

Colorful Curry pairs well with Python’s `filter()` and similar patterns. You can style only the subset of data you care about while ignoring the rest. This is great for highlighting matching entries from lists or log files.

---

### Alternating Styles (e.g., Every Other Line)

A common requirement when reading large files or logs is alternating line styles for readability. Colorful Curry makes this easy by letting you alternate styling functions dynamically inside a loop, providing visual distinction line-by-line.

---

### Log File Highlighting

Colorful Curry is particularly useful for styling log files based on log levels (INFO, ERROR, DEBUG, etc.). You can map log levels to specific styles and highlight them during output, making it easier to spot warnings or errors in real time.

---

### Returning Styled Strings

In addition to printing, Colorful Curry supports strin literals and string-returning functions. This allows you to build styled strings and use them in other contexts—like logging frameworks, email generation, or UI toolkits—without immediate printing.

---

## ⚙️ Design Goals

- **Readable syntax** with minimal overhead.
- **Composable design**—styles can be chained as needed.
- **Versatile output**—supporting both printing and string transformation.
- **Lightweight implementation** with no external dependencies.

---

## 📄 License

MIT License. Use freely in personal and commercial projects.
