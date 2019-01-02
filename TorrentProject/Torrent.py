class Torrent:
    # URL to tracker
    tracker = '' 

    # Legnth of the file in bytes
    legnth = 0

    # Suggested name for the file
    name = ''

    # number of bytes per piece.
    pieceLength = 0

    # a hash list, i.e., a concatenation of each piece's SHA-1 hash.
    pieces = [] 

    def __init__(self, tracker):
            self.tracker = tracker
            

    def __init__(self, torrentFile):
        with open(torrentFile, 'r') as file:
            data = file.readlines()
            tracker = data[0]
            legnth = data[1]
            name = data[2]
            pieceLength = data[3]
            pieces = data[4:]


