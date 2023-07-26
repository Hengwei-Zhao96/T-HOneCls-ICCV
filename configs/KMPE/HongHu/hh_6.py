config = dict(
    dataset=dict(
        train=dict(
            type='HongHuDataset',
            params=dict(
                image_path='/home/zhw2021/code/HOneCls/Data/UAVData/WHU-Hi-HongHu/data',
                gt_path='/home/zhw2021/code/HOneCls/Data/UAVData/WHU-Hi-HongHu/gt',
                train_flage=True,
                num_positive_train_samples=100,
                sub_minibatch=10,
                ccls=6,
                ratio=40
            )
        ),
        test=dict(
            type='HongHuDataset',
            params=dict(
                image_path='/home/zhw2021/code/HOneCls/Data/UAVData/WHU-Hi-HongHu/data',
                gt_path='/home/zhw2021/code/HOneCls/Data/UAVData/WHU-Hi-HongHu/gt',
                train_flage=False,
                num_positive_train_samples=100,
                sub_minibatch=10,
                ccls=6,
                ratio=40
            )
        )
    ),
    meta=dict()
)
