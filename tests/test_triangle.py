from triangle import hypot
import math
def test_hypot():
    assert hypot(3, 4) == 5
    assert hypot(1, 1) == math.sqrt(2)
    assert hypot(2, 2) == math.sqrt(8)
    assert hypot(5, 5) == math.sqrt(50)
