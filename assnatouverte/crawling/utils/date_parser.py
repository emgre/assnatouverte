import re
from typing import Optional

from datetime import date


MONTH_STR_TO_INT_DICT = {
    'janvier': 1,
    'février': 2,
    'mars': 3,
    'avril': 4,
    'mai': 5,
    'juin': 6,
    'juillet': 7,
    'août': 8,
    'septembre': 9,
    'octobre': 10,
    'novembre': 11,
    'décembre': 12
}


def parse_date(string: str) -> Optional[date]:
    string = string.strip().lower()
    match = re.search(r'(\d{1,2})(er)?\s+(\w+)\s+(\d{4})', string)
    if match:
        day = int(match.group(1))
        month_str = match.group(3)
        year = int(match.group(4))

        month = MONTH_STR_TO_INT_DICT.get(month_str)
        if month:
            return date(year, month, day)

    return None
