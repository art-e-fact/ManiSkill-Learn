_base_ = ['../_base_/bc/bc_mani_skill_pointnet_transformer2.py']


env_cfg = dict(
    type='gym',
    env_name='OpenCabinetDrawer_1045_link_0-v0',
    #env_name='OpenCabinetDoor_1027_link_0-v0',
)


replay_cfg = dict(
    type='ReplayMemory',
    capacity=1000000,
)
nsteps = 150000
train_mfrl_cfg = dict(
    total_steps=nsteps,
    warm_steps=0,
    n_steps=0,
    n_updates=500,
    n_eval=nsteps,
    n_checkpoint=nsteps,
    init_replay_buffers=[
    './example_mani_skill_data/OpenCabinetDrawer_1045_link_0-v0_pcd.h5',
    './full_mani_skill_data/OpenCabinetDoor/OpenCabinetDrawer_1000_link_0-v0.h5',
    './full_mani_skill_data/OpenCabinetDoor/OpenCabinetDrawer_1000_link_1-v0.h5',
    './full_mani_skill_data/OpenCabinetDoor/OpenCabinetDrawer_1056_link_1-v0.h5',
    './full_mani_skill_data/OpenCabinetDoor/OpenCabinetDrawer_1056_link_2-v0.h5',
    './full_mani_skill_data/OpenCabinetDoor/OpenCabinetDrawer_1016_link_0-v0.h5',
    './full_mani_skill_data/OpenCabinetDoor/OpenCabinetDrawer_1016_link_1-v0.h5',
    './full_mani_skill_data/OpenCabinetDoor/OpenCabinetDrawer_1016_link_2-v0.h5',
    './full_mani_skill_data/OpenCabinetDoor/OpenCabinetDrawer_1016_link_3-v0.h5',
    './full_mani_skill_data/OpenCabinetDoor/OpenCabinetDrawer_1027_link_0-v0.h5',
    './full_mani_skill_data/OpenCabinetDoor/OpenCabinetDrawer_1027_link_1-v0.h5',
    './full_mani_skill_data/OpenCabinetDoor/OpenCabinetDrawer_1038_link_0-v0.h5',
    './full_mani_skill_data/OpenCabinetDoor/OpenCabinetDrawer_1044_link_0-v0.h5',
    './full_mani_skill_data/OpenCabinetDoor/OpenCabinetDrawer_1044_link_1-v0.h5',
    './full_mani_skill_data/OpenCabinetDoor/OpenCabinetDrawer_1045_link_0-v0.h5',
    './full_mani_skill_data/OpenCabinetDoor/OpenCabinetDrawer_1052_link_0-v0.h5',
    './full_mani_skill_data/OpenCabinetDoor/OpenCabinetDrawer_1054_link_0-v0.h5',
    './full_mani_skill_data/OpenCabinetDoor/OpenCabinetDrawer_1067_link_0-v0.h5',
    './full_mani_skill_data/OpenCabinetDoor/OpenCabinetDrawer_1076_link_0-v0.h5',
    './full_mani_skill_data/OpenCabinetDoor/OpenCabinetDrawer_1076_link_1-v0.h5',
    './full_mani_skill_data/OpenCabinetDoor/OpenCabinetDrawer_1076_link_2-v0.h5',
    './full_mani_skill_data/OpenCabinetDoor/OpenCabinetDrawer_1076_link_3-v0.h5',
    './full_mani_skill_data/OpenCabinetDoor/OpenCabinetDrawer_1079_link_0-v0.h5',
    './full_mani_skill_data/OpenCabinetDoor/OpenCabinetDrawer_1079_link_1-v0.h5',
    './full_mani_skill_data/OpenCabinetDoor/OpenCabinetDrawer_1079_link_2-v0.h5',
    './full_mani_skill_data/OpenCabinetDoor/OpenCabinetDrawer_1079_link_3-v0.h5',

    './full_mani_skill_data/OpenCabinetDoor/OpenCabinetDoor_1000_link_0-v0.h5',
    './full_mani_skill_data/OpenCabinetDoor/OpenCabinetDoor_1000_link_1-v0.h5',
    './full_mani_skill_data/OpenCabinetDoor/OpenCabinetDoor_1045_link_0-v0.h5',
    './full_mani_skill_data/OpenCabinetDoor/OpenCabinetDoor_1027_link_0-v0.h5',
    './full_mani_skill_data/OpenCabinetDoor/OpenCabinetDoor_1038_link_0-v0.h5',
    './full_mani_skill_data/OpenCabinetDoor/OpenCabinetDoor_1042_link_1-v0.h5',
    './full_mani_skill_data/OpenCabinetDoor/OpenCabinetDoor_1042_link_3-v0.h5',
    './full_mani_skill_data/OpenCabinetDoor/OpenCabinetDoor_1044_link_0-v0.h5',
    './full_mani_skill_data/OpenCabinetDoor/OpenCabinetDoor_1044_link_1-v0.h5',
    './full_mani_skill_data/OpenCabinetDoor/OpenCabinetDoor_1044_link_2-v0.h5',
    './full_mani_skill_data/OpenCabinetDoor/OpenCabinetDoor_1044_link_3-v0.h5',
    './full_mani_skill_data/OpenCabinetDoor/OpenCabinetDoor_1045_link_0-v0.h5',
    './full_mani_skill_data/OpenCabinetDoor/OpenCabinetDoor_1052_link_0-v0.h5',
    './full_mani_skill_data/OpenCabinetDoor/OpenCabinetDoor_1052_link_1-v0.h5',
    './full_mani_skill_data/OpenCabinetDoor/OpenCabinetDoor_1054_link_0-v0.h5',
    './full_mani_skill_data/OpenCabinetDoor/OpenCabinetDoor_1061_link_0-v0.h5',
    './full_mani_skill_data/OpenCabinetDoor/OpenCabinetDoor_1063_link_0-v0.h5',
    './full_mani_skill_data/OpenCabinetDoor/OpenCabinetDoor_1064_link_1-v0.h5',
    './full_mani_skill_data/OpenCabinetDoor/OpenCabinetDoor_1064_link_3-v0.h5',
    './full_mani_skill_data/OpenCabinetDoor/OpenCabinetDoor_1067_link_0-v0.h5',
    './full_mani_skill_data/OpenCabinetDoor/OpenCabinetDoor_1075_link_0-v0.h5',
    './full_mani_skill_data/OpenCabinetDoor/OpenCabinetDoor_1075_link_1-v0.h5',
    './full_mani_skill_data/OpenCabinetDoor/OpenCabinetDoor_1078_link_0-v0.h5',
    './full_mani_skill_data/OpenCabinetDoor/OpenCabinetDoor_1078_link_1-v0.h5',
    ]
)

eval_cfg = dict(
    num=10,
    num_procs=1,
    use_hidden_state=False,
    start_state=None,
    save_traj=True,
    save_video=False,
    use_log=False,
)
