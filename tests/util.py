import re

def gbnf_to_lark(text: str) -> str:
    """Rough conversion from llama.cpp GBNF to Lark grammar."""
    def fix_regex(segment: str) -> str:
        def repl(match):
            inner = match.group(1)
            quant = match.group(2) or ''
            return f"/[{inner}]{quant}/"
        return re.sub(r"\[([^\]]+)\](\{\d+,?\d*\})?", repl, segment)

    lines = []
    for line in text.splitlines():
        if '::=' not in line:
            lines.append(line)
            continue
        left, right = line.split('::=', 1)
        left = left.strip()
        right = fix_regex(right.strip())
        if left == 'root':
            left = 'start'
        lines.append(f"{left}: {right}")
    return '\n'.join(lines)
