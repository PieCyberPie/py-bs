def contains_pickle(*args):
    if "pickle" in args:
        return True
    else:
        return False
print(contains_pickle("ass", "pickle", 123, [], True))

def count_fails(*args):
    failed = 0
    for score in args:
        if score <= 50:
            failed += 1
    return failed
print(count_fails(59, 49, 100, 90, 27))

def get_top_students(**kwargs):
    top_students = []
    for k, w in kwargs.items():
        if w >= 90:
            top_students.append(k)
    return top_students
print(get_top_students(mike=92, daniel=60, anya=100))