from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

i = Image.open('images/numbers/y0.5.png')

iar = np.asarray(i)

plt.imshow(iar)
print(iar)
plt.show()

# Actually, I did nothing in this chapter
# because in this chapter, I learned
# what thresholding is, not
# practices. So, I did nothing I think.
