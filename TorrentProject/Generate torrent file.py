import hashlib

if __name__ == '__main__':
    tracker = raw_input('enter file tracker URL: ')
    fileToSend = r'../test files/testFile.txt' #raw_input('enter the path of the file you want to conovert to torrent file: ')
    try:
        pieceLen = int(raw_input('ender piece len: '))
    except:
        pieceLen = 8

    name = fileToSend.split('/')[-1]
    torrentPath = r'../torrents/'

    with open(fileToSend, 'r') as f:
        fData = f.read()
        legnth = len(fData)
        pieces = []
        for i in xrange(0, len(fData), pieceLen):
            p = fData[i: i + pieceLen]
            #print ':' + repr(p) + ':'
            h = hashlib.sha224()
            h.update(p)
            pieces.append(h.hexdigest())
            #print pieces[-1]
    with open(torrentPath + 'torrent_' + name, 'w') as torrent:
        data = ''
        data += (tracker + '\n')
        data += (str(legnth) + '\n')
        data += (name + '\n')
        data += (str(pieceLen) + '\n')
        for h in pieces:
            data += (h + '\n')
        print data 
        torrent.write(data)
            
