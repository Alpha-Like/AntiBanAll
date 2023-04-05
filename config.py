from os import getenv as g

API_ID = int(g("API_ID", None))
API_HASH = g("API_HASH", "")

BOT_TOKEN = g("BOT_TOKEN", "")

GROUP_IDS = g("GROUP_IDS", "").split() # example : "-123 -566"
SUDO_USERS = g("SUDO_USERS", "").split() # example : "12578627 74992683"

# DONT EDIT CODE BELOW !

ADMINS = []
GROUPS = []

for x in ADMIN_IDS:
    ADMINS.append(int(x))

for y in GROUP_IDS:
    GROUPS.append(int(y))
