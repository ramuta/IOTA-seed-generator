import random
import string

print ''.join(random.choice(string.ascii_uppercase + "9") for _ in range(81))
