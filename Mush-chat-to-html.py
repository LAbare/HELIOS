f = open('Chat.txt', 'r')
dest = open('Chat.html', 'w')

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
    if 'class="reply bubble"' in line:
        ismainmessage = False
        replies[i].append('')
    if 'class="char' in line or 'class="neron"' in line:
        if ismainmessage:
            mainmessages[i] += line.strip('\n').replace('src="//', 'src="http://').replace('src="/img', 'src="http://mush.vg/img')
        else:
            replies[i][j] += line.strip('\n').replace('src="//', 'src="http://').replace('src="/img', 'src="http://mush.vg/img')
    if 'class="buddy' in line:
        if ismainmessage:
            mainmessages[i] += line.strip('\n').replace('src="//', 'src="http://').replace('src="/img', 'src="http://mush.vg/img')
        else:
            replies[i][j] += line.strip('\n').replace('src="//', 'src="http://').replace('src="/img', 'src="http://mush.vg/img')
            j += 1

dest.write('<html>\n<head>\n    <title>HELIOS</title>\n    <style></style>\n    <meta charset="UTF-8" />\n</head>\n\n<body>\n<div id="wall">\n\n\n')

for k in range(0, len(mainmessages)):
    dest.write('<div class="mainmessage"> ' + mainmessages[k] + ' </div>\n\n')
    if replies[k]:
        dest.write('<div class="show" onclick="show(this);">Montrer les réponses</div>\n<div class="hiddenreplies">\n')
        for l in range(0, len(replies[k])):
            dest.write('<div class="reply"> ' + replies[k][l] + ' </div>\n')
        dest.write('</div>\n\n')

dest.write('\n\n\n</div>\n</body>\n</html>')
f.close()
dest.close()
