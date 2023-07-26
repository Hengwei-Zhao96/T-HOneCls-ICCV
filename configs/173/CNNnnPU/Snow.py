config = dict(
    dataset=dict(
        train=dict(
            type='OneSevenThreeDataset',
            params=dict(
                image_path='./Data/173Data/Snow/snow.dat',
                # image_path='./Data/173Data/Snow/noise.dat',
                gt_path='./Data/173Data/Snow/Snow_unlabeled_gt',
                train_flage=True,
                num_positive_train_samples=50,
                sub_minibatch=10,
                ccls=1,
                ratio=400
            )
        ),
        test=dict(
            type='OneSevenThreeDataset',
            params=dict(
                image_path='./Data/173Data/Snow/snow.dat',
                # image_path='./Data/173Data/Snow/noise.dat',
                gt_path='./Data/173Data/Snow/Snow_unlabeled_gt',
                train_flage=False,
                num_positive_train_samples=50,
                sub_minibatch=10,
                ccls=1,
                ratio=400
            )
        )
    ),
    model=dict(
        type='FreeNetEncoder',
        params=dict(
            in_channels=36,
            out_channels=1,
            patch_size=15,
        )
    ),
    loss_function=dict(
        type='NnPULossPb',
        params=dict(
            prior=0.01348747591522158,
            beta=None,
            gamma=None
        ),
    ),
    optimizer=dict(
        type='SGD',
        params=dict(
            lr=0.0003,
            momentum=0.9,
            weight_decay=0.0001
        ),
    ),
    lr_scheduler=dict(
        type='ExponentialLR',
        params=dict(
            gamma=1),
    ),
    trainer=dict(
        type='SingleModelTrainer_PB',
        params=dict(
            max_iters=200,
            clip_grad=6,
            patch_size=15,
            batch_size_pb=1024,
        ),
    ),
    meta=dict(
        save_path='Log/173',
        image_size=(624, 848),
        palette=[
            [0, 0, 0],
            [255, 0, 0]],
    )
)
