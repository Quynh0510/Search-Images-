
import os
import argparse
from flask import Flask
from flask import request, json
import requests
import matplotlib as plt
from test import *

app = Flask(__name__)

bov = BOV(no_clusters=100)
# parse cmd args
parser = argparse.ArgumentParser(
        description=" Bag of visual words example"
    )
# parser.add_argument('--train_path', action="store", dest="train_path", required=True)
# parser.add_argument('--test_path', action="store", dest="test_path", required=True)



# set training paths
bov.train_path = 'images/train/'

# train the model
bov.trainModel()

@app.route('/', methods=['POST'])
def searchImage (file) :
    # set testing paths
    bov.test_path = file

    # test model
    
    # bov.testModel()
    # print('result : ', bov.testModel())
    result = {}
    a = os.listdir('images/train/' + bov.testModel()[0])
    result['images'] = file
    result['sim'] = a
    # for i in a :
    #     # cv2.imshow(each['object_name'], each['image'])
    #     # cv2.waitKey()
    #     # cv2.destroyWindow(each['object_name'])
    #     # 
    #     plt.imshow(cv2.cvtColor(i['image'], cv2.COLOR_GRAY2RGB))
    #     plt.title(i['object_name'])
    #     plt.show()use
    return result




# if __name__ == "__main__":
#     app.run( port=8080, host="0.0.0.0", threaded=True) #debug=True, use_reloader=True,


print(searchImage('images/test/test/396.jpg'))

