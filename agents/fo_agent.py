from core.reasoning_tree import ReasoningTree
from core.decision_making import majority_vote
from core.benchmarks import run_benchmark

class FoAgent:
    def __init__(self):
        self.reasoning_tree = ReasoningTree()

    def make_decision(self, votes):
        return majority_vote(votes)

    def validate_reasoning(self, benchmark):
        return run_benchmark(benchmark)
