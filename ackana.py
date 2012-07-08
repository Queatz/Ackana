import re

_pattern = re.compile("(\()?([a-z]*\:\/\/)?([-@\.\w]+\.[a-z|0-9]{1,4}[-~;:,@$%+!*'=#\/\?&\(\)\.\w]*)", flags = re.I)
_sep = re.compile('[;,\.]')

def ackana(string, target = '_blank'):
	"Parse links in a string."
	return re.sub(_pattern, lambda m: (
		(m.group(1) if m.group(1) else '') +
		'<a href="' + (m.group(2) if m.group(2) else 'http://') +
		(m.group(3)[:-1] if (
			m.group(1) and
			m.group(3) and
			m.group(3)[-1] == ')' or
			m.group(3) and
			re.match(_sep, m.group(3)[-1])
		) else (m.group(3) if m.group(3) else '')) +
		'" target="' + target + '">' +
		(m.group(2) if m.group(2) else '') +
		(m.group(3)[:-1] if (
			m.group(1) and
			m.group(3) and
			m.group(3)[-1] == ')' or
			m.group(3) and re.match(_sep, m.group(3)[-1])
		) else (m.group(3) if m.group(3) else '')) +
		'</a>' +
		(')' if m.group(1) and m.group(3) and m.group(3)[-1] == ')' else '') +
		(m.group(3)[-1] if m.group(3) and re.match(_sep, m.group(3)[-1]) else '')
	), string)
