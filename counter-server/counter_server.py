from counter import Counter

class CounterImpl(Counter):
    def __init__(self, state_path: str) -> None:
        self.state_path = state_path
    def increment(self, delta: int) -> int:
        try:
            with open(self.state_path, 'r') as f:
                state = int(f.read() or '0')
        except FileNotFoundError:
            state = 0
        state += delta
        with open(self.state_path, 'w') as f:
            f.write(str(state))
        return state
