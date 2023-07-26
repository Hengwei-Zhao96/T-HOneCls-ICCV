config = dict(
    dataset=dict(
        train=dict(
            type='OsMccLongKouDataset',
            params=dict(
                image_path='/home/zhw2021/code/HOneCls/Data/UAVData/WHU-Hi-LongKou/WHU-Hi-LongKou',
                gt_path='/home/zhw2021/code/HOneCls/Data/UAVData/WHU-Hi-LongKou/Train100_new_label.npy',
                train_flage=True,
                num_classes=6,
                num_train_samples_per_class=100,
                sub_minibatch=5,
                num_unlabeled_samples=4000
            )
        ),
        test=dict(
            type='OsMccLongKouDataset',
            params=dict(
                image_path='/home/zhw2021/code/HOneCls/Data/UAVData/WHU-Hi-LongKou/WHU-Hi-LongKou',
                gt_path='/home/zhw2021/code/HOneCls/Data/UAVData/WHU-Hi-LongKou/Test100_new_open_label.npy',
                train_flage=False,
                num_classes=7,
                num_train_samples_per_class=100,
                sub_minibatch=5,
                num_unlabeled_samples=4000
            )
        )
    ),
    model=dict(
        type='FreeNetEncoder',
        params=dict(
            in_channels=270,
            out_channels=6,
            patch_size=9,
        )
    ),
    loss_function=dict(
        type='None',
        params=dict(),
    ),
    optimizer=dict(
        type='None',
        params=dict(),
    ),
    lr_scheduler=dict(
        type='None',
        params=dict(),
    ),
    trainer=dict(
        type='OsPOODDetectorTrainer_PB',
        params=dict(
            detector_name='KLMatching',
            # MCD, MaxSoftmax, Mahalanobis, EnergyBased, Entropy, MaxLogit, ODIN, KLMatching
            checkpoint_path="/home/zhw2021/code/HOneCls/Log/MCC_for_Open_Set/MccLongKouDataset/MccSingleModelTrainer_PB/CELossPb/FreeNetEncoder/2023-06-15 13-59-53/checkpoint.pth",
            patch_size=9,
            batch_size_pb=256,
        ),
    ),
    meta=dict(
        save_path='./Log/OpenSet',
        image_size=(550, 400),
        palette_class_mapping={1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 0},
        palette=[
            [0, 0, 0],
            [255, 0, 0],
            [238, 154, 0],
            [255, 255, 0],
            [0, 255, 0],
            [0, 255, 255],
            [0, 139, 139],
            [0, 0, 255],
            [255, 255, 255],
            [160, 32, 240]
        ],
    )
)
