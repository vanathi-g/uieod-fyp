import json
import os

file = open("instances_train.json")
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

temp = [i for i in range(1,6672)]
for id in images:
	if id in temp:
		temp.remove(id)
print(len(temp))
for i in temp:
	os.remove(str(i)+".jpg")