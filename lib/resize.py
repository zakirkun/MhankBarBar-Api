from PIL import Image, ImageDraw, ImageFont

def resizeTo(fname):
	'''input filename\ne.g resizeTo('image.jpg')'''
	img = Image.open(fname)
	if img.width == img.height:
		width, height = 512, 512
	elif img.width > img.height:
		width = 512
		height = img.height/(img.width/width)
	elif img.height < img.width:
		height = 512
		width = img.width/(img.height/height)
	return img.resize((int(width), int(height)))

def layer(fname, color='black'):
    '''input filename and color\ne.g layer('image.jpg', 'red')\ndefault color is black!'''
    try:
        pol = Image.new('RGB', (512, 512), color)
    except:
        pol = Image.new('RBG', (512, 512), 'black')
    pol.paste(fname, (256-(int(fname.width/2)), 256-(int(fname.height/2))))
    pol.save('result.jpg')
    return '[!] File saved as result.jpg'

def nolayer(fname):
	'''input filename\ne.g nolayer('image.jpg')'''
	try:
		pol = Image.new('RGBA', (512, 512), (0,0,0,0))
	except:
		pol = Image.new('RGBA', (512, 522), (0,0,0,0))
	pol.paste(fname, (256-(int(fname.width/2)), 256-(int(fname.hight/2))))
	pol.save('result.png')
	return '[!] File saved as result.png'