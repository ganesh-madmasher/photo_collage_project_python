import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
image_names = os.listdir()
royal_enfield = []
for f in image_names:
    if(f.endswith("jpg")):
        # print(f)
        file_path = f
        img = cv2.imread(file_path)
        img = cv2.cvtColor(img, 4)
        img = cv2.resize(img, (200, 200))
        royal_enfield.append(img)
collage1 = np.hstack((royal_enfield[0], royal_enfield[1]))
collage2 = np.hstack((royal_enfield[2], royal_enfield[3]))
collage = np.vstack((collage1, collage2))
collage[100:300, 100:300, :] = royal_enfield[4]
plt.imshow(collage)
plt.axis('off')
plt.show()
