#####################################################################
# Jan Berglund
#
# Exam
#
#####################################################################


# Function "fun_chest" to use when a "chest" has been found on the
# grid.
# If a key is in inventory, score adds, chest goes to inventory and
# is cleared from the grid.
# If no key in inventory, info only.
def fun_chest(score, inventory, maybe_item):
    if "key" in inventory:
        score += maybe_item.value
        str_print = (f"You found a {maybe_item.name}, +{maybe_item.value} points. "
                      f"One key has been used and is now consumed.")
        inventory.remove("key")
        clear = True
        return(score, str_print, clear, inventory)
    else:
        score = score
        str_print = (f"You found a {maybe_item.name}, but you had no key.")
        clear = False
        return (score, str_print, clear, inventory)


# Function "fun_trap" to use when a "trap" has been found on the
# grid.
# 10 points deducted if player has more than 10 points, or if
# negative values are allowed.
# Else if less than 10 points, and not negative allowed,
# zeroes the score.
def fun_trap(score, maybe_item, neg_values):
    str_print = (f"Oh no, it is a {maybe_item.name}!")
    if score >= 10 or neg_values:
        score += maybe_item.value
    else:
        score = 0
    return (score, str_print)

