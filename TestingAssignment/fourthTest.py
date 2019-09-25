from searchStudentPass import idNumberSearchedFor, studentIDList

def test():
    passorfail = 1
    digits = len(str(idNumberSearchedFor))

    if (digits != 5):
        passorfail = 0
        assert passorfail == 1

    if idNumberSearchedFor in studentIDList:
        numberinList = 1
    else:
        numberinList = 0
    
    assert numberinList == 1