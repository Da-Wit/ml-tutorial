from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import time

def createExamples():
    numberArrayExamples = open('6_data_saving/numArEx.txt','a')
    numbersWeHave = range(0, 10)
    numberOfNumbers = range(1, 10)
    print("numbersWeHave:",numbersWeHave)
    for eachNum in numbersWeHave:
        # print eachNum
        for furtherNum in numberOfNumbers:
            print(str(eachNum) + '.' + str(furtherNum))
            imageFilePath = 'images/numbers/' + str(eachNum) + '.' + str(furtherNum) + '.png'
            ei = Image.open(imageFilePath)
            eiar = np.array(ei)
            eiarl = str(eiar.tolist())

            print(eiarl)
            lineToWrite = str(eachNum) + '::' + eiarl + '\n'
            numberArrayExamples.write(lineToWrite)
createExamples()
