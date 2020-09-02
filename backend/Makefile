revision:
	export PYTHONPATH=$(shell pwd) &&  python3 ./src/database/alembic/revision.py

upgrade:
	export PYTHONPATH=$(shell pwd) && python3 ./src/database/alembic/upgrade.py

downgrade:
	@alembic downgrade head

run:
	@echo "---- Running Application ----"
	@PYTHONPATH="${PYTHONPATH}" gunicorn -c ./src/utils/gunicorn.py src.app:app

release:
	@echo "Input version[$(shell git describe --abbrev=0 --tags --always)]:"
	@read INPUT_VERSION; [[ ! -z $$INPUT_VERSION ]] \
		|| INPUT_VERSION=`git describe --abbrev=0 --tags --always` \
		&& echo "__version__ = '$$INPUT_VERSION'" > `pwd`/src/__init__.py \
		&& echo "Creating a new release version: $$INPUT_VERSION" \
		&& git add `pwd`/src/__init__.py \
		&& git commit -m "new version $$INPUT_VERSION" \
		&& git tag "$$INPUT_VERSION" \
		&& git push origin "$$INPUT_VERSION" \
		&& git push origin -u "$(shell git rev-parse --abbrev-ref HEAD)"