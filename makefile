
install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt;

init:
	@echo "Creating Python virtual environment 'HF_SA_MLOps'"; \
    python3 -m venv ../ENVS/HF_SA_MLOps; \
    @echo "Activating Python virtual environment 'HF_SA_MLOps'"; \
    . ../ENVS/HF_SA_MLOps/bin/activate; \
    @echo "Installing requirements"; \
    pip install -r requirements.txt; \
    echo "Initialization complete"
		

.PHONY: install init
