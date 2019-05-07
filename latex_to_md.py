#!/usr/bin/env python
import sys
import re


def clean(text):
    l = [
        (r'\\[hv]space\{[^}]+\}', ''),
        (r'\{\\hilit ([^}]+)\}', lambda m: '**%s**' % m.group(1)),
        (r'\\hilit', ''),
        (r'\{\\lolit ([^}]+)\}', lambda m: m.group(1)),
        (r'\{\\tt ([^}]+)\}', lambda m: '`%s`' % m.group(1)),
        (r'\{\\ttfn ([^}]+)\}', lambda m: '`%s`' % m.group(1)),
        (r'\\href\{([^}]+)\}\{([^}]+)\}', lambda m: '[%s](%s)' % (m.group(2), m.group(1))),
        (r'\\textasciitilde', '~'),
        (r'\\texttt{([^}]+)}', lambda m: '`%s`' % m.group(1)),
        (r'\{\\footnotesize \\lolit ([^}]+)\}', lambda m: m.group(1)),
        (r'\\(bbi|bi|ei)\b\s*', ''),
        (r'\\note\{([^}]+)\}', lambda m: m.group(1)),
        (r'\\end\{frame\}', ''),
        (r'\\begin\{frame\}[^{]*\{([^}]+)\}', lambda m: '## %s\n\n' % m.group(1)),
        (r'\\/', '/'),
        (r'\\emph{([^}]+)}', lambda m: '**%s**' % m.group(1)),
        (r'\\begin{lstlisting}', '```'),
        (r'\\end{lstlisting}', '```'),
        (r'\\bigskip', ''),
        (r'\\textbackslash', '/'),
        (r'\\begin{frame}{}', '- - - - -'),
        (r'\\end{document}', ''),
    ]
    result = text
    for pattern, repl in l:
        result = re.sub(pattern, repl, result, flags=re.MULTILINE)
    return result


def test_clean():
    pairs = [
        (r'{\hilit Real}', '**Real**'),
        (r'\href{http://example.org}{example}', '[example](http://example.org)'),
        (r'{\tt git status}', '`git status`'),
        (r'\textasciitilde', '~'),
        (r'\texttt{m}', '`m`'),
        (r'{\footnotesize \lolit hi}', 'hi'),
        (r'\hspace{1in}', ''),
        (r'\bbi', ''),
        ('\\note{hi\nthere}', 'hi\nthere'),
        (r'\begin{frame}[fragile]{hi}', '## hi\n\n'),
        (r'\/', '/'),
    ]
    for in_text, out_text in pairs:
        assert clean(in_text) == out_text


if __name__ == "__main__":
    text = sys.stdin.read()
    cleaned = clean(text)
    sys.stdout.write(cleaned)
