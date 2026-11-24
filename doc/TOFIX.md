# TOFIX

Findings from a code scan on 2026-10-04.

## Medium

- `src/pearson_spearman.py:33` - the comment under "calculate Pearson's correlation" is a copy of the covariance formula from line 28, not Pearson's; replace it with `pearson(X, Y) = cov(X, Y) / (stdv(X) * stdv(Y))` (mirroring the Spearman comment at lines 38-39).

## Low

- `pyproject.toml:14` - `pytest` is in the dev group but the repo has no tests and `rsconstruct.toml` has no pytest processor; drop it (or add a test for the demo).
- `pyproject.toml:23` - `mypy_path = "src:python:scripts"` names `python/` and `scripts/`, neither of which exists; reduce to `"src"`.
- `rsconstruct.toml:28` - `[processor.ruff]` and `[processor.mypy]` (line 32) include `config` in `src_dirs`, but `config/` holds only Lua files; narrow both to `["src"]`.
- `src/pearson_spearman.py:17` - commented-out alternative `data2` line is dead code; remove it or turn it into a documented second scenario (uncorrelated data).
