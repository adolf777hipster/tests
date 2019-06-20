def test_substring(full_string, substring):
    # ваша реализация, напишите assert и сообщение об ошибке
    assert substring in full_string, "expected '{}' to be substring of '{}'".format(substring, full_string)

