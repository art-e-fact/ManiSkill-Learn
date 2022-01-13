_base_ = ['../_base_/bc/bc_mani_skill_pointnet_transformer3.py']


env_cfg = dict(
    type='gym',
    env_name='OpenCabinetDrawer_1045_link_0-v0',
    #env_name='OpenCabinetDoor_1027_link_0-v0',
)


replay_cfg = dict(
    type='ReplayMemory',
    capacity=1000000,
)
nsteps = 25002
train_mfrl_cfg = dict(
    total_steps=nsteps,
    warm_steps=0,
    n_steps=0,
    n_updates=500,
    n_eval=nsteps,
    n_checkpoint=nsteps,
    init_replay_buffers=[
    # Drawer environments with cabinet present at least once in both drawer and door
    './full_mani_skill_data/OpenCabinetDrawer/OpenCabinetDrawer_1000_link_0-v0.h5',
    './full_mani_skill_data/OpenCabinetDrawer/OpenCabinetDrawer_1000_link_1-v0.h5',
    './full_mani_skill_data/OpenCabinetDrawer/OpenCabinetDrawer_1016_link_0-v0.h5',
    './full_mani_skill_data/OpenCabinetDrawer/OpenCabinetDrawer_1016_link_1-v0.h5',
    './full_mani_skill_data/OpenCabinetDrawer/OpenCabinetDrawer_1016_link_2-v0.h5',
    './full_mani_skill_data/OpenCabinetDrawer/OpenCabinetDrawer_1016_link_3-v0.h5',
    './full_mani_skill_data/OpenCabinetDrawer/OpenCabinetDrawer_1027_link_0-v0.h5',
    './full_mani_skill_data/OpenCabinetDrawer/OpenCabinetDrawer_1027_link_1-v0.h5',
    './full_mani_skill_data/OpenCabinetDrawer/OpenCabinetDrawer_1038_link_0-v0.h5',
    './full_mani_skill_data/OpenCabinetDrawer/OpenCabinetDrawer_1044_link_0-v0.h5',
    './full_mani_skill_data/OpenCabinetDrawer/OpenCabinetDrawer_1044_link_1-v0.h5',
    './full_mani_skill_data/OpenCabinetDrawer/OpenCabinetDrawer_1045_link_0-v0.h5',
    './full_mani_skill_data/OpenCabinetDrawer/OpenCabinetDrawer_1052_link_0-v0.h5',
    './full_mani_skill_data/OpenCabinetDrawer/OpenCabinetDrawer_1054_link_0-v0.h5',
    './full_mani_skill_data/OpenCabinetDrawer/OpenCabinetDrawer_1056_link_0-v0.h5',
    './full_mani_skill_data/OpenCabinetDrawer/OpenCabinetDrawer_1056_link_1-v0.h5',
    './full_mani_skill_data/OpenCabinetDrawer/OpenCabinetDrawer_1056_link_2-v0.h5',
    './full_mani_skill_data/OpenCabinetDrawer/OpenCabinetDrawer_1067_link_0-v0.h5',
    './full_mani_skill_data/OpenCabinetDrawer/OpenCabinetDrawer_1076_link_0-v0.h5',
    './full_mani_skill_data/OpenCabinetDrawer/OpenCabinetDrawer_1076_link_1-v0.h5',
    './full_mani_skill_data/OpenCabinetDrawer/OpenCabinetDrawer_1076_link_2-v0.h5',
    './full_mani_skill_data/OpenCabinetDrawer/OpenCabinetDrawer_1076_link_3-v0.h5',
    './full_mani_skill_data/OpenCabinetDrawer/OpenCabinetDrawer_1079_link_0-v0.h5',
    './full_mani_skill_data/OpenCabinetDrawer/OpenCabinetDrawer_1079_link_1-v0.h5',
    './full_mani_skill_data/OpenCabinetDrawer/OpenCabinetDrawer_1079_link_2-v0.h5',
    './full_mani_skill_data/OpenCabinetDrawer/OpenCabinetDrawer_1079_link_3-v0.h5',
    './full_mani_skill_data/OpenCabinetDrawer/OpenCabinetDrawer_1063_link_0-v0.h5',

    # environments with at least 2 drawers
    './full_mani_skill_data/OpenCabinetDrawer/OpenCabinetDrawer_1004_link_0-v0.h5',
    './full_mani_skill_data/OpenCabinetDrawer/OpenCabinetDrawer_1004_link_1-v0.h5',
    './full_mani_skill_data/OpenCabinetDrawer/OpenCabinetDrawer_1024_link_0-v0.h5',
    './full_mani_skill_data/OpenCabinetDrawer/OpenCabinetDrawer_1024_link_1-v0.h5',
    './full_mani_skill_data/OpenCabinetDrawer/OpenCabinetDrawer_1024_link_2-v0.h5',

    #other Drawer
    #'./full_mani_skill_data/OpenCabinetDrawer/OpenCabinetDrawer_1005_link_3-v0.h5',
    #'./full_mani_skill_data/OpenCabinetDrawer/OpenCabinetDrawer_1013_link_0-v0.h5',
    #'./full_mani_skill_data/OpenCabinetDrawer/OpenCabinetDrawer_1021_link_0-v0.h5',
    #'./full_mani_skill_data/OpenCabinetDrawer/OpenCabinetDrawer_1032_link_0-v0.h5',
    #'./full_mani_skill_data/OpenCabinetDrawer/OpenCabinetDrawer_1033_link_2-v0.h5',
    #'./full_mani_skill_data/OpenCabinetDrawer/OpenCabinetDrawer_1035_link_0-v0.h5',
    #'./full_mani_skill_data/OpenCabinetDrawer/OpenCabinetDrawer_1040_link_0-v0.h5',
    #'./full_mani_skill_data/OpenCabinetDrawer/OpenCabinetDrawer_1061_link_0-v0.h5',
    './full_mani_skill_data/OpenCabinetDrawer/OpenCabinetDrawer_1066_link_0-v0.h5',
    './full_mani_skill_data/OpenCabinetDrawer/OpenCabinetDrawer_1082_link_0-v0.h5',


    # Door environmentswith cabinet present at least once in both drawer and door
    './full_mani_skill_data/OpenCabinetDoor/OpenCabinetDoor_1000_link_0-v0.h5',
    './full_mani_skill_data/OpenCabinetDoor/OpenCabinetDoor_1000_link_1-v0.h5',
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

    # environments with at least 2 doors
    './full_mani_skill_data/OpenCabinetDoor/OpenCabinetDoor_1007_link_0-v0.h5',
    './full_mani_skill_data/OpenCabinetDoor/OpenCabinetDoor_1007_link_1-v0.h5',
    './full_mani_skill_data/OpenCabinetDoor/OpenCabinetDoor_1018_link_0-v0.h5',
    './full_mani_skill_data/OpenCabinetDoor/OpenCabinetDoor_1018_link_1-v0.h5',
    './full_mani_skill_data/OpenCabinetDoor/OpenCabinetDoor_1034_link_0-v0.h5',
    './full_mani_skill_data/OpenCabinetDoor/OpenCabinetDoor_1034_link_1-v0.h5',
    './full_mani_skill_data/OpenCabinetDoor/OpenCabinetDoor_1036_link_0-v0.h5',
    './full_mani_skill_data/OpenCabinetDoor/OpenCabinetDoor_1036_link_1-v0.h5',
    './full_mani_skill_data/OpenCabinetDoor/OpenCabinetDoor_1060_link_2-v0.h5',
    './full_mani_skill_data/OpenCabinetDoor/OpenCabinetDoor_1060_link_3-v0.h5',

    #other Door
    #'./full_mani_skill_data/OpenCabinetDoor/OpenCabinetDoor_1001_link_0-v0.h5',
    #'./full_mani_skill_data/OpenCabinetDoor/OpenCabinetDoor_1002_link_0-v0.h5',
    #'./full_mani_skill_data/OpenCabinetDoor/OpenCabinetDoor_1006_link_0-v0.h5',
    #'./full_mani_skill_data/OpenCabinetDoor/OpenCabinetDoor_1014_link_0-v0.h5',
    #'./full_mani_skill_data/OpenCabinetDoor/OpenCabinetDoor_1017_link_0-v0.h5',
    #'./full_mani_skill_data/OpenCabinetDoor/OpenCabinetDoor_1025_link_1-v0.h5',
    #'./full_mani_skill_data/OpenCabinetDoor/OpenCabinetDoor_1026_link_0-v0.h5',
    #'./full_mani_skill_data/OpenCabinetDoor/OpenCabinetDoor_1028_link_0-v0.h5',
    #'./full_mani_skill_data/OpenCabinetDoor/OpenCabinetDoor_1030_link_0-v0.h5',
    #'./full_mani_skill_data/OpenCabinetDoor/OpenCabinetDoor_1031_link_0-v0.h5',
    #'./full_mani_skill_data/OpenCabinetDoor/OpenCabinetDoor_1039_link_0-v0.h5',
    #'./full_mani_skill_data/OpenCabinetDoor/OpenCabinetDoor_1041_link_0-v0.h5',
    #'./full_mani_skill_data/OpenCabinetDoor/OpenCabinetDoor_1046_link_0-v0.h5',
    #'./full_mani_skill_data/OpenCabinetDoor/OpenCabinetDoor_1047_link_0-v0.h5',
    #'./full_mani_skill_data/OpenCabinetDoor/OpenCabinetDoor_1049_link_0-v0.h5',
    #'./full_mani_skill_data/OpenCabinetDoor/OpenCabinetDoor_1051_link_0-v0.h5',
    #'./full_mani_skill_data/OpenCabinetDoor/OpenCabinetDoor_1057_link_0-v0.h5',
    #'./full_mani_skill_data/OpenCabinetDoor/OpenCabinetDoor_1062_link_0-v0.h5',
    #'./full_mani_skill_data/OpenCabinetDoor/OpenCabinetDoor_1065_link_0-v0.h5',
    #'./full_mani_skill_data/OpenCabinetDoor/OpenCabinetDoor_1068_link_0-v0.h5',
    #'./full_mani_skill_data/OpenCabinetDoor/OpenCabinetDoor_1073_link_0-v0.h5',
    './full_mani_skill_data/OpenCabinetDoor/OpenCabinetDoor_1077_link_0-v0.h5',
    './full_mani_skill_data/OpenCabinetDoor/OpenCabinetDoor_1081_link_0-v0.h5',

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
