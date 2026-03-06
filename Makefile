.PHONY: brain-games brain-even brain-calc brain-gcd brain-progression brain-prime install lint package-build package-publish package-install package-reinstall package-uninstall package-list

# Test => only for testing CLI entry point (displays greeting)
brain-games:
	uv run brain-games

# Launch games => for playing/testing
brain-even:
	uv run brain-even

brain-calc:
	uv run brain-calc

brain-gcd:
	uv run brain-gcd

brain-progression:
	uv run brain-progression

brain-prime:
	uv run brain-prime


# Dependencies => environment setup
install:
	uv sync


# Lint => code quality
lint:
	uv run ruff check brain_games


# Package => building/distributing/installing/uninstalling/listing
package-build:
	uv build

package-publish:
	uv publish --dry-run

package-install:
	uv tool install dist/*.whl
	@echo "✅ Package successfully installed"

package-reinstall:
	uv tool install --force dist/*.whl
	@echo "✅ Package successfully reinstalled"

package-uninstall:
	uv tool uninstall hexlet-code
	@echo "✅ Package successfully uninstalled"

package-list:
	uv pip list
