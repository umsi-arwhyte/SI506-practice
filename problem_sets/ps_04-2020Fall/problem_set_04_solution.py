# START PROBLEM SET 04
print('Problem Set 04')

# START SET UP
summary = [
    'Step 1: Beat It',
    'Step 2: Prep the Pan',
    'Step 3: Add the Eggs',
    'Step 4: Patience Makes Perfect',
    'Step 5: Almost Done',
    'Step 6: Ready to Eat'
]
recipe = [
    "Beat your eggs until they're completely blended. Add a little water, cream or milk to make them tender. Use 1 tablespoon of liquid per egg. Add a pinch of salt.",
    "Next, heat a nonstick skillet over a medium-low flame and toss in a pat of butter. Make sure the butter coats the pan.",
    "Then, pour in the eggs. Pause to let them heat slightly — gentle heat is essential.",
    "Move the eggs across the pan like a bulldozer so the eggs cook evenly. This takes a little time, but it's worth it.",
    "As the eggs start to set, add chopped fresh herbs, or bits of ham or cheese.",
    "Turn your eggs onto warmed plates and dig in! Watch our how-to video for more."
]

# Problem 01
print('\nProblem 1')

step_length = []
for step in recipe:
    step_length.append(len(step))

print(step_length)

gte_100 = 0
less_100 = 0
for l in step_length:
    if l > 100:
        gte_100 += 1
    elif l < 100:
        less_100 += 1
print(gte_100, less_100)

step_25_mins = 0
for l in step_length[1:5]:
    if l > 100:
        step_25_mins += 10
    elif l < 100:
        step_25_mins += 5
print(step_25_mins)

# Problem 02
print('\nProblem 2')

step_order_3 = summary[2][:6].upper().replace(' ', '')
print(step_order_3)

recipe_summary_3 = f"{step_order_3}: {recipe[2]}"
print(recipe_summary_3)

recipe_summary = []
for i, s in enumerate(summary):
    recipe_summary.append(f"{s[:6].upper().replace(' ', '')}: {recipe[i]}")
print(recipe_summary)

# Problem 03
print('\nProblem 3')
step2_r_num = 0
for c in recipe[1]:
    if c == "r":
        step2_r_num += 1
print(step2_r_num)

step_r_num = []
for step in recipe:
    r_num = 0
    for c in step:
        if c == "r":
            r_num += 1
    step_r_num.append(r_num)
print(step_r_num)

max_r_index = -1
max_r_num = -1
for num in step_r_num:
    if num > max_r_num:
        max_r_num = num
        max_r_index = step_r_num.index(max_r_num)
print(max_r_index, max_r_num)
