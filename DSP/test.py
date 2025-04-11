import re
import json

# Example line to test
test_line = "just gimme a call back."

# Example JSON profanity list
with open("en.json", "r") as profanity_file:
        profanity_list = json.load(profanity_file)

# Test each pattern
for entry in profanity_list:
    pattern = entry["match"]
    if re.search(pattern, test_line, re.IGNORECASE):
        print(f"Matched '{pattern}' with severity {entry['severity']}")