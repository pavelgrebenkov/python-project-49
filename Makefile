.PHONY: install brain-games brain-even brain-calc brain-gcd brain-progression brain-prime build publish lint package-install package-reinstall package-uninstall

install:
	poetry install

brain-games:
	poetry run brain-games

brain-even:
	poetry run brain-even

brain-calc:
	poetry run brain-calc

brain-gcd:
	poetry run brain-gcd

brain-progression:
	poetry run brain-progression

brain-prime:
	poetry run brain-prime

build:
	poetry build

publish:
	poetry publish --dry-run

lint:
	poetry run flake8 brain_games

# Installation commands for system-wide testing
# Use virtual environment instead for normal development
package-install:
	python3 -m pip install dist/*.whl

package-reinstall:
	python3 -m pip install --force-reinstall dist/*.whl

package-uninstall:
	python3 -m pip uninstall hexlet-code -y
