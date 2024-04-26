# **Steps to Setup YOLOv5 and Reinforcement Learning w/ CARLA**
The Reinforcement Learning Group's Senior Design at the University of Detroit Mercy. Please see our associated [Paper](https://github.com/legendairytri/YOLO-RL-CARLA/blob/main/Final%20Report%20Autonomous%20Driving%20via%20RL%20with%20Object%20Detection.pdf) and [Presentation](https://github.com/legendairytri/YOLO-RL-CARLA/blob/main/Presentation%20Autonomous%20Driving%20via%20RL%20with%20Object%20Detection.pdf).


# System Requirements
_The requirements are based on the computers we have access to. I will attempt to list the requirements in a manner that can be adapted for each user._

## Computer Configuration
- Ubuntu 18.02
- Python 3.8  
- CARLA 9.14
- Cuda 11.6
- Pytorch 1.12.1
- NVIDIA Driver 510
- RTX 3060 LHR

_The CUDA integration is essential for the YOLO code, so that is why there is the emphasis on getting the versioning correct here at the start._

## Necessary Downloads
### CARLA
Download CARLA_0.9.14.tar.gz from [CARLA_0.9.14](https://github.com/carla-simulator/carla/releases/tag/0.9.14/)
Extract CARLA simulator to desired location.

### YOLO Code
Download zip file of [YOLO Code](https://github.com/ferdialaca/Carla_Detection_YOLOv5).
Extract YOLO code into examples folder of the CARLA simulator. 
> base folder/CARLA/PythonAPI/examples

Download the best.pt from either link below
[best.pt file](https://drive.google.com/file/d/1MxxIOVqHve3JCYKMepqFAgmI86mF_wXH/view) for Traffic Lights
[best.pt](https://drive.google.com/file/d/1EuuVSsFQEEKmEoeWUMMzQSwsDmNbenxJ/view?usp=sharing) file for crosswalks

_Note: This is the weights file that is generated after running the training file from Ultralytics YOLOv5. The chosen best.pt file should also be placed in the examples folder._

### Reinforcement Learning Code
Download zip file of [Reinforcement Learning Code](https://github.com/cjy1992/gym-carla/tree/master).
Extract Reinforcement Learning Code into the examples folder of the CARLA simulator.

### Code from this GitHub Repository
This repository was made with the folder structure of the source codes that it has used in mind. The examples folder should be merged with the examples of the simulator. The utils folder has some changes for the YOLO code and the gym_carla folder has changes in the environment for the Reinforcement Learning Code.

# Steps to Run
After all of the downloads, this code runs in a few different sections. 
1. Virtual Envelope/ Conda Environment
2. Initial Downloads
3. Testing
4. CARLA Code(s)
5. YOLO Code
6. Reinforcement Learning Code

## 1. Venv/ CONDA
**Before downloading the related content**

Create a virtual environment or CONDA environemnt to isolate and resolve versioning/ dependency issues.

For a virtual Environment,
```

```


## 2. Initial Downloads
```
python -m pip install --upgrade pip
python -m pip install --upgrade pillow
pip install pygame numpy && pip3 install pygame numpy
pip install carla
pip install gym
pip install wheel
pip install torch==1.12.1+cu116 torchvision==0.13.1+cu116 torchaudio==0.12.1 --extra-index-url https://download.pytorch.org/whl/cu116 
```

### Requirements Documents
```
sudo pip install -r requirements.txt (gym)
pip install scikit-image
```

## Testing
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







# Description
/Display w/ figures/ 

### codes
https://github.com/cjy1992/gym-carla/blob/master/README.md
https://github.com/ferdialaca/Carla_Detection_YOLOv5/tree/main

https://github.com/ultralytics/yolov5/tree/master
https://github.com/carla-simulator/carla/releases/tag/0.9.14/

https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#headings 
