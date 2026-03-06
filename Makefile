.PHONY: brain-games brain-even brain-calc brain-gcd brain-progression brain-prime install lint package-build package-publish package-install package-reinstall package-uninstall package-list

# Test => only for testing CLI entry point (displays greeting)
brain-games:
	poetry run brain-games


# Launch games => for playing/testing
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


# Dependencies => environment setup
install:
	poetry install


# Lint => code quality
lint:
	poetry run flake8 brain_games


# Package => building/distributing/installing/uninstalling/listing
package-build:
	poetry build

package-publish:
	poetry publish --dry-run

package-install:
	pipx install dist/*.whl

package-reinstall:
	pipx install --force dist/*.whl

package-uninstall:
	pipx uninstall hexlet-code

# Lists packages in the current virtual environment
package-list-local:
	pip list

# Lists globally installed tools
package-list-global:
	pipx list
