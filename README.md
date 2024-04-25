# **Steps to Setup YOLOv5 and Reinforcement Learning w/ CARLA**
The Reinforcement Learning Group's Senior Design at the University of Detroit Mercy. 

# Associated Paper and Presentation
[Paper](https://github.com/legendairytri/YOLO-RL-CARLA/blob/main/Final%20Report%20Autonomous%20Driving%20via%20RL%20with%20Object%20Detection.pdf)

[Presentation](https://github.com/legendairytri/YOLO-RL-CARLA/blob/main/Presentation%20Autonomous%20Driving%20via%20RL%20with%20Object%20Detection.pdf)

# Description
/Display w/ figures/

# System Requirements
_The requirements are based on the computers we have access to. I will attempt to list the requirements in a manner that can be adapted for each user._

## Computer Configuration
- Ubuntu 18.02
- Python 3.8  
- CARLA 9.14
- Cuda 11.6
- Pytorch 1.12.1
- GPU Driver

_The CUDA integration is essential for the YOLO code, so that is why there is the emphasis on getting the versioning correct here at the start._

## Necessary Downloads
### CARLA
Download CARLA_0.9.14.tar.gz from [CARLA_0.9.14](https://github.com/carla-simulator/carla/releases/tag/0.9.14/)
Extract CARLA simulator to desired location.

### YOLO Code
Download zip file of [YOLO code](https://github.com/ferdialaca/Carla_Detection_YOLOv5)
Extract YOLO code into examples folder of CARLA simulator. 
> base folder/CARLA/PythonAPI/examples

# Steps to Run
```
python -m pip install --upgrade pip
python -m pip install --upgrade pillow
pip install pygame numpy && pip3 install pygame numpy
pip install carla
pip install gym
pip install wheel
sudo pip install -r requirements.txt (gym)
pip install scikit-image
pip install torch==1.12.1+cu116 torchvision==0.13.1+cu116 torchaudio==0.12.1 --extra-index-url https://download.pytorch.org/whl/cu116 
```

Checking pytorch Cuda connection
```
import torch
torch.cuda.is_available()
quit()
Downloading CARLA
```
Testing CARLA
Activate venv
```
source <venvname>/bin/activate
```
Navigate into venv and run CARLA server
```
cd <venvname>
./CarlaUE4.sh
```
Open new tab and run clientside python file
```
source YOLOvenv/bin/activate
cd YOLOvenv/PythonAPI/examples/
python manual_control.py
```

Setting up YOLO
```
pip install -r requirements.txt (both for carla and YOLO
```
Update ultralytics code
>ultralytics.yolo.utils->ultralytics.utils








### codes
https://github.com/cjy1992/gym-carla/blob/master/README.md
https://github.com/ferdialaca/Carla_Detection_YOLOv5/tree/main

https://github.com/ultralytics/yolov5/tree/master
https://github.com/carla-simulator/carla/releases/tag/0.9.14/

https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#headings 
