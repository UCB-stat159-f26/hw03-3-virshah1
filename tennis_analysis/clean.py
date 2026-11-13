import json
import re


def parse_matches(js_text):
    """Extract match records from Tennis Abstract JavaScript."""
    match = re.search(
        r"var\s+morematchmx\s*=\s*(\[[\s\S]*?\]);",
        js_text
    )

    if not match:
        raise ValueError("Could not find match data in the JS file.")

    return json.loads(match.group(1))
