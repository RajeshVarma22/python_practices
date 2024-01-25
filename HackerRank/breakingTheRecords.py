
def breakingRecords(scores):
    # Write your code here

    highest_score = scores[0]
    lowest_score = scores[0]

    highest_score_break_count = 0
    lowest_score_break_count = 0

    for i in scores:
        if(i > highest_score):
            highest_score_break_count += 1
            highest_score = i
        if(i < lowest_score):
            lowest_score = i
            lowest_score_break_count += 1


    return [highest_score_break_count, lowest_score_break_count]

scores = [3 ,4,21, 36, 10, 28, 35, 5, 24, 42]

res = breakingRecords(scores)

print(res)
