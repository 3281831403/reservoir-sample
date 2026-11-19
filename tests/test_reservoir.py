import pytest

from probabilistic import reservoir as mod

CASES = [
    ('lcg', [1], 1103527590, False),
    ('lcg', [0], 12345, False),
    ('sample_indices', [10, 3, 7], [1, 7, 9], False),
    ('sample_indices', [3, 5, 1], [0, 1, 2], False),
    ('reservoir', [['a', 'b', 'c'], 2, 3], ['a', 'c'], False),
    ('probability', [3, 10], 0.3, True),
    ('probability', [0, 0], 0.0, True),
    ('merge_samples', [[1, 2], [3, 4], 2, 5], [1, 2], False),
    ('lcg', [42], 1250496027, False),
    ('sample_indices', [0, 0, 1], [], False),
    ('sample_indices', [5, 0, 2], [], False),
    ('reservoir', [[], 2, 1], [], False),
    ('probability', [1, 3], 0.3333333333333333, True),
    ('merge_samples', [[], [], 2, 1], [], False),
    ('reservoir', [[1], 1, 1], [1], False),
]


@pytest.mark.parametrize("func_name,args,expected,approx", CASES)
def test_reservoir_contract(func_name, args, expected, approx):
    func = getattr(mod, func_name)
    result = func(*args)
    if approx:
        assert result == pytest.approx(expected)
    else:
        assert result == expected
