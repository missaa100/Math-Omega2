# MathOmega — iPhone / iPad Cloud Development Starter

This project is designed to be opened in **GitHub Codespaces** from Safari.
The iPhone/iPad is the control surface; compilation and computation run in a
remote Linux container.

## Included
- C++17 compute-core starter
- Python research harness
- SymPy for symbolic mathematics
- .venv/bin/pytest for automated tests
- CMake and VS Code web extensions
- JSONL experiment log in `data/experiments.jsonl`

## Set up from iPhone/iPad
1. Sign in to GitHub in Safari and create a **new empty repository**.
2. Upload the contents of this project ZIP to the repository (or upload the
   extracted files using GitHub's web interface).
3. Open the repository on GitHub.
4. Select **Code → Codespaces → Create codespace on main**.
5. Wait for the container to build. Open the integrated terminal.

## First commands in the Codespaces terminal

```bash
cmake -S . -B build
cmake --build build
./build/mathomega_cpp
```

Run the Python experiment:

```bash
.venv/bin/python -m mathomega.research
```

Run tests:

```bash
.venv/bin/pytest
```

## Research integrity
A finite search can find counterexamples and test conjectures, but it cannot
establish a universal theorem. MathOmega must keep separate records for:
1. conjectures,
2. computational evidence,
3. proof attempts,
4. machine-checked proofs.

## Roadmap
1. Problem and conjecture registry
2. Counterexample search with configurable domains
3. Symbolic algebra and exact arithmetic
4. Proof assistant integration (Lean 4)
5. Literature ingestion with source tracking
6. A controlled research agent that proposes tasks and records reproducible runs

This is a development foundation, not an autonomous mathematician yet.
