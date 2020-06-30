import glob
import cv2
import numpy as np

cats = ['Asphalt' , 'Brick' , 'Cement-Granular' , 'Clay Hollow Block' , 'Concrete Block' , 'Gravel' , 'Paving' , 'Sand' , 'Soil-Vegetation','Stone' , 'Wood']

x = []
y = []

for cat in cats:
    l_files = glob.glob('./' + cat + '/*')
    print('loading ' + cat + ' data...')
    for f in l_files:
        im = cv2.imread(f)
        x.append(cv2.resize(im , (1024,1024)))
        y.append(cat)

x = np.array(x)
print(x.shape)