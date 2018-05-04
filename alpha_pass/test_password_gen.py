import alpha_pass.password_gen as password_gen


def test_PasswordGen():
    expected_result = '749bd32ac64d1ceb'
    master_key = '1234'
    service_name = 'Bank'
    test_password = password_gen.generate_password(master_key, service_name)
    assert test_password == expected_result

def test_trim_password():
    expected_result = 4
    test_string = '123456'
    test_trim = password_gen.trim_password(test_string,4)
    test_result = len(test_trim)
    assert test_result == expected_result
