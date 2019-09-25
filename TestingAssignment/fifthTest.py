from removeStudentPass import studentID, IdToRemove

def test():
    if IdToRemove in studentID:
        exists = 1
    else:
        exists = 0
    assert exists == 1

    length = len(str(IdToRemove))

    assert length == 5