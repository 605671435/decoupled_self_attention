_base_ = ['../resnet/fcn_r50-d8_1xb2-40k_lits17-512x512.py']

model = dict(
    backbone=dict(plugins=[dict(cfg=dict(type='ContextBlock',
                                         ratio=1 / 4.),
                                stages=(True, True, True, True),
                                position='after_conv1')]))

vis_backends = [
    dict(type='LocalVisBackend'),
    dict(
        type='WandbVisBackend',
        init_kwargs=dict(
            project='lits17', name='fcn-r50-gcnet-40k'),
        define_metric_cfg=dict(mDice='max'))
]
visualizer = dict(
    type='SegLocalVisualizer', vis_backends=vis_backends, name='visualizer')

