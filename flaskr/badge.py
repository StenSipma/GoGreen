import os
from random import randint

images = {
    80: 'im-6-small-2.png',
    60: 'im-8-small-2.png',
    40: 'im-4-small-2.png',
    20: 'im-7-small-2.png',
    0:  'im-3-small-2.png',
}

badges = [
    'im-1-small-2.png',
    'im-2-small-2.png',
    'im-5-small-2.png'
]

base_path = 'images/badges'


def get_badge_by_rank(score):
    if score > 80:
        return os.path.join(base_path, images[80])
    if score > 60:
        return os.path.join(base_path, images[60])
    if score > 40:
        return os.path.join(base_path, images[40])
    if score > 20:
        return os.path.join(base_path, images[20])
    return os.path.join(base_path, images[0])

def randomize_other_badges(num):
    return [(randint(0, num-1), os.path.join(base_path, badge)) for badge in badges]
