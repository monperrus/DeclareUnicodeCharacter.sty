# DeclareUnicodeCharacter.sty

A LaTeX package that enables the use of unicode/utf8 characters with pdflatex without encountering encoding errors.

---

## Overview

DeclareUnicodeCharacter is a specialized LaTeX package designed to solve the common problem of using Unicode characters in pdflatex documents. Unlike other solutions that require replacing characters with LaTeX commands or using alternative engines like XeLaTeX or LuaLaTeX, this package allows direct usage of Unicode characters while maintaining compatibility with the traditional pdflatex workflow.

The package provides declarations for over 500 Unicode characters, including Greek letters, mathematical symbols, and special punctuation, making it especially valuable for academic and scientific documents where these characters are frequently used.

## Problem Solved

When you try to use unicode characters in LaTeX documents processed with pdflatex, you often encounter errors like:

```
! LaTeX Error: Unicode character β (U+03B2)
              not set up for use with LaTeX.
```

This package allows you to use these characters directly in your document.

## Installation

Place the `DeclareUnicodeCharacter.sty` file in one of the following locations:
- In the same directory as your LaTeX document (easiest)
- In your local texmf directory for system-wide installation:
  - Linux/macOS: `~/texmf/tex/latex/`
  - Windows: `C:\Users\<username>\texmf\tex\latex\`
  
After placing in your texmf directory, you may need to run `texhash` or `mktexlsr` to update the TeX database. You can test with `$ kpsewhich DeclareUnicodeCharacter.sty` which should output the actual path.

## Usage

1. Add the package to your LaTeX preamble:

```tex
\usepackage{DeclareUnicodeCharacter}
```

2. Use unicode characters directly in your document:

```tex
\documentclass{article}
\usepackage{DeclareUnicodeCharacter}

\begin{document}
β and other unicode/utf8 characters like α, δ, π can be used directly.
\end{document}
```

## Supported Characters

The package supports a wide range of unicode characters including:
- Greek letters (α, β, γ, δ, etc.)
- Mathematical symbols (∑, ∫, ∞, etc.)
- Special punctuation (—, –, ', etc.)
- Various other symbols (©, ®, ™, etc.)

See the complete list in `successful-chars.pdf`.

## Compatibility Notes

- Compatible with pdflatex
- Not compatible with luatex
- The package was created by extracting commands from `/usr/share/texmf/tex/texinfo/texinfo.tex`
- See the test file `successful-chars.pdf` which demonstrates 550+ successfully compiled characters
- The repository includes `extract-test-file.py` containing utility test functions

## Contributing

Contributions are welcome! Here's how you can help:

1. Report bugs and request features through issues
2. Submit pull requests with improvements
3. Help add support for more unicode characters
4. Improve documentation

Please follow the existing code style and add tests for new features.

## License

MIT
