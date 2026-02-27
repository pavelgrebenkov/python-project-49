.PHONY: install brain-games brain-even brain-calc brain-gcd brain-progression brain-prime build publish lint package-install package-reinstall package-uninstall

install:
	uv sync

brain-games:
	uv run brain-games

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

build:
	uv build

publish:
	uv publish --dry-run

lint:
	uv run ruff check brain_games

# Installation commands for system-wide testing
# Make sure you're working in an activated virtual environment
package-install:
	uv pip install dist/*.whl

package-reinstall:
	uv pip install --force-reinstall dist/*.whl

package-uninstall:
	uv pip uninstall hexlet-code -y

# Clean everything
package-clean:
	rm -rf dist/ build/ *.egg-info
	uv pip uninstall hexlet-code -y 2>/dev/null || true

# Full reinstall from scratch
package-reinstall-clean: package-clean build
	uv pip install dist/*.whl
	@echo "✅ Clean reinstall complete"

# Show what's installed
package-list:
	uv pip list
