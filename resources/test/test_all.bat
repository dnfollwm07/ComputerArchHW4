python ../code/sim_dm.py first.trace 16 1 4
python ../code/sim_dm.py first.trace 16 1 8
python ../code/sim_dm.py pingpong.trace 16 1 4
python ../code/sim_sa.py pingpong.trace 16 2 4
python ../code/sim_sa.py test_q.trace 64 2 4
python ../code/sim_sa.py sa.trace  64 2 8
python ../code/sim_dm.py dm_a.trace 64 1 4
python ../code/sim_dm.py dm_b.trace 64 1 8