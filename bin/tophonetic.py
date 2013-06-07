#!/usr/bin/python

#Translates argv[] into NATO phonetics for proper and clean phone communications.
#Fred Dinkler IV


import os
import sys

phones={
'-':'Dash',
'.':'Period|(Full) Stop|Decimal (point)',
'?':'Question|Interrogation mark|Point',
'!':'Exclamation mark|Bang',
'@':'At symbol|Ampersat',
"#":'Number sign|Pound|Hash',
'$':'Dollar sign',
'%':'Percent sign',
'^':'Caret',
'&':'Ampersand',
'*':'Asterisk|Star|Splat',
'(':'Left paren|Left round brackets',
')':'Right paren|Right round brackets',
'-':'Hyphen|Minus',
'=':'Equals sign|Equality sign',
'_':'Underscore|Understrike|Underbar|Low line',
'+':'Plus sign',
'{':'Left curly bracket|Left brace',
'}':'Right curly bracket|Right brace',
'[':'Left square bracket|Left bracket',
']':'Right square bracket|Right bracket',
';':'Semicolon',
':':'Colon',
'\'':'Single quote|Apostrophe',
'"':'Double quote|Quotation marks',
'<':'Less-than (sign)',
'>':'Greater-than (sign)',
',':'Coma',
'/':'(forward) Slash|Stroke',
'|':'Vertical bar|Broken bar|Pipe|OR',
'\\':'Backslash|Backslant|Backslant',
'`':'Backtick|Backquote|Grave',
'~':'Tilde',
'0':'Zero|Naught|Nil',
'1':'Wun (One)',
'2':'Two',
'3':'Tree (Three)',
'4':'Fower (Four)',
'5':'Fife (Five)',
'6':'Six',
'7':'Seven',
'8':'Ait (Eight)',
'9':'Niner (Nine)',
'A':'Alpha',
'B':'Bravo',
'C':'Charlie',
'D':'Delta',
'E':'Echo',
'F':'Foxtrot',
'G':'Golf',
'H':'Hotel',
'I':'India',
'J':'Juliet',
'K':'Kilo',
'L':'Lima',
'M':'Mike',
'N':'November',
'O':'Oscar',
'P':'Papa',
'Q':'Quebec',
'R':'Romeo',
'S':'Sierra',
'T':'Tango',
'U':'Uniform',
'V':'Victor',
'W':'Whiskey',
'X':'X-ray',
'Y':'Yankee',
'Z':'Zulu'
}

del sys.argv[0]
for word in sys.argv:
	if len(sys.argv) > 1:
		print("\n\t" + word + "\n")
	for char in word:
		if str.isalpha(char):
			if str.islower(char):
				case=" lowercase "
			else:
				case=" CAPITAL   "
			let=str.upper(char)
			print(char + case + phones[let])
		else:
			case="           "
			try:
				print(char + case + phones[char])
			except:
				print(char)
