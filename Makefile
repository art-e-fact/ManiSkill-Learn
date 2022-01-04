submission:
	for env in OpenCabinetDrawer OpenCabinetDoor PushChair MoveBucket ; do\
		git archive -o submission_$$env.zip HEAD ; \
		cp config_$$env.yml conf.yml ; \
		zip -ur submission_$$env.zip models/*.ckpt conf.yml ; \
	done

