import os

images = {
    80: 'im-6-small.png',
    60: 'im-8-small.png',
    40: 'im-4-small.png',
    20: 'im-7-small.png',
    0:  'im-3-small.png',
}

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
