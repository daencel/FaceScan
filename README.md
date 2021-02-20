<h1 align="center">
  <img alt="GitHub repo size" src="https://github.com/DanielLechner/FaceScan/blob/main/app/pictures/logo1.png">
</h1>

<p align="center">
  <a href="https://github.com/DanielLechner/FaceScan/blob/main/LICENSE"><img alt="GitHub license" src="https://img.shields.io/github/license/DanielLechner/FaceScan"></a>
  <a href="https://github.com/DanielLechner/FaceScan/stargazers"><img alt="GitHub stars" src="https://img.shields.io/github/stars/DanielLechner/FaceScan"></a>
  <a href="https://github.com/DanielLechner/FaceScan/network"><img alt="GitHub forks" src="https://img.shields.io/github/forks/DanielLechner/FaceScan"></a>
  <a href="https://github.com/DanielLechner/FaceScan/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/DanielLechner/FaceScan"></a>
  <img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/DanielLechner/FaceScan">
</p>
<p align="center">
FaceScan is a Python program which can detect face masks in webcams, images or video files and streams
</p>

## 📖 Table of Contents

* [Face Scan](#face-scan)
  * [Demo](#-demo)
    * [Webcam](#-webcam)
    * [Files](#-files)
    * [Online Streams](#-online-streams)
    * [Use with GUI Interface](#-use-with-gui-interface)
  * [Installation](#️-installation)
  * [Usage](#-usage)
  * [Models](#-models)
  * [Code Contributors](#-code-contributors)
  * [License](#-license)


## ✨ Demo
#### 📹 Webcam
FaceScan is able to detect face masks in video feed from connected webcams in realtime:
<img src="https://github.com/DanielLechner/FaceScan/blob/main/readme/webcam.gif">

#### 📁 Files
FaceScan is able to detect face masks from locally saved video and image files:

<table style="width:100%">
    <tr>
      <td><p>Before</p></td>
      <td><p>After</p></td>
    </tr>
    <tr>
        <td><img src="https://github.com/DanielLechner/FaceScan/blob/main/readme/before_images/0.jpg"></td>
        <td><img src="https://github.com/DanielLechner/FaceScan/blob/main/readme/after_images/0.jpg"></td>
    </tr>
  <tr>
        <td><img src="https://github.com/DanielLechner/FaceScan/blob/main/readme/before_images/1.jpg"></td>
        <td><img src="https://github.com/DanielLechner/FaceScan/blob/main/readme/after_images/1.jpg"></td>
    </tr>
    <tr>
        <td><img src="https://github.com/DanielLechner/FaceScan/blob/main/readme/before_images/2.jpg"></td>
        <td><img src="https://github.com/DanielLechner/FaceScan/blob/main/readme/after_images/2.jpg"></td>
    </tr>
</table>

#### 📲 Online Streams
FaceScan is able to detect face masks from online streams such as rtsp, rtmp and http.

#### 💻 Use with GUI Interface
FaceScan also comes with a <a href="https://github.com/DanielLechner/FaceScan/blob/main/app/layout.py">GUI</a> which functions the same way as the python command, just with an easier interface.

<img src="https://github.com/DanielLechner/FaceScan/blob/main/readme/interface.png">

## ⚙️ Installation

Clone the [git repo](https://github.com/DanielLechner/FaceScan)
```bash
$ git clone https://github.com/DanielLechner/FaceScan
```

Change directory to [FaceScan/app](https://github.com/DanielLechner/FaceScan/tree/main/app)
```bash
$ cd FaceScan/app
```
__If you are using Windows, then go into your [Anaconda](https://docs.conda.io/projects/conda/en/latest/index.html) environment and install torchvision with this command__
```bash
$ conda install pytorch torchvision cpuonly -c pytorch-nightly -c defaults -c conda-forge
```

Intstall all dependencies from [requirements.txt](https://github.com/DanielLechner/FaceScan/blob/main/app/requirements.txt). We reccomend using Python 3.8.5.
```bash
$ pip install -r requirements.txt
```

Enviroment should now be fully functional

## 🚀 Usage

As mentioned above, there are many ways to use our Python program. Here you can check all the functions:

```bash
$ python detect.py --source 0  # webcam
                            file.jpg  # image 
                            file.mp4  # video
                            path/  # directory
                            path/*.jpg  # glob
                            rtsp://170.93.143.139/rtplive/470011e600ef003a004ee33696235daa  # rtsp stream
                            rtmp://192.168.1.105/live/test  # rtmp stream
                            http://112.50.243.8/PLTV/88888888/224/3221225900/1.m3u8  # http stream

```

All outputs are saved in ``` FaceScan/app/runs/detect```

Furthermore you can use the following parser tags:
```
--weights: weights of the trained model
--source: input file/folder to run inference on, 0 for webcam
--output: directory to save results
--iou-thres: IOU threshold for NMS, defaults to 0.45
--conf-thres: object confidence threshold
```

## 🧠 Models

We decided to use the yolov5s model, since it is the fastes. This is important since live feed has to be computet very fast to have no lag.

<img src="https://github.com/DanielLechner/FaceScan/blob/main/readme/yolov5_models.png" width="1000">
<img src="https://github.com/DanielLechner/FaceScan/blob/main/readme/models.png" width="1000">


Our weights file has a high precision as you can see in this graph, which represents the confidence the trained model has gained over time. This is tested with the "test" Dataset. 
<img src="https://github.com/DanielLechner/FaceScan/blob/main/readme/confidence-curve.png">
<img src="https://github.com/DanielLechner/FaceScan/blob/main/readme/classes.jpg">



## 👨🏾‍💻👨🏻‍💻 Code Contributors


## 📝 License

To check out more about our License click <a href="https://github.com/DanielLechner/FaceScan/blob/main/LICENSE">here</a>
