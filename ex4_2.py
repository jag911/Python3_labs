filename = r"./labs/messier.txt"
no_name = "no name"
for line in open(filename, encoding='latin_1'):
        if not line: break
        if line[0] == "M":
            MessierNumber = line[:6].rstrip()
            CommonName = line[6:40].lstrip().rstrip()
            ObjectType = line[40:64].rstrip()
            Constellation = line[64:].rstrip()
            print(f"|{MessierNumber}|{no_name if not CommonName else CommonName}|{ObjectType}|{Constellation}|")
            