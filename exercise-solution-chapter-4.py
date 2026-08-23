def apply_bonus(scores, bonus):
    return [score + bonus for score in scores]

scores = [10, 20, 30]
print("Applying bonus...") # side effect, on the edge
new_scores = apply_bonus(scores, 5)
print(new_scores) # 15, 25, 35]
