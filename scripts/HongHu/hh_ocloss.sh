for repeat in 1 2 3 4 5
do
CUDA_VISIBLE_DEVICES=0 python tools/train.py -c 'configs/HongHu/OCLoss/4.py'
CUDA_VISIBLE_DEVICES=0 python tools/train.py -c 'configs/HongHu/OCLoss/6.py'
CUDA_VISIBLE_DEVICES=0 python tools/train.py -c 'configs/HongHu/OCLoss/7.py'
CUDA_VISIBLE_DEVICES=0 python tools/train.py -c 'configs/HongHu/OCLoss/9.py'
CUDA_VISIBLE_DEVICES=0 python tools/train.py -c 'configs/HongHu/OCLoss/10.py'
#CUDA_VISIBLE_DEVICES=0 python tools/train.py -c 'configs/HongHu/OCLoss/11.py'
#CUDA_VISIBLE_DEVICES=0 python tools/train.py -c 'configs/HongHu/OCLoss/18.py'
#CUDA_VISIBLE_DEVICES=0 python tools/train.py -c 'configs/HongHu/OCLoss/19.py'
done