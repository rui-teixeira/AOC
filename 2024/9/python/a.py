class Block:
    def __init__(this, file_id, size):
        this.file_id = file_id
        this.size = size

    def __str__(this):
        return f"fid: {this.file_id}, s: {this.size}"

class Disk:
    dmap = "" 
    raw  = [] 

    def __str__(this):
        raw = ''
        for b in this.raw:
            raw += str(b.file_id) * b.size
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
        file_id = 0
        for c in this.dmap:
            s = int(c)
            if file:
                if s > 0: 
                    raw.append(Block(file_id, int(c)))
            else:
                if s > 0: 
                    raw.append(Block(None, int(c)))

            file_id += 1 if file else 0
            file = not file
        return raw
                
    def checksum(this):
        val, i = 0, 0
        for b in this.raw:
            if b.file_id:
                for j in range(i,i+b.size):
                    val += j * b.file_id
            i += b.size
        return val

    def compress(this):
        i = 0
        finished = False
        while not finished:
            debug and print(this)
            b = this.raw.pop()
            debug and print("poped", b)
            if not b.file_id:
                debug and print("it was empty, trash it")
                # found empty trash it
                continue
            # if not empty, find room for it
            debug and print("allocating", b)
            while b.size > 0:
                if b.size < 0:
                    raise Exception("Allocation failed")
                # find the 1st empty
                i, e = this.find_empty(i)
                debug and print("empty", i, e)

                # no more empty spaces
                if i == -1:
                    # no more empty, done
                    debug and print("finished")
                    this.raw.append(b)
                    finished = True
                    break

                # empty is smaller/equal
                if b.size >= e.size:
                    # take over the block
                    this.raw[i].file_id = b.file_id
                    b.size -= e.size
                # empty was bigger
                else:
                    # split the empty block
                    this.split(i, b.size)
                    # take over the block
                    this.raw[i].file_id = b.file_id
                    b.size -= e.size

    def find_empty(this, i):
        for i in range(i, len(this.raw)):
            if this.raw[i].file_id == None:
                return i, this.raw[i]
        return -1, {}

    def split(this, i, s):
        b = this.raw[i]
        if b.size < s:
            raise Exception("Can't split, not enough blocks")
        new_blocks = []
        # make the new block
        new_blocks.append(Block(b.file_id, s))
        # make the leftover
        if b.size > s:
            new_blocks.append(Block(b.file_id, b.size-s))
        # extract the old block, add the new blocks
        this.raw = this.raw[:i] + new_blocks + this.raw[i+1:]


debug = True
debug = False
# with open("../tests.txt") as fp:
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
    

    



