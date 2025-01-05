from agents.fo_agent import FoAgent

if __name__ == '__main__':
    agent = FoAgent()
    votes = ['A', 'B', 'A', 'C', 'A']
    decision = agent.make_decision(votes)
    print(f'Decision made: {decision}')
    benchmark_result = agent.validate_reasoning('GSM8K')
    print(f'Benchmark result: {benchmark_result}')
