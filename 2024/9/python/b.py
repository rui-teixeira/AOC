class Block:
    i = 0
    def __init__(this, fid, s):
        this.fid = fid
        this.s = s
        this.i = Block.i
        Block.i += 1

    def __str__(this):
        return f"i: {this.i}, fid: {this.fid}, s: {this.s}"

class Disk:
    dmap = "" 
    raw  = [] 

    def __str__(this):
        raw = ''
        for b in this.raw:
            raw += str(b.fid) * b.s
        return f"""
{[str(b) for b in this.raw]}
        """
        return f"""
diskmap: {this.dmap}
raw: {[str(b) for b in this.raw]}
checksum: {this.checksum()}
        """

    def read(this, line):
        this.dmap = line.strip()

    def expand(this):
        raw = []
        file = True
        fid = 0
        for c in this.dmap:
            s = int(c)
            if file:
                if s > 0: 
                    raw.append(Block(fid, int(c)))
            else:
                if s > 0: 
                    raw.append(Block(None, int(c)))

            fid += 1 if file else 0
            file = not file
        return raw
                
    def checksum(this):
        val, i = 0, 0
        for b in this.raw:
            if b.fid:
                for j in range(i,i+b.s):
                    val += j * b.fid
            i += b.s
        return val

    def compress(this):
        i = len(this.raw)
        last_ei = 0
        while i >= 0:
            i -= 1
            b = this.raw[i]
            debug and print(this)
            draw = [ str(b.fid)*b.s if b.fid != None else '.'*b.s for b in this.raw ]
            show and print(''.join(draw), end='')
            
            
            if not b.fid:
                # found empty trash it
                debug and print("it was empty, ignore it")
                show and print(" - empty")
                continue

            debug and print("trying", i, b)

            if i < last_ei:
                break
            # find the 1st empty that fits
            ei, e = this.find_empty(i, b.s)
            last_ei = ei

            debug and print("empty", ei, e)

            if ei == -1:
                debug and print("no space for", b)
                show and print(f" ({i}) - skipped")
                continue

            # empty is equal
            if b.s == e.s:
                # swap the blocks over the block
                show and print(f" ({i}) - swapped")
                this.raw[ei].fid, this.raw[i].fid = this.raw[i].fid, this.raw[ei].fid
            elif b.s < e.s:
                # split the empty block
                this.split(ei, b.s)
                i += 1
                # swap the blocks over the block
                # this.raw[ei].fid = b.fid
                this.raw[ei].fid, this.raw[i].fid = this.raw[i].fid, this.raw[ei].fid
                # this.raw[ei].fid, this.raw[i].fid = this.raw[i].fid, this.raw[ei].fid
                show and print(f" ({i}) - fitted")
            else:
                raise Exception("can't happen")

    def find_empty(this, i_max, s):
        for i, b in enumerate(this.raw):
            if i >= i_max:
                break
            if b.fid == None and b.s >= s:
                return i, b
        return -1, {}

    def split(this, i, s):
        b = this.raw[i]
        debug and print(b)
        if b.s < s:
            raise Exception("Can't split, not enough blocks")
        new_blocks = []
        # make the new block
        new_blocks.append(Block(b.fid, s))
        # make the leftover
        if b.s > s:
            new_blocks.append(Block(b.fid, b.s-s))
        # extract the old block, add the new blocks
        for b in new_blocks:
            debug and print(b)
        this.raw = this.raw[:i] + new_blocks + this.raw[i+1:]


debug = True
debug = False
show = False
# with open("../tests.txt") as fp:
# with open("../test.txt") as fp:
with open("../input.txt") as fp:
    for line in fp:
        d = Disk()
        d.read(line)
        d.raw = d.expand()
        debug and print(d)
        d.compress()
        print(d.checksum())
    #d.read(fp)
    #d.expand()
    #d.defrag()
    #print(d.checksum())
    

    



