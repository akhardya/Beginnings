#
# Skeleton file for the Python "Bob" exercise.
#
def hey(sentence):
    if sentence[-1] == "?":
        return "Sure."
    elif sentence == "WATCH OUT!":
        return "Whoa, chill out!"
    else:
        return "Whatever."
