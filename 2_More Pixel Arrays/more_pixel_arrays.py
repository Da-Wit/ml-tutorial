from PIL import Image
import numpy as np

i = Image.open('images/dotndot.png')
iar = np.asarray(i)
print(iar)
"""
About alpha,
The higher the number, the more solid the color is,
The lower the number, the more transparent it is.
"""
