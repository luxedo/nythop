# Nyhtop: The Python Replacement You Never Knew You Didn’t Need

[![PyPI - Version](https://img.shields.io/pypi/v/nythop.svg)](https://pypi.org/project/nythop)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/nythop.svg)](https://pypi.org/project/nythop)
[![License: GPL v3](https://img.shields.io/badge/License-GPL_v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0.en.html)
![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/luxedo/nythop/publish.yml)
![Codecov](https://img.shields.io/codecov/c/github/luxedo/nythop)
![CodeFactor Grade](https://img.shields.io/codefactor/grade/github/luxedo/nythop)

---

Nyhtop is here to revolutionize your coding experience by turning Python on its head – literally.
Forget the simplicity and readability of Python; Nyhtop takes that elegance and adds an exciting
twist: every line is written backwards! With Nyhtop, code clarity reaches a whole new level (of
confusion), promising an impressively awkward and cryptic experience that will have you wondering
how you ever tolerated straightforward syntax.

Nyhtop enthusiasts argue that it’s not just Python – it’s Python improved. Indentation wars?
Resolved. All your indentation happens at the end of the line, so tabs vs. spaces is no longer a
battle you can even see. And comments? They’re read from right to left, so cryptic notes and
backward logic are just part of the _Nythopic_ experience.

If you’re tired of the predictability and accessibility of Python, Nyhtop promises to shake things
up by keeping things just familiar enough to fool you into thinking you know what’s happening. But
in practice? It’s perfectly unreadable – just as any good esolang should be.

Ready to leave Python behind? Let’s dive in!

---

## Table of Contents

- [Installation](#installation)
- [Coding](#coding)
- [Running](#running)
- [License](#license)

## Installation

Nyhtop is available on [PyPI](https://pypi.org/project/nythop/), so you can install it in seconds
if you’re ready to turn Python upside-down. Just run:

```bash
pip install nythop
```

And that’s it! You’re now equipped to enjoy the _Nythop_ experience.

## Coding

Nyhtop is, at its core, just Python – but backwards. Every line is simply a reversed version of
Python syntax, which means if you’re already familiar with Python, you’re halfway there (or perhaps
halfway confused). Any valid Python code can be adapted to Nyhtop by flipping each line from right
to left. For example:

```python
print("Hello, World!")
```

```
)"!dlroW ,olleH"(tnirp
```

That’s it. No new keywords, no unfamiliar constructs – just reversed lines of Python code. Of
course, this makes even the simplest tasks look cryptic, but it’s still technically Python.
Indentation (the invisible kind) happens at the end of each line, so the usual debate over tabs
vs. spaces doesn’t apply here.

Check out some of the possible `for` loop versions:

```
# Using the character ␠ to visualize whitespaces
:)01(egnar ni i rof
)"}20:i{ retI"f(tnirp␠␠␠␠

# You can move things around within the line, just don't mess with the invisible indentation at the end.
                                :)01(egnar ni i rof
)"}20:i{ retI"f(tnirp␠␠␠␠

# Maybe you're feeling adventurous and want to make it feel right.
      :)01(egnar ni i rof
)"}20:i{ retI"f(tnirp␠␠␠␠
```

Once you get used to this “improvement,” you’ll find Nyhtop code offers the same functionality as
Python but with the added benefit of looking impressively perplexing.

## Running

### Running Nyhtop from a File

Given the example file `hello_world.yp`:

```
)"!dlroW ,olleH"(tnirp
```

Run it with:

```bash
nyhtop hello_world.yp
```

### Running Nyhtop with a Command

Alternatively, you can run Nyhtop code directly from the command line with the -c option:

```bash
nythop -c ')"!dlroW ,olleH"(tnirp'
```

### Interactive REPL

To explore Nyhtop’s logic on the fly, you can start an interactive REPL session by simply running:

```bash
nyhtop
```

The REPL will wait for your input in a prompt format. Type `)(tixe` when you’re ready to escape.

## License

`nythop` is distributed under the terms of the [GPL-3.0-or-later](https://spdx.org/licenses/GPL-3.0-or-later.html) license.
