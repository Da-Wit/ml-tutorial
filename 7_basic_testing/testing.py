from PIL import Image
import numpy as np

import time
from collections import Counter

def whatNumIsThis(filePath):

    matchedAr = []
    loadExamps = open('6_data_saving/numArEx.txt','r').read()
    loadExamps = loadExamps.split('\n')

    i = Image.open(filePath)
    iar = np.array(i)
    iarl = iar.tolist()

    inQuestion = str(iarl)

    for eachExample in loadExamps:
        try:
            splitEx = eachExample.split('::')
            currentNum = splitEx[0]
            currentAr = splitEx[1]

            eachPixEx = currentAr.split('],')
            eachPixInQ = inQuestion.split('],')

            x = 0

            while x < len(eachPixEx):
                if eachPixEx[x] == eachPixInQ[x]:
                    matchedAr.append(int(currentNum))

                x += 1
        except Exception as e:
            print(str(e))

    # print(matchedAr)
    x = Counter(matchedAr)
    print("x: ",x)
    # print("x[0]: ",x[2])


whatNumIsThis('images/numbers/0.1.png')
whatNumIsThis('images/numbers/1.2.png')
whatNumIsThis('images/numbers/2.3.png')
whatNumIsThis('images/numbers/3.1.png')
whatNumIsThis('images/numbers/4.4.png')
whatNumIsThis('images/numbers/5.1.png')
whatNumIsThis('images/numbers/6.1.png')
whatNumIsThis('images/numbers/7.1.png')
whatNumIsThis('images/numbers/8.9.png')
whatNumIsThis('images/numbers/9.1.png')
