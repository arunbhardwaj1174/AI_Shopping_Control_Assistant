def evaluate_decision_rules(cost, savings, previous_purchase, days_since_last_purchase):
    score = 0
    if cost > savings * 0.5:
        score += 1
    if previous_purchase >= 3:
        score += 1
    if days_since_last_purchase < 10:
        score += 1

    if score >= 2:
        return (
            "This purchase has multiple risk factors. Review the timing, your budget, and whether you need this item now."
        )
    elif score == 1:
        return (
            "There is a mild risk of regret. Consider waiting for a sale or checking your budget again."
        )
    return "The purchase appears reasonable based on the available signals."
