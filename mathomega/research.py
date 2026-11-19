"""Small, auditable starting point for computational mathematics."""
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
import json
from pathlib import Path
from typing import Callable

@dataclass
class Experiment:
    name: str
    claim: str
    tested_inputs: int
    counterexamples: list
    status: str
    timestamp_utc: str

def test_conjecture(
    name: str,
    claim: str,
    values: range,
    predicate: Callable[[int], bool],
    conjecture: Callable[[int], bool],
) -> Experiment:
    """Compare a conjecture with a predicate over a finite test range.

    A successful finite test is evidence only; it is not a proof.
    """
    counterexamples = []
    tested = 0
    for x in values:
        tested += 1
        actual = bool(predicate(x))
        predicted = bool(conjecture(x))
        if actual != predicted:
            counterexamples.append({"input": x, "actual": actual, "predicted": predicted})
    status = "counterexample_found" if counterexamples else "no_counterexample_in_test_range"
    return Experiment(
        name=name,
        claim=claim,
        tested_inputs=tested,
        counterexamples=counterexamples,
        status=status,
        timestamp_utc=datetime.now(timezone.utc).isoformat(),
    )

def save_experiment(experiment: Experiment, path="data/experiments.jsonl"):
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    with target.open("a", encoding="utf-8") as f:
        f.write(json.dumps(asdict(experiment), ensure_ascii=False) + "\\n")

def demo():
    # Example exploration: every prime greater than 2 is odd.
    from sympy import isprime
    result = test_conjecture(
        name="odd-prime-check",
        claim="For integers n from 2 through 500, if n is prime and n > 2, n is odd.",
        values=range(2, 501),
        predicate=lambda n: (not isprime(n) or n == 2 or n % 2 == 1),
        conjecture=lambda n: True,
    )
    save_experiment(result)
    print(json.dumps(asdict(result), ensure_ascii=False, indent=2))
    print("\\nNOTE: Finite computation is not a mathematical proof.")

if __name__ == "__main__":
    demo()
