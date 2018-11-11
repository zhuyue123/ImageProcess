# coding=utf-8
from PIL import Image
size = 512
class Graphics:
    '''图片处理类

    参数: infile, outfile
    ------
    infile: 加载图片文件的路径
    outfile: 转存图片文件的路径
    '''

    def __init__(self, infile, outfile):
        self.infile = infile
        self.outfile = outfile

    def cut_by_ratio(self):

        im = Image.open(self.infile)
        (x, y) = im.size
        if(x>=y):
            p = Image.new('RGB', (x, x), (255, 255, 255))
            #p.paste(im, (0, (x-y)/2, x, (x+y)/2))
            b = int((x-y)/2)
            p.paste(im, (0, b))
            p.save(self.outfile)
        if(y>x):
            p = Image.new('RGB', (y, y), (255, 255, 255))
            a = int((y-x)/2)
            p.paste(im, (a, 0))
            p.save(self.outfile)

    def image_resize(self):
        im = Image.open(self.infile)
        im_resized = im.resize((size, size), Image.BILINEAR)
        im_resized.save(self.outfile)

    def image_rotate(self):
        im = Image.open(self.infile)
        out = im.transpose(Image.FLIP_LEFT_RIGHT)
        # out = im_resized.transpose(img.ROTATE_90)
        # out = im_resized.transpose(img.ROTATE_180)
        # out = im_resized.transpose(img.ROTATE_270)
        out.save(self.outfile)


