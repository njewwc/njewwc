from creatAssignmentPass import assignmentid
def test():
    if len(str(assignmentid)) == 9:
        length = 1
    else:
        length = 0
    assert length == 1


