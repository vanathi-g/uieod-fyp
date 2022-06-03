import json
import os

file = open("instances_test.json")
instances = json.load(file)

images = {}

for i in instances['annotations']:
	if(i['image_id'] not in images):
		images[i['image_id']] = {i['category_id'] : [i['bbox']]}
	else:
		if i['category_id'] not in images[i['image_id']]:
			images[i['image_id']][i['category_id']] = [i['bbox']]
		else:
			images[i['image_id']][i['category_id']].append(i['bbox'])

size_file = open("test_sizes.txt","r")
sizes = size_file.read().split("\n")

for id in images:
	new_file = open(str(id)+".txt", "w")

	size = sizes[id-1].split(" ")
	width = float(size[2])
	height = float(size[1])

	for category_id in images[id]:
		for bbox in images[id][category_id]:
			l = bbox[2]
			h = bbox[3]

			cx = bbox[0]+l/2
			cy = bbox[1]+h/2

			cx/=width
			cy/=height

			l/=width
			h/=height

			line = str(category_id-1)+" "+str(cx)+" "+str(cy)+" "+str(l)+" "+str(h)+"\n"
			new_file.write(line)
	new_file.close()