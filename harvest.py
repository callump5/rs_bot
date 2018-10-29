from img_matcher import *
from items import *

i = 0
p = 0

while i < 20:
    while p < len(treeimages):
        img_match(treeimages[p]['link'])
