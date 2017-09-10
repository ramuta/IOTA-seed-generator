import secrets
import string

print(''.join(secrets.choice(string.ascii_uppercase + "9") for _ in range(81)))
