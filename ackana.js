String.prototype.ackana = function() {
	return this.replace(/(\()?([a-z]*\:\/\/)?([-@\.\w]+\.[a-z|0-9]{1,4}[-~;:,@$%+!*'=#\/\?&\(\)\.\w]*)/gi, function helper(str, $1, $2, $3) {if(typeof $1=='undefined')$1='';if(typeof $2=='undefined')$2='';return $1+'<a href="'+($2?$2:'http://')+($1&&$3.substr(-1)==')'||($3.substr(-1).match(/[;,\.]/g))?$3.substr(0, $3.length-1):$3)+'" target="_blank">' +$2+($1&&$3.substr(-1)==')'||($3.substr(-1).match(/[;,\.]/g))?$3.substr(0, $3.length-1):$3)+'</a>'+($1&&$3.substr(-1)==')'?')':'')+($3.substr(-1).match(/[;,\.]/g)?$3.substr(-1):'');});
}
