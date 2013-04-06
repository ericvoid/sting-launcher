import os



def readConfig(path):
    with open(os.path.expanduser(path), 'r') as f:
        for line in _meaningfulLines(f):
                
            key, value = line.split('=', 1)
            yield key.strip(), value.strip()


def _meaningfulLines(f):
    for line in f:
        line = line.strip()

        if not line:
            continue
            
        if line.startswith('#'):
            continue

        yield line



def filter(search_text, items):
    for name, command in items:
        match_item = match(search_text, name)
        
        if not match_item:
            continue

        match_item.command = command

        yield match_item


def match(search_text, item_text):
    is_match, distance, matching_idx = _match(search_text, item_text, list())

    if not is_match:
        return None

    m = MatchItem()
    m.distance = distance
    m.matching_idx = matching_idx
    m.search_text = search_text
    m.name = item_text

    return m


def _match(search_text, item_text, matching_idx, distance=0, walked=0):
    if not search_text:
        # search text depleted - item matches
        return True, distance, matching_idx
    
    if not item_text:
        # item text depleted - item does not match
        return False, -1, []

    i = item_text.find(search_text[0])
    
    if i < 0 :
        return False, -1, []
    
    matching_idx.append(walked + i)
    
    return _match(search_text[1:], item_text[i + 1:], matching_idx,
        distance + i, walked + i + 1)


class MatchItem:
    def __init__(self):
        self.distance = 0
        self.matching_idx = []
        self.search_text = ''
        self.name = ''
        self.command = ''


def ChnltoFloat(x):
    x = float(x)
    return x / 255.0

def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    res = [int(value[i:i+lv/3], 16) for i in range(0, lv, lv/3)]
    return tuple(map(ChnltoFloat, res))


def hex_to_rgba(value):
    value = value.lstrip('#')
    lv = len(value)
    res = [int(value[i:i+lv/4], 16) for i in range(0, lv, lv/4)]
    return tuple(map(ChnltoFloat, res))

