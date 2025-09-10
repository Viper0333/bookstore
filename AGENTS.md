# Repository Guidelines

## Project Structure & Module Organization
- Django project root: `bookstore/` (settings, urls, asgi, wsgi).
- Domain apps: `product/` and `order/` with `models/`, `serializers/`, `viewsets/`, `urls.py`, `factories.py`, `tests/`, and `migrations/`.
- Entry point: `manage.py`.
- Static assets collected under `staticfiles/` (generated; do not edit).
- Python: `>=3.11` (see `pyproject.toml`).

## Build, Test, and Development Commands
- Install (Poetry): `poetry install`
- Run server: `poetry run python manage.py runserver`
- Apply migrations: `poetry run python manage.py migrate`
- Run tests (pytest): `poetry run pytest -q`
- Type checks (mypy + django-stubs): `poetry run mypy`
- Alternative (pip): create a venv and `pip install -e .` or `pip install -r requirements.txt` if present.

## Coding Style & Naming Conventions
- Follow PEP 8; 4-space indentation; 88–100 column soft limit.
- Types: add hints to public functions; keep `mypy` green (see `mypy.ini`).
- Naming: `snake_case` for functions/variables, `PascalCase` for classes, `UPPER_SNAKE_CASE` for constants.
- Django/DRF layout: serializers in `serializers/`, viewsets in `viewsets/`, urls in `<app>/urls.py`.

## Testing Guidelines
- Framework: `pytest` with `factory_boy` for fixtures.
- Location: tests live in `<app>/tests/` (e.g., `product/tests/test_serializers/`, `order/tests/test_viewsets/`).
- Naming: modules `test_*.py`.
- Coverage: aim for ≥80% on changed code; include serializer and viewset tests.
- Run locally: `poetry run pytest -q` (use `-k` to filter).

## Commit & Pull Request Guidelines
- Commits: imperative mood, concise subject; optional scope prefix (e.g., `product: add ProductSerializer validation`).
- Include related migrations when models change.
- PRs: clear description, linked issue, checklist of changes, and test evidence (output or API screenshots where relevant). Note breaking changes explicitly.

## Security & Configuration Tips
- Do not commit secrets; use env vars read by `bookstore/settings.py`.
- For non-dev: set `DEBUG=False` and configure `ALLOWED_HOSTS`.
- Static files served via `whitenoise`; avoid editing `staticfiles/` directly.

## Agent-Specific Instructions
- Keep diffs minimal and aligned with this structure.
- Obey this AGENTS.md for all files you touch; deeper files may override with their own AGENTS.md.
- Update or add tests for any new behavior before opening a PR.
