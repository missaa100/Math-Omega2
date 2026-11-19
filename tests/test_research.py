from mathomega import research

def test_finds_counterexample():
    result = research.test_conjecture(
        "test", "all integers are odd", range(1, 5),
        predicate=lambda n: n % 2 == 1,
        conjecture=lambda n: True,
    )
    assert result.status == "counterexample_found"
    assert result.counterexamples[0]["input"] == 2
