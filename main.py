# imports
import json
import os.path
import shutil

# user settings
src = [
    ('C:\\Users\\User\\Downloads\\our_car\\mycar\\tub_1_no_obs', [(10, 20), (30, 40)]),
    ('C:\\Users\\User\\Downloads\\our_car\\mycar\\tub_2_obs', [(10, 20), (30, 40)]),
]
dst = 'C:\\Users\\User\\Downloads\\our_car\\mycar\\tub_1_post'

# make dst dir
if not os.path.exists(dst):
    os.mkdir(dst)

# make target list
targets = []
for dir_target in src:
    target_indexes = []
    for target_range in dir_target[1]:
        target_indexes += range(target_range[0], target_range[1])
    targets += [(dir_target[0], target_index) for target_index in target_indexes]

# fill dst
for enumeration, (path, index) in enumerate(targets):
    # read metadata
    with open(os.path.join(path, 'record_' + str(index)+'.json'), 'r') as file:
        metadata = json.load(file)

    # edit metadata
    metadata['cam/image_array'] = str(enumeration+1) + '_cam-image_array_.jpg'

    # write metadata to dst
    with open(os.path.join(dst, 'record_' + str(enumeration + 1) + '.json'), 'w') as file:
        json.dump(metadata, file)

    # move image file with enumerated name
    shutil.copy(
        os.path.join(path, str(index) + '_cam-image_array_.jpg'),
        os.path.join(dst, str(enumeration + 1) + '_cam-image_array_.jpg'))
