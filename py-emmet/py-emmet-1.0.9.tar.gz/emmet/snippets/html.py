snippets = {
	"a": "a[href]",
	"a:blank": "a[href='http://${0}' target='_blank' rel='noopener noreferrer']",
	"a:link": "a[href='http://${0}']",
	"a:mail": "a[href='mailto:${0}']",
	"a:tel": "a[href='tel:+${0}']",
	"abbr": "abbr[title]",
	"acr|acronym": "acronym[title]",
	"base": "base[href]/",
	"basefont": "basefont/",
	"br": "br/",
	"frame": "frame/",
	"hr": "hr/",
	"bdo": "bdo[dir]",
	"bdo:r": "bdo[dir=rtl]",
	"bdo:l": "bdo[dir=ltr]",
	"col": "col/",
	"link": "link[rel=stylesheet href]/",
	"link:css": "link[href='${1:style}.css']",
	"link:print": "link[href='${1:print}.css' media=print]",
	"link:favicon": "link[rel='shortcut icon' type=image/x-icon href='${1:favicon.ico}']",
	"link:mf|link:manifest": "link[rel='manifest' href='${1:manifest.json}']",
	"link:touch": "link[rel=apple-touch-icon href='${1:favicon.png}']",
	"link:rss": "link[rel=alternate type=application/rss+xml title=RSS href='${1:rss.xml}']",
	"link:atom": "link[rel=alternate type=application/atom+xml title=Atom href='${1:atom.xml}']",
	"link:im|link:import": "link[rel=import href='${1:component}.html']",
	"meta": "meta/",
	"meta:utf": "meta[http-equiv=Content-Type content='text/html;charset=UTF-8']",
	"meta:vp": "meta[name=viewport content='width=${1:device-width}, initial-scale=${2:1.0}']",
	"meta:compat": "meta[http-equiv=X-UA-Compatible content='${1:IE=7}']",
	"meta:edge": "meta:compat[content='${1:ie=edge}']",
	"meta:redirect": "meta[http-equiv=refresh content='0; url=${1:http://example.com}']",
	"meta:kw": "meta[name=keywords content]",
	"meta:desc": "meta[name=description content]",
	"style": "style",
	"script": "script",
	"script:src": "script[src]",
	"img": "img[src alt]/",
	"img:s|img:srcset": "img[srcset src alt]",
	"img:z|img:sizes": "img[sizes srcset src alt]",
	"picture": "picture",
	"src|source": "source/",
	"src:sc|source:src": "source[src type]",
	"src:s|source:srcset": "source[srcset]",
	"src:t|source:type": "source[srcset type='${1:image/}']",
	"src:z|source:sizes": "source[sizes srcset]",
	"src:m|source:media": "source[media='(${1:min-width: })' srcset]",
	"src:mt|source:media:type": "source:media[type='${2:image/}']",
	"src:mz|source:media:sizes": "source:media[sizes srcset]",
	"src:zt|source:sizes:type": "source[sizes srcset type='${1:image/}']",
	"iframe": "iframe[src frameborder=0]",
	"embed": "embed[src type]/",
	"object": "object[data type]",
	"param": "param[name value]/",
	"map": "map[name]",
	"area": "area[shape coords href alt]/",
	"area:d": "area[shape=default]",
	"area:c": "area[shape=circle]",
	"area:r": "area[shape=rect]",
	"area:p": "area[shape=poly]",
	"form": "form[action]",
	"form:get": "form[method=get]",
	"form:post": "form[method=post]",
	"label": "label[for]",
	"input": "input[type=${1:text}]/",
	"inp": "input[name=${1} id=${1}]",
	"input:h|input:hidden": "input[type=hidden name]",
	"input:t|input:text": "inp[type=text]",
	"input:search": "inp[type=search]",
	"input:email": "inp[type=email]",
	"input:url": "inp[type=url]",
	"input:p|input:password": "inp[type=password]",
	"input:datetime": "inp[type=datetime]",
	"input:date": "inp[type=date]",
	"input:datetime-local": "inp[type=datetime-local]",
	"input:month": "inp[type=month]",
	"input:week": "inp[type=week]",
	"input:time": "inp[type=time]",
	"input:tel": "inp[type=tel]",
	"input:number": "inp[type=number]",
	"input:color": "inp[type=color]",
	"input:c|input:checkbox": "inp[type=checkbox]",
	"input:r|input:radio": "inp[type=radio]",
	"input:range": "inp[type=range]",
	"input:f|input:file": "inp[type=file]",
	"input:s|input:submit": "input[type=submit value]",
	"input:i|input:image": "input[type=image src alt]",
	"input:b|input:button": "input[type=button value]",
	"input:reset": "input:button[type=reset]",
	"isindex": "isindex/",
	"select": "select[name=${1} id=${1}]",
	"select:d|select:disabled": "select[disabled.]",
	"opt|option": "option[value]",
	"textarea": "textarea[name=${1} id=${1} cols=${2:30} rows=${3:10}]",
	"marquee": "marquee[behavior direction]",
	"menu:c|menu:context": "menu[type=context]",
	"menu:t|menu:toolbar": "menu[type=toolbar]",
	"video": "video[src]",
	"audio": "audio[src]",
	"html:xml": "html[xmlns=http://www.w3.org/1999/xhtml]",
	"keygen": "keygen/",
	"command": "command/",
	"btn:s|button:s|button:submit" : "button[type=submit]",
	"btn:r|button:r|button:reset" : "button[type=reset]",
	"btn:d|button:d|button:disabled" : "button[disabled.]",
	"fst:d|fset:d|fieldset:d|fieldset:disabled" : "fieldset[disabled.]",

	"bq": "blockquote",
	"fig": "figure",
	"figc": "figcaption",
	"pic": "picture",
	"ifr": "iframe",
	"emb": "embed",
	"obj": "object",
	"cap": "caption",
	"colg": "colgroup",
	"fst": "fieldset",
	"btn": "button",
	"optg": "optgroup",
	"tarea": "textarea",
	"leg": "legend",
	"sect": "section",
	"art": "article",
	"hdr": "header",
	"ftr": "footer",
	"adr": "address",
	"dlg": "dialog",
	"str": "strong",
	"prog": "progress",
	"mn": "main",
	"tem": "template",
	"fset": "fieldset",
	"datag": "datagrid",
	"datal": "datalist",
	"kg": "keygen",
	"out": "output",
	"det": "details",
	"sum": "summary",
	"cmd": "command",

	"ri:d|ri:dpr": "img:s",
	"ri:v|ri:viewport": "img:z",
	"ri:a|ri:art": "pic>src:m+img",
	"ri:t|ri:type": "pic>src:t+img",

	"!!!": "{<!DOCTYPE html>}",
	"doc": "html[lang=${lang}]>(head>meta[charset=${charset}]+meta:vp+title{${1:Document}})+body",
	"!|html:5": "!!!+doc",

	"c": "{<!-- ${0} -->}",
	"cc:ie": "{<!--[if IE]>${0}<![endif]-->}",
	"cc:noie": "{<!--[if !IE]><!-->${0}<!--<![endif]-->}"
}
