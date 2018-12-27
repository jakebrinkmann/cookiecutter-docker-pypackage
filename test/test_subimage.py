from skimage import data

def test_find():
    im = data.coins()
    y, x = (170, 75)
    tpl = im[y:y+50, x:x+50].copy()
    assert((y, x) == find_image(im, tpl))
