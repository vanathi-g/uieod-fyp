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

Software: Python3 with the following libraries installed:

* tensorflow
* keras
* scipy
* numpy
* Python Imaging Library (PIL)
* matplotlib
* glob
* darknet
* continue for yolo

Hardware (recommended): 12GB RAM, Nvidia Tesla T4 GPU, Intel Xeon CPU @ 2.30GHz (Google Colab free tier specs)

## Instructions to execute code

### SRGAN Training and Testing

1. Ensure the UIEB dataset folders are available (either host on Github or upload zip file to drive and unzip as required). The required folders are already avilable [here](https://github.com/vanathi-g/fyp-datasets.git).
2. Download and prepare to run SRGAN_code.ipynb (found in SRGAN folder) either in Jupyter notebook or Google Colab (recommended). 
3. Install required libraries specified in the first cell of the notebook.
4. Authorize Google drive access to ensure model checkpoints are taken properly. 
5. Follow instructions in the notebook to set appropriate file and folder paths to dataset and model chekpoint folders.
6. Specify a file to save loss values and FID scores to. This will be used to plot losses later. 
7. For training, configure parameters such as starting epoch, loss step, checkpoint step and so on. The weights file to continue training from is also configurable.
8. For testing, the generator trained in step 7 can be used or a saved model may be loaded as well. 
9. Follow instructions in the notebook to configure how to calculate FID over a batch of images.
10. To test images from the UIEB "challenging" set, ensure the path to the dataset is correct and run the last cell.

### YOLOv3 execution

* stuff
