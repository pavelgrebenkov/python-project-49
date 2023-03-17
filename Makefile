# This is an executable file which cantains several useful programs

install:
	poetry install # This command is useful at the first instance of repository cloning (or after deleting the dependencies).


brain-games:
	poetry run brain-games # Launches the Brain Games program.


build:
	poetry build # Puts together the package.


publish:
	poetry publish --dry-run # Used for debugging without publishing to PyPI.


package-install:
	python3 -m pip install --user dist/*.whl # Installs the program by way of the operating system.
