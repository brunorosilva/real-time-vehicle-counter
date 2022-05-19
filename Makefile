.PHONY: checks format clean

# Package paths
PACKAGE_PATH=rtvc

checks:
	@poetry run flake8 rtvc
	@poetry run black --check rtvc tests
	@poetry run mypy rtvc
	@poetry run mypy ./tests/**.py
	@poetry run vulture rtvc
	@poetry run pytest tests
	@poetry run poetry check
	@poetry run safety check --full-report -i 44715

format:
	@isort *
	@poetry run black rtvc tests

clean:
	find . -type f -name '*.pyc' -delete
	-rm -rf $(PACKAGE_PATH)/lib
	-rm -rf $(PACKAGE_PATH)/*.egg-info
	-rm -rf $(PACKAGE_PATH)/.coverage
	-rm -rf $(PACKAGE_PATH)/.eggs
	-rm -rf $(PACKAGE_PATH)/.tox
	-rm -rf $(PACKAGE_PATH)/__pycache__
	-rm -rf $(PACKAGE_PATH)/cover
	-rm -rf $(PACKAGE_PATH)/dist
	-rm -rf $(PACKAGE_PATH)/spark-warehouse
	-rm -rf $(PACKAGE_PATH)/*.log
