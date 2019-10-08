import re
from typing import Optional, Tuple


def extract_member_id(url: str) -> Optional[str]:
    match = re.search(r'/([a-z0-9\-\(\)]+)(/index)?\.html', url)
    if match:
        return match.group(1)
    return None


def extract_parentheses(string: str) -> Tuple[str, Optional[str]]:
    paren_text = None
    match = re.search(r'\((.+)\)', string)
    if match:
        paren_text = match.group(1)
        string = re.sub(r'\(.+\)', '', string, count=1).strip()

    return string, paren_text
