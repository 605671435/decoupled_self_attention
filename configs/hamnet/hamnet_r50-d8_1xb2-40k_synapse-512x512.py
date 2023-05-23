_base_ = ['../resnet/fcn_r50-d8_1xb2-40k_synapse-512x512.py']
# model settings
ham_norm_cfg = dict(type='GN', num_groups=32, requires_grad=True)
model = dict(
    decode_head=dict(
        _delete_=True,
        type='HamHead',
        in_channels=2048,
        in_index=3,
        channels=512,
        ham_channels=512,
        dropout_ratio=0.1,
        num_classes=9,
        norm_cfg=ham_norm_cfg,
        align_corners=False,
        loss_decode=[
            dict(
                type='CrossEntropyLoss', use_sigmoid=False, loss_weight=1.2),
            dict(
                type='DiceLoss', loss_weight=0.8)]))

vis_backends = [
    dict(type='LocalVisBackend'),
    dict(
        type='WandbVisBackend',
        init_kwargs=dict(
            project='synapse', name='fcn-r50-hamnet-40k'),
        define_metric_cfg=dict(mDice='max'))
]
visualizer = dict(
    type='SegLocalVisualizer', vis_backends=vis_backends, name='visualizer')