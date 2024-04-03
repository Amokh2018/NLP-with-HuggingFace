install:
	@echo "install requirements ins HF_SA_MLOps";\
    . ../ENVS/HF_SA_MLOps/bin/activate; \
    pip install -r requirements.txt;
init:
	@echo "Creating Python virtual environment 'HF_SA_MLOps'"; \
	python3 -m venv ../ENVS/HF_SA_MLOps; \
	@echo "Activating Python virtual environment 'HF_SA_MLOps'"; \
	. ../ENVS/HF_SA_MLOps/bin/activate; \
	@echo "Installing requirements"; \
	pip install -r requirements.txt; \
	echo "Initialization complete"


run: 
# add the command to run the webapp
test:
# add the command to run the try summarise and generate apps
build:
# add the command to build the docker image
build-push:
# add the command to build the docker image and push it the the ECR

.PHONY:  init 
