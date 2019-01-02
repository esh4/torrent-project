import socket
import thread
from threading import Thread
import Torrent

class Peer:
    def __init__(self):
        self.threads = []

        # thread.start_new_thread(self.waitForConnections, ())
        self.tWaitForConnections = Thread(target=self.waitForConnections)
        self.tWaitForConnections.start()
        self.threads.append(self.tWaitForConnections)

    def waitForConnections(self):
        # listen for multiple requests
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        port = 6881
        s.bind(('0.0.0.0', port))
        s.listen(1)
        while True:
            print 'Wainting for connections'
            client_socket, addr = s.accept()
            print 'connected to' + addr
            # thread.start_new_thread(handleRequest, (client_socket,))
            conn = Thread(target=self.handleRequest, args=(client_socket))
            conn.start()
            self.threads.append(conn) 
        
    def handleRequest(self, socket):
        torrent = Torrent.Torrent(socket.recv(1024))
        
        #check we have the file
        f = open(torrent.name, 'r').read()
        splitFile = []
        for i in xrange(0, len(f), torrent.pieceLength):
            splitFile.append(f[i: i + pieceLen])

        chunk_index = socket.recv(1024)
        while chunk_index != 'kill':
            chunk_index = socket.recv(1024)
            socket.send(splitFile[chunk_index])

    def requestPeers():
        pass


    def searchForFile(fileName):
        """
        search through all the servers for a certain file.
        """
        pass

    # suggestion: if more servers connect during the transfer, restart the process and refragment what remains
    def requestTorrentFile(self, torrentFile):
        torrent = Torrent.Torrent(torrentFile)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print 'trying to connect'
        s.connect(('S11', 6881))
        print 'Connected'
        s.send(open(torrentFile, 'r').read())
        data = {}
        for i in xrange(torrent.pieces):
            s.send(torrent.pieces[i])
            data[i] = s.recv(torrent.pieceLength)
        s.send('kill')
        print data

    def requestFragment():
        pass

