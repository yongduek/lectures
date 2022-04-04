import imageio
import visvis as vv
import numpy as np 

reader = imageio.get_reader('<video0>')
t = vv.imshow(reader.get_next_data(), clim=(0, 255))
r, c = 100, 100
for im in reader:
    vv.processEvents()
    print(type(im), im.meta, im.shape)
    r += int(np.random.normal(0, 5))
    c += int(np.random.normal(0, 5))
    im[r:r+100,c:c+100,:] = (255, 0, 0)
    t.SetData(im)