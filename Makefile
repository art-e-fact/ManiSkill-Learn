submission:
	for env in OpenCabinetDrawer OpenCabinetDoor PushChair MoveBucket ; do\
		git archive -o submission_$$env.zip HEAD ; \
		cp config_$$env.yml config.yml ; \
		zip -d submission_$$env.zip *.ckpt ; \
		zip -ur submission_$$env.zip models/*$$env*.ckpt config.yml ; \
	done

