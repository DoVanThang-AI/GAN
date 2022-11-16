from options import ModelOptions
from main import main

options = ModelOptions().parse()
options.mode = 0
main(options)
#python train.py --seed 100 --dataset cifar10 --dataset-path dataset/cifar10 --checkpoints-path ./checkpoints --batch-size 128 --epochs 200 --lr 3e-4  --lr-decay-steps 1e4  --augment True