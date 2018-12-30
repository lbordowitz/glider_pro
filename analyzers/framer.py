from PIL import Image, ImageChops
import json

'''
# Format of json info
[
	{
		"name":"imageName",
		"mask":"maskName",
		"crops":[
			{
				"name":"output_name",
				"x":x_offset,
				"y":y_offset,
				"w":width,
				"h":height
			},
			...
		]
	},
	...
]
'''

data = json.load(open('sprites.json'))

for smap in data:
    im_name = smap['name']
    mask_name = smap['mask']

    im = Image.open(im_name)
    mask = ImageChops.invert(Image.open(mask_name).convert('1'))
    frames = Image.new("RGBA",im.size,(255,0,0,0))
    frames.paste(im,(0,0,im.size[0],im.size[1]),mask)

    for out in smap['crops']:
        x = out['x']
        y = out['y']
        w = out['w']
        h = out['h']
        frames.crop((x,y,x+w,y+h)).save(out['name'], 'PNG')
