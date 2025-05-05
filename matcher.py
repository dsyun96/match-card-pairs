import numpy as np
import cv2


def match_cards(cards):
    matched = []

    s = []
    for i in range(len(cards)):
        for j in range(i + 1, len(cards)):
            diff = np.mean(cv2.absdiff(cards[i]['img'], cards[j]['img']))
            s.append((diff, i, j, cards[i]['pos'], cards[j]['pos']))

    used = set()
    for diff, i, j, i_center, j_center in sorted(s):
        if i in used or j in used: continue
        used.add(i)
        used.add(j)
        matched.append((i_center, j_center))

    return matched
