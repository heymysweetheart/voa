#!/usr/bin/env python

import re

v = """<p id=1>Sometimes, <b>simpler</b> is better,
but <i>not</i> always.</p>"""

result = re.sub("<.*?>", "", v)
print(result)

