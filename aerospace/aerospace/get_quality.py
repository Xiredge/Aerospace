# A simple function that returns the quality range
# Parameter: integer, float and double
# Returns a string
def get_quality(quality):
    if quality <= 1.30:
        return "Q0-Q3"
    elif quality <= 1.50:
        return "Q4-Q5"
    elif quality <= 2.0:
        return "Q6-Q7"
    elif quality <= 2.5 or quality > 2.5:
        return "Q8-Q10"

if __name__ == "__main__":
    print(get_quality(1))
    print(get_quality(1.4))
    print(get_quality(3))