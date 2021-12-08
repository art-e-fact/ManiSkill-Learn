submission:
	git archive -o submission.zip HEAD
	zip -ur submission.zip models/model_50000_drawer_door.ckpt
