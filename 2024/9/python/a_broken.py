
class Disk:
    dmap = "" 
    raw  = ""

    def __str__(this):
        return f"""
diskmap: {this.dmap}
raw: {"".join(this.raw)}
checksum: {this.checksum()}
        """

    def read(this, line):
        this.dmap = line.strip()

    def expand(this):
        raw = ""
        file = True
        fileId = 0
        for c in this.dmap:
            s = str(fileId) if file else '.' 
            # print('s', s)
            # print('c', c)
            # print('raw:',raw)
            raw += s * int(c)

            fileId += 1 if file else 0
            file = not file

        return raw
                
    def checksum(this):
        val = 0
        for i, c in enumerate(this.raw):
            if c == '.':
                continue
            val += i*int(c)
        return val

    def compress(this):
        spaces = 0
        reverse_copy = []
        raw = []
        for c in this.raw[::-1]:
            if c == '.':
                spaces += 1
            else:
                reverse_copy.append(c)

        i = 0
        end = len(reverse_copy)
        for c in this.raw:
            # print('found',c)
            if i >= end:
                # print('already copied' ,i, 'of', end)
                break
            if c != '.':
                # print('copy', c)
                raw.append(c)
            elif c == '.':
                d = reverse_copy[i] 
                # print('copy', d)
                raw.append(d)
                i += 1


        return(''.join(raw[:len(this.raw)-spaces])+'.'*spaces)




debug = True
with open("../input.txt") as fp:
# with open("../tests.txt") as fp:
    for line in fp:
        d = Disk()
        d.read(line)
        print(d)
        d.raw = d.expand()
        print(d)
        d.raw = d.compress()
        print(d)
    #d.read(fp)
    #d.expand()
    #d.defrag()
    #print(d.checksum())
    

    



