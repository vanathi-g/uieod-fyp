# Underwater Image Enhancement and Object Detection Based on Generative Adversarial Networks

The Underwater Image Enhancement and Object Detection (UIEOD) system performs image enhancement on low quality underwater images followed by object detection on the enhanced images. A super resolution generative adversarial network (SRGAN) is used to improve the quality of underwater images, and the Darknet YOLOv3 is used to perform object detection on the enhanced underwater images to identify sea cucumbers, sea urchins, scallops, and starfishes.

## Datasets

* Underwater Image Enhancement Benchmark (UIEB)

The SRGAN is trained on the publicly available Underwater Image Enhancement Benchmark consisting of original images and corresponding reference images. The dataset contains 890 natural underwater images and their enhanced counterparts for reference. The dataset also contains a challenging set consisting of 60 original images without their corresponding reference images.

URL: https://li-chongyi.github.io/proj_benchmark.html

* Detecting Underwater Objects (DUO)

The YOLOv3 model is trained on the publicly available Detection of Underwater Objects (DUO) dataset. Categories of objects: holothurians, echinus, scallops, and starfishes. It has 6671 training images and 1111 testing images.The dataset is structured as two parts: the images and annotations of the images.

URL: https://github.com/chongweiliu/DUO

## Software and Hardware Requirements

For software we will require python3 with the following libraries installed:

* keras
* numpy
* Python Imaging Library (PIL)
* glob
* continue for srgan
* darknet
* continue for yolo

## Instructions to execute code

### SRGAN execution

* stuff

### YOLOv3 execution

* stuff
