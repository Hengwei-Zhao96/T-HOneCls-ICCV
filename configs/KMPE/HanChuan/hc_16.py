config = dict(
    dataset=dict(
        train=dict(
            type='HanChuanDataset',
            params=dict(
                image_path='./Data/UAVData/WHU-Hi-HanChuan/WHU-Hi-HanChuan',
                gt_path='./Data/UAVData/WHU-Hi-HanChuan/Train100',
                train_flage=True,
                num_positive_train_samples=100,
                sub_minibatch=10,
                ccls=16,
                ratio=40
            )
        ),
        test=dict(
            type='HanChuanDataset',
            params=dict(
                image_path='./Data/UAVData/WHU-Hi-HanChuan/WHU-Hi-HanChuan',
                gt_path='./Data/UAVData/WHU-Hi-HanChuan/Test100',
                train_flage=False,
                num_positive_train_samples=100,
                sub_minibatch=10,
                ccls=16,
                ratio=40
            )
        )
    ),

    meta=dict(),
)
