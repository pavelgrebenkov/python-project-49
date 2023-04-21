# This is an executable file which cantains several useful commands for quick and easy use.

install:
	poetry install # This command is useful at the first instance of cloning a repository (or after deleting dependencies).

brain-games:
	poetry run brain-games # Launches the Brain Games program.

brain-even:
	poetry run brain-even # Launches the Brain Even program

brain-calc:
	poetry run brain-calc # Launches the Brain Calculator program

brain-gcd:
	poetry run brain-gcd #Launches the Brain Greatest Common Denominator program

brain-progression:
	poetry run brain-progression # Launches the Brain Progression program

brain-prime:
	poetry run brain-prime # Launches the Brain Prime program

build:
	poetry build # Assembles packages.

publish:
	poetry publish --dry-run # Used for checking and  debugging without publishing to PyPI.

lint:
	poetry run flake8 brain_games # Launches Flake 8

package-install:
	python3 -m pip install --user dist/*.whl # Installs programs from the operating system.

package-reinstall:
	python3 -m pip install --user --force-reinstall dist/*.whl # Re-installs programs from the operating system.

package-uninstall:
	python3 -m pip uninstall hexlet-code # Uninstalls the Hexlet Code project from the operating sytem.


