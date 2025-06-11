#!/usr/bin/env python3
"""Simple self-modifying neural network example.

This program implements a minimal neural network from scratch without using
external numerical libraries.  The network learns character level patterns of
its own source code and then generates new text which is saved as a new Python
module.

The implementation is intentionally small and educational rather than
state‑of‑the‑art.  It demonstrates basic gradient‑descent training and a very
lightweight visualization of the training loss.
"""

from __future__ import annotations

import math
import random
from pathlib import Path
from typing import Dict, List, Tuple


def read_self() -> str:
    """Return the contents of this source file."""
    return Path(__file__).read_text()


# ---------------------------------------------------------------------------
# Data utilities
# ---------------------------------------------------------------------------

def build_vocab(text: str) -> Tuple[Dict[str, int], Dict[int, str]]:
    """Return character to index and index to character mappings."""
    chars = sorted(set(text))
    c2i = {c: i for i, c in enumerate(chars)}
    i2c = {i: c for c, i in c2i.items()}
    return c2i, i2c


def one_hot(index: int, size: int) -> List[float]:
    """Return a one‑hot encoded vector of length ``size``."""
    vec = [0.0] * size
    vec[index] = 1.0
    return vec


def softmax(vec: List[float]) -> List[float]:
    m = max(vec)
    exps = [math.exp(v - m) for v in vec]
    s = sum(exps)
    return [e / s for e in exps]


def cross_entropy(pred: List[float], target: int) -> float:
    return -math.log(max(pred[target], 1e-12))


# ---------------------------------------------------------------------------
# Simple two layer network: input -> hidden -> output
# ---------------------------------------------------------------------------

class Net:
    def __init__(self, input_size: int, hidden_size: int, lr: float = 0.1) -> None:
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = input_size
        self.lr = lr

        self.w1 = [[self._rand() for _ in range(input_size)] for _ in range(hidden_size)]
        self.b1 = [0.0 for _ in range(hidden_size)]
        self.w2 = [[self._rand() for _ in range(hidden_size)] for _ in range(self.output_size)]
        self.b2 = [0.0 for _ in range(self.output_size)]

    def _rand(self) -> float:
        return random.uniform(-0.1, 0.1)

    def forward(self, x: List[float]) -> Tuple[List[float], List[float]]:
        hidden_raw = [sum(w * x_i for w, x_i in zip(row, x)) + b for row, b in zip(self.w1, self.b1)]
        hidden = [math.tanh(h) for h in hidden_raw]
        out_raw = [sum(w * h for w, h in zip(row, hidden)) + b for row, b in zip(self.w2, self.b2)]
        out = softmax(out_raw)
        self._cache = (x, hidden, out)
        return hidden, out

    def backward(self, target_idx: int) -> None:
        x, hidden, out = self._cache

        # output gradients
        d_out = out[:]
        d_out[target_idx] -= 1.0

        # gradients for w2 and b2
        for i in range(self.output_size):
            for j in range(self.hidden_size):
                self.w2[i][j] -= self.lr * d_out[i] * hidden[j]
            self.b2[i] -= self.lr * d_out[i]

        # backprop into hidden layer
        d_hidden = [0.0 for _ in range(self.hidden_size)]
        for j in range(self.hidden_size):
            for i in range(self.output_size):
                d_hidden[j] += self.w2[i][j] * d_out[i]
            d_hidden[j] *= (1 - hidden[j] ** 2)  # tanh derivative

        for j in range(self.hidden_size):
            for k in range(self.input_size):
                self.w1[j][k] -= self.lr * d_hidden[j] * x[k]
            self.b1[j] -= self.lr * d_hidden[j]


# ---------------------------------------------------------------------------
# Training and generation
# ---------------------------------------------------------------------------

class Trainer:
    def __init__(self, text: str, hidden_size: int = 64, lr: float = 0.1) -> None:
        self.text = text
        self.c2i, self.i2c = build_vocab(text)
        self.data = [self.c2i[c] for c in text]
        self.net = Net(len(self.c2i), hidden_size, lr)

    def train(self, epochs: int = 5) -> List[float]:
        losses = []
        for ep in range(1, epochs + 1):
            total = 0.0
            for i in range(len(self.data) - 1):
                x_idx = self.data[i]
                y_idx = self.data[i + 1]
                _, out = self.net.forward(one_hot(x_idx, self.net.input_size))
                loss = cross_entropy(out, y_idx)
                total += loss
                self.net.backward(y_idx)
            avg = total / (len(self.data) - 1)
            losses.append(avg)
            self._visualize(ep, avg)
        return losses

    def _visualize(self, epoch: int, loss: float) -> None:
        bar = "#" * max(1, int(50 * (1 - min(loss, 5) / 5)))
        print(f"Epoch {epoch:2d} | loss {loss:.4f} {bar}")

    def sample(self, length: int = 200, seed: str = "\n") -> str:
        idx = self.c2i.get(seed[-1], random.randrange(self.net.input_size))
        out_chars = [seed[-1]]
        for _ in range(length):
            _, probs = self.net.forward(one_hot(idx, self.net.input_size))
            idx = self._sample_from_dist(probs)
            out_chars.append(self.i2c[idx])
        return "".join(out_chars)

    def _sample_from_dist(self, dist: List[float]) -> int:
        r = random.random()
        total = 0.0
        for i, p in enumerate(dist):
            total += p
            if total > r:
                return i
        return len(dist) - 1


# ---------------------------------------------------------------------------
# Putting it together
# ---------------------------------------------------------------------------

def main() -> None:
    source = read_self()
    trainer = Trainer(source)
    losses = trainer.train(epochs=5)

    generated = trainer.sample(len(source))
    out_file = Path(__file__).with_name("neural_self_mod_generated.py")
    out_file.write_text(generated)

    print(f"\nGenerated code written to {out_file}")
    print("Training losses:")
    for i, loss in enumerate(losses, 1):
        print(f" epoch {i:2d}: {loss:.4f}")


if __name__ == "__main__":
    main()
