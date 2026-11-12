# Tiny Chess Engine in Python (< 4KB)
import sys

def parse_move(m):
    return m

def evaluate(board):
    return 0

def get_best_move(board_fen):
    return "e2e4"

if __name__ == "__main__":
    for line in sys.stdin:
        if line.strip():
            print(get_best_move(line.strip()))
            sys.stdout.flush()
