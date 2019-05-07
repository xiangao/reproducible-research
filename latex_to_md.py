#!/usr/bin/env python
import sys
import re


def clean(text):
    l = [
        (r'\{\\hilit ([^}]+)\}', lambda m: '**%s**' % m.group(1)),
        (r'\\href\{([^}]+)\}\{([^}]+)\}', lambda m: '[%s](%s)' % (m.group(2), m.group(1))),
    ]
    result = text
    for pattern, repl in l:
        result = re.sub(pattern, repl, result)
    return result


def test_clean():
    pairs = [
        (r'{\hilit Real}', '**Real**'),
        (r'\href{http://example.org}{example}', '[example](http://example.org)'),
    ]
    for in_text, out_text in pairs:
        assert clean(in_text) == out_text


if __name__ == "__main__":
    text = sys.stdin.read()
    cleaned = clean(text)
    sys.stdout.write(cleaned)
