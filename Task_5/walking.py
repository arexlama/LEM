journey = []

def forward(n=1) -> None:
    global journey
    journey += ['fw' for _ in range(n)]

def right(n=1) -> None:
    global journey
    journey += ['tr' for _ in range(n)]

def left(n=1) -> None:
    global journey
    journey += ['tl' for _ in range(n)]