for repeat in 1 2 3 4 5
do
CUDA_VISIBLE_DEVICES=2 python tools/train.py -c 'configs/HanChuan/OCLoss/1.py'
CUDA_VISIBLE_DEVICES=2 python tools/train.py -c 'configs/HanChuan/OCLoss/2.py'
CUDA_VISIBLE_DEVICES=2 python tools/train.py -c 'configs/HanChuan/OCLoss/3.py'
#CUDA_VISIBLE_DEVICES=2 python tools/train.py -c 'configs/HanChuan/OCLoss/5.py'
CUDA_VISIBLE_DEVICES=2 python tools/train.py -c 'configs/HanChuan/OCLoss/6.py'
CUDA_VISIBLE_DEVICES=2 python tools/train.py -c 'configs/HanChuan/OCLoss/14.py'
CUDA_VISIBLE_DEVICES=2 python tools/train.py -c 'configs/HanChuan/OCLoss/16.py'
done