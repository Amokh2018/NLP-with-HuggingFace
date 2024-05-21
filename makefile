install:
	@echo "install requirements in HF_SA_MLOps";\
    . ./HF_SA_MLOps/bin/activate; \
    pip install -r requirements.txt;
init:
	@echo "Creating Python virtual environment 'HF_SA_MLOps'"; \
	python3 -m venv ./HF_SA_MLOps; \
	@echo "Activating Python virtual environment 'HF_SA_MLOps'"; \
	. ./HF_SA_MLOps/bin/activate; \
	@echo "Installing requirements"; \
	pip install -r requirements.txt; \
	echo "Initialization complete"


run: 
	python3 ./summarize/webapp/app.py
# add the command to run the webapp
test-gen:
	python3 ./summarize/try_generate.py
test-sum:
	python3 ./summarize/try_summarize.py	
# add the command to run the try summarise and generate apps
build:
	docker build -t genapp:v1 . 
# add the command to build the docker image
build-push:

# add the command to build the docker image and push it the the ECR

.PHONY:  init 
