import re

class Gift:
    def __init__(self, string):
        self.string = string
    
    def parse(self):
        patterns = [
            r"I just received a gift from ",
            r" via Throne Gifts: "
        ]
        out = self.string
        for i in patterns:
            out = out.replace(i, "()")
        out = out.split(" Thank you! ")[0]
        li = out[1:].split("()")
        l = []
        for item in li:
            if item.startswith(" ") or item.startswith(")"):
                item = item[1:]
            if item.endswith(" "):
                item = item[:-1]
            if item != "":
                l.append(item)
        return {"giftedFrom": l[0], "giftName": l[1]}

test = "I just received a gift from Mistah_Mace via Throne Gifts: Gaming Mouse Pad, Canjoy Extended Mouse Pad, 31.5x15.7inch XXL Large Big Computer Keyboard Mouse Mat Desk Pad with Non-Slip Base and Stitched Edge for Home. Thank you! https://thrn.co/u/miilkywayz #Wishlist #Throne"

def isGift(tweet):
    patterns = [
        "I just received a gift from",
        "via Throne Gifts:",
        "#Wishlist",
        "#Throne"
    ]
    matches = 0
    for i in patterns:
        if tweet.find(i) != -1:
            matches += 1
    if matches > 2:
        return True
    else:
        return False

if isGift(test):
    g = Gift(test)
    print(g.parse())