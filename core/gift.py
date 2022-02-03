class Gift:
    def __init__(self, string):
        self.string = string
    
    def parse(self):
        patterns = [
            r"I just received a gift from ",
            r" via Throne Gifts: ",
            r" Thank you!… "
        ]
        out = self.string
        for i in patterns:
            out = out.replace(i, "()")
        try:
            out = out.split("")[0]
        except:
            pass
        li = out.split("()")
        l = []
        for item in li:
            if item.startswith(" ") or item.startswith(")"):
                item = item[1:]
            if item.endswith(" "):
                item = item[:-1]
            if item != "":
                l.append(item)
        return {"giftedFrom": l[0], "giftName": l[1], "media":l[2]}

def isGift(tweet):
    patterns = [
        "I just received a gift from",
        "via Throne Gifts:",
        " Thank you!… ",
    ]
    matches = 0
    for i in patterns:
        if tweet.find(i) != -1:
            matches += 1
    if matches > 2:
        return True
    else:
        return False

def getParse(tweet):
    if isGift(tweet):
        g = Gift(tweet)
        return g.parse()
    