import os
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, landscape


def get_file(path):
    files = os.listdir(u"%s" % path)
    files.sort(key=lambda x: int(x[:-4]))
    dict = {".png": 2, ".jpg": 3, ".bmp": 1}
    filelist = []
    for f in files:
        if os.path.isfile(path + '/' + f):
            flag = dict.get(f[-4:], 0)
        if flag:
                filelist.append(path + '\\' + f)
    return filelist


def convert(picture_path, save_path=None):
    filelist = get_file(picture_path)
    l = len(filelist)
    if save_path is None:
        save_path = 'result.pdf'
    c = canvas.Canvas(save_path, pagesize=landscape(A4))
    (w, h) = landscape(A4)
    for i in range(l):
        f = filelist[i]
        c.drawImage(f, 0, 0, w, h)
        c.showPage()
    c.save()


if __name__ == '__main__':
    picture_path = 'F:/Material/Books/深度学习/Attention/Attention Pictures'
    convert(picture_path)
