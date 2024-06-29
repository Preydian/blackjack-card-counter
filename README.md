# Blackjack Card Counting with YOLO

## Prerequisites

```
cd yolov7-custom
pip install -r requirements.txt
pip install -r requirements_gpu.txt
```

## How to Run
Run the below command from the yolov7-custom directory
device 0 specifices a CUDA GPU, otherwise use cpu
source 0 specifies a webcam
### GPU
```
python3 detect.py --weights best.pt --device 0 --source 0
```
### CPU
```
python3 detect.py --weights best.pt --device cpu --source 0
```

# Training Data
The code to generate the training dataset can be found in the `dataset-generation` directory. 
The `Jupyter Notebok` contains the in depth instructions to perform. 

## Code structure
Within the `yolov7-custom` directory there are two main files. `detect.py` and `cardCounting.py`. The former handles
running the yolo model while the latter is blackjack card counting specific code. 

## User Input
Lines `35 - 48` allow the user to press `r` or any of a single digit number `0 - 9`. 

### Resetting The Counts
Pressing `r` resets both the counts and the dictionary of seen cards. Essential starting from scratch.

### Updating True Count
The number keys allow the user to specify how many decks remain in play. This affects the calculation 
for the True count. Although you can specify multiple decks, the method can only count through 1 deck at a time.

### Demo

[demo.webm](https://github.com/Preydian/blackjack-card-counter/assets/102883379/16ce82c9-c826-4415-b9ac-a6ec1b014b68)
