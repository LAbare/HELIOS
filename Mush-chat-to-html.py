n = input("Nom du fichier : ")
f = open(n + '.txt', 'r')
dest = open(n + '.html', 'w')

def smileySource(string):
	return string.replace('src="//', 'src="http://').replace('src="http://data.twinoid.com/img/smile', 'src="smile').replace('src="/img', 'src="http://mush.vg/img')

ismainmessage = True
mainmessages = []
replies = []
i = -1

for line in f:
    if 'mainmessage' in line:
        ismainmessage = True
        mainmessages.append('')
        replies.append([])
        i += 1
        j = 0
    if 'class="reply bubble' in line:
        ismainmessage = False
        replies[i].append('')
    if 'class="char' in line or 'class="neron' in line:
        if ismainmessage:
            mainmessages[i] += smileySource(line.strip('\n'))
        else:
            replies[i][j] += smileySource(line.strip('\n'))
    if 'class="buddy' in line:
        if ismainmessage:
            mainmessages[i] += smileySource(line.strip('\n'))
        else:
            replies[i][j] += smileySource(line.strip('\n'))
            j += 1

dest.write("<html>\n<head>\n\t<title>" + input("Nom de la partie : ") + " — Partie HELIOS</title>\n")
dest.write("\t<style>\n" +
"		#wall { max-width: 800px; margin: 0 auto; }\n" +
"		.hiddenreplies { display: none; }\n" +
"		.mainmessage { border-radius: 8px; border: 2px #000440 solid; padding: 10px; margin-top: 20px; min-height: 48px; position: relative; }\n" +
"		.reply { margin-left: 50px; border-radius: 5px; border: 2px navy solid; padding: 10px; margin-top: 10px; }\n" +
"		.show { text-align: right; color: green; cursor: pointer; }\n" +
"		.link { position: absolute; bottom: 10px; right: 10px; }\n" +
"		em { color: #F03; }\n" +
"		strong { color: #30F; }\n" +
"		.char { background: url('img/char.png'); background-repeat: no-repeat; width: 28px; height: 48px; resize: none; float: left; }\n" +
"		.reply .char { height: 16px; }\n" +
"		.buddy { font-variant: small-caps; color: blue; float: left; margin-right: 5px; }\n" +
"		p { margin: 0 5px; word-wrap: break-word; }\n" +
"		.janice { background-position: 0px -144px !important; }\n" +
"		.frieda { background-position: 0px -48px !important; }\n" +
"		.paola { background-position: 0px -288px !important; }\n" +
"		.gioele { background-position: 0px -624px !important; }\n" +
"		.jin_su { background-position: 0px 0px !important; }\n" +
"		.kuan_ti { background-position: 0px -96px !important; }\n" +
"		.chun { background-position: 0px -528px !important; }\n" +
"		.chao { background-position: 0px -336px !important; }\n" +
"		.hua { background-position: 0px -240px !important; }\n" +
"		.roland { background-position: 0px -192px !important; }\n" +
"		.derek { background-position: -2px -1776px !important; }\n" +
"		.andie { background-position: -2px -1824px !important; }\n" +
"		.stephen { background-position: 0px -432px !important; }\n" +
"		.ian { background-position: 0px -480px !important; }\n" +
"		.raluca { background-position: 0px -576px !important; }\n" +
"		.finola { background-position: 0px -384px !important; }\n" +
"		.terrence { background-position: 0px -720px !important; }\n" +
"		.eleesha { background-position: 0px -672px !important; }\n" +
"		.mainmessage .neron { background-image : url('img/neron_chat.png'); float: left; margin-right: 5px; height: 38px; width: 38px; }\n" +
"		.reply .neron { float: left; margin-right: 5px; }\n" +
"	</style>\n" +
"	<meta charset='UTF-8' />\n" +
"</head>\n\n" +
"<body>\n" +
"<div id='wall'>\n\n" +
"<script>\n" +
"function show(el) {\n" +
"	var repliesblock = el.nextElementSibling;\n" +
"	if (repliesblock.className == 'hiddenreplies')\n" +
"		{ el.textContent = 'Cacher les réponses'; repliesblock.className = 'shownreplies'; }\n" +
"	else\n" +
"		{ el.textContent = 'Montrer les réponses'; repliesblock.className = 'hiddenreplies'; }\n" +
"}</script>\n\n")

for k in range(0, len(mainmessages)):
    dest.write('<div class="mainmessage" id="' + str(k) + '"> ' + mainmessages[k] + '<a class="link" href="#' + str(k) + '">Ancre</a> </div>\n\n')
    if replies[k]:
        dest.write('<div class="show" onclick="show(this);">Montrer les réponses</div>\n<div class="hiddenreplies">\n')
        for l in range(0, len(replies[k])):
            dest.write('<div class="reply"> ' + replies[k][l] + ' </div>\n')
        dest.write('</div>\n\n')

dest.write('\n\n\n</div>\n</body>\n</html>')
f.close()
dest.close()