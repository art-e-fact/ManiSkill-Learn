FROM 280607528988.dkr.ecr.ap-northeast-1.amazonaws.com/test_sapien:latest
ENV TZ=Asia/Tokyo
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update -y  && apt-get install -y \
  tzdata unzip git curl libglib2.0-0 \
  && rm -rf /var/lib/apt/lists/* \
  && apt-get clean
COPY ManiSkill ManiSkill
WORKDIR ManiSkill
RUN pip install --no-cache-dir -r requirements.txt && pip install --no-cache-dir -e .
RUN pip install --no-cache-dir torch==1.10.0+cu113 torchvision==0.11.1+cu113 -f https://download.pytorch.org/whl/cu113/torch_stable.html
RUN mkdir ManiSkill-Learn
WORKDIR ManSkill-Learn
COPY mani_skill_learn mani_skill_learn
COPY requirements.txt requirements.txt
COPY setup.py setup.py
RUN pip install --no-cache-dir -r requirements.txt && pip install -e .
RUN pip install --no-cache-dir neptune-client
RUN apt-get update -y  && apt-get install -y \
  ffmpeg \
  && rm -rf /var/lib/apt/lists/* \
  && apt-get clean
WORKDIR /ManiSkill
CMD ./eval.sh
