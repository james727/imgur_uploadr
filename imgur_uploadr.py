"""
    Script to upload an image to imgur. Syntax is as follows:

        python imgur_uploadr.py X Y Z

    X, Y, and Z are the arguments for the script, defined as follows:

        X: the path of the image file you'd like to upload
        Y: the title of the image (optional)
        Z: the description of the image (optional)

    Before running this script you MUST install the imgur python API client,
    using the following command:

        pip install imgurpython        
"""

import sys
from imgurpython import ImgurClient
client_id = '82c51ca2f32f6d6'
client_secret = '077827772b09216439f16463a4fc84128ffd82f5'
client = ImgurClient(client_id, client_secret)

def upload_image(client, image_path, title, description):
	album = None
	# Here's the metadata for the upload. All of these are optional, including
	# this config dict itself.
	config = {
		'album': album,
		'name':  'Catastrophe!',
		'title': title,
		'description': description
	}

	print"Uploading image... "
	image = client.upload_from_path(image_path, config=config, anon=False)
	print "Done"
	print

	return image


args = sys.argv
path = args[1]
title = ""
description = ""
if len(args)>2:
    title = args[2]
    if len(args)>3:
        description = args[3]
image = upload_image(client, path, title, description)
print "Image was posted!"
print "You can find it here: {0}".format(image['link'])
