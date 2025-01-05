def majority_vote(votes):
    from collections import Counter
    vote_count = Counter(votes)
    return vote_count.most_common(1)[0][0]


def expert_evaluation(experts, decision):
    # Implement expert evaluation logic here
    pass
