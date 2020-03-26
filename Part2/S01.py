>>> import re
>>> rexp = re.compile('^cat')
>>> m = rexp.search('I see a cat')
>>> print(m)
None
>>> m = rexp.search('category')
>>> print(m)
<_sre.SRE_Match object; span=(0, 3), match='cat'>
>>> print(m.group(0))
cat
>>>
