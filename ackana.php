<?php

function ackana($s) {
	return preg_replace("/(\()?([a-z]*\:\/\/)?([-@\.\w]+\.[a-z|0-9]{2,4}[-~;:,@$%+!*'=#\/\?&\(\)\.\w]*)/ei", "'$1<a href=\"'.('$2'?'$2':'http://').('$1'&&substr('$3',-1)==')'||preg_match('/[;,\.]/', substr('$3',-1))?substr('$3',0,-1):'$3').'\" target=\"_blank\">$2'.('$1'&&substr('$3',-1)==')'||preg_match('/[;,\.]/', substr('$3',-1))?substr('$3',0,-1):'$3').'</a>'.('$1'&&substr('$3',-1)==')'?')':'').(preg_match('/[%;,\.]/', substr('$3',-1))?substr('$3',-1):'')", $s);
}
