from collections import defaultdict
from pprint import pprint

class Page:
    def __init__(self, order, status, score):
        self.order = order
        self.status = status
        self.score = score

    def __str__(self):
        return f"{self.status}: {self.order}"

with open("../input.txt") as fp:

    # The notation X|Y means that if both page number X and page number Y are to be produced as part of an update, page number X must be printed at some point before page number Y.
    
    # before[Y] = [X1,X2,X3]
    before = defaultdict(set)
    pages = []

    for line in fp:
        if "|" in line:
            (x,y) = (int(i) for i in line.split('|'))
            before[y].add(x)
        if "," in line:
            order = [int(i) for i in line.split(',')]
            pages.append(
                    Page(
                        order,
                        None,
                        order[len(order) // 2]
                        )
                    )

    for page in pages:
        printed = set()
        total = set(page.order)
        for n in page.order:
            required = before[n]
            should_be_printed = required & total
            if should_be_printed <= printed:
                page.status='OK'
            else:
                page.status='BAD'
                break
            printed.add(n)

    total = 0
    bad_pages = []
    for page in pages:
        if page.status == "OK":
            total += page.score if page.status == "OK" else 0
        else:
            bad_pages.append(page)
    
    print("PART 1: ok pages total", total)

    # FIX BAD PAGE ORDERS
    for i in range(len(bad_pages)):
        page = bad_pages[i]
        while page.status == 'BAD':
            printed = set()
            total = set(page.order)
            p_j = 0
            for j in range(p_j, len(page.order)):
                n = page.order[j]
                required = before[n]
                should_be_printed = required & total
                if should_be_printed <= printed:
                    page.status='OK'
                    printed.add(n)
                else:
                    # lets shove the bad page to the end of the oder and try again
                    page.status='BAD'
                    page.order.append(n)
                    del page.order[j]
                    # try again starting from the same place where we last stopped
                    p_j = j
                    break
        else:
            page.score = page.order[len(page.order) // 2]


    total = 0
    for page in bad_pages:
        if page.status == "OK":
            total += page.score if page.status == "OK" else 0

    print("PART 2: bad pages total", total)

