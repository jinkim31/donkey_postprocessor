# imports
import json
import os.path
import shutil

# user settings
src_dir = 'C:\\Users\\User\\Downloads\\our_car\\mycar\\tub_1_no_obs'
dst_dir = 'C:\\Users\\User\\Downloads\\our_car\\mycar\\tub_1_post'
ranges = [[10, 20]]

# make dst dir
if not os.path.exists(dst_dir):
    os.mkdir(dst_dir)

# concat ranges
indexes = []
for i_range in ranges:
    indexes += range(i_range[0], i_range[1])

for enumeration, index in enumerate(indexes):
    # read metadata
    with open(os.path.join(src_dir, 'record_' + str(index)+'.json'), 'r') as file:
        metadata = json.load(file)

    # edit metadata
    metadata['cam/image_array'] = str(enumeration) + '_cam-image_array_.jpg'

    # write metadata to dst
    with open(os.path.join(dst_dir, 'record_' + str(enumeration)+'.json'), 'w') as file:
        json.dump(metadata, file)

    # move image file with enumerated name
    shutil.move(
        os.path.join(src_dir, str(index) + '_cam-image_array_.jpg'),
        os.path.join(dst_dir, str(enumeration) + '_cam-image_array_.jpg'))
