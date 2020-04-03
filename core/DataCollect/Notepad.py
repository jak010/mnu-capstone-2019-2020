import psutil
from pprint import pprint
for x in psutil.process_iter():
    pprint(x.as_dict())

