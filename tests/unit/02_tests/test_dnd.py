import pytest
from functs_02.dnd import attack_damage

@pytest.mark.parametrize("dnd.randit", return=5, )
def test_attack_damage():
    assert attack_damage(1) == 6
