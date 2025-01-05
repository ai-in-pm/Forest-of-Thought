from core.benchmarks import run_benchmark

class BenchmarkRunner:
    def __init__(self, benchmarks):
        self.benchmarks = benchmarks

    def run_all(self):
        results = {}
        for benchmark in self.benchmarks:
            results[benchmark] = run_benchmark(benchmark)
        return results
