# This is an executable file which cantains several useful commands.

install:
	poetry install # This command is useful at the first instance of repository cloning (or after deleting the dependencies).


brain-games:
	poetry run brain-games # Launches the Brain Games program.


build:
	poetry build # Puts together the package.


publish:
	poetry publish --dry-run # Used for debugging without publishing to PyPI.

lint:
	poetry run flake8 brain_games # Launches Flake 8

package-install:
	python3 -m pip install --user dist/*.whl # Installs the program by way of the operating system.

package-reinstall:
	python3 -m pip install --user --force-reinstall dist/*.whl # Re-installs the program by way of the operating system.

package-uninstall:
	python3 -m pip uninstall hexlet-code # Un-installs the program by way of the operating sytem.


