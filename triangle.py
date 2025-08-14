
def hypot(a: float, b: float):
    """
    Compute the hypotenuese of a right triangle

    Args:
        a (float): Length of one side next to hypot
        b (float): Length of other side next to hypot

    Returns:
        float: Length of hypot

    Examples:
        hypot(3, 4) returns 5
    """
    # Check input types
    if a < 0 or b < 0:
        print("a and b must be positive")
    if a == 0 or b == 0:
        print("a and b cannot be zero")
    else:
        return (a**2 + b**2)**(0.5)
