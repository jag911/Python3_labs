filename = "./labs/messier.txt"
for line in open(filename, encoding='latin_1'):
        if not line: break
        if line[0] == "M":
            #print(line,end="")
            MessierNumber = line[:6].rstrip()
            CommonName = "no name" if not line[6:40].lstrip().rstrip() else line[6:40].lstrip().rstrip()
            ObjectType = line[40:64].rstrip()
            Constellation = line[64:].rstrip()
            print(f"|{MessierNumber}|{CommonName}|{ObjectType}|{Constellation}|")
            