import argparse
import cv2
import sys
import numpy as np
import insightface
from insightface.app import FaceAnalysis
from insightface.data import get_image as ins_get_image

assert insightface.__version__>='0.3'

parser = argparse.ArgumentParser(description='insightface app test')
# general
parser.add_argument('--ctx', default=0, type=int, help='ctx id, <0 means using cpu')
parser.add_argument('--det-size', default=640, type=int, help='detection size')
args = parser.parse_args()

app = FaceAnalysis()
app.prepare(ctx_id=args.ctx, det_size=(args.det_size,args.det_size))

# img = ins_get_image('t1')
# faces = app.get(img)
# assert len(faces)==6
# rimg = app.draw_on(img, faces)
# cv2.imwrite("./t1_output.jpg", rimg)

# # then print all-to-all face similarity
# feats = []
# for face in faces:
#     feats.append(face.normed_embedding)
# feats = np.array(feats, dtype=np.float32)
# sims = np.dot(feats, feats.T)
# print(sims)

def get_box_xyxys(faces):
    results = []
    for i in range(len(faces)):
        face = faces[i]
        box = face.bbox.astype(np.int)
        results.append((box[0], box[1], box[2], box[3]))
    return results

img = cv2.imread('../images/sample_GeneratedPhotosDataset-1024x613.png')
faces = app.get(img)
rimg = app.draw_on(img, faces)
cv2.imwrite("./output.jpg", rimg)
points = get_box_xyxys(faces)
print(points)