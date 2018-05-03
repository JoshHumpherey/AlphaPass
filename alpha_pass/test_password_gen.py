import alpha_pass.password_gen as password_gen


def test_PasswordGen():
    expected_result = '749bd32ac64d1ceb519878e6e1925d072b8bf143eb84c035cb94caf9bc693a6f'
    master_key = '1234'
    service_name = 'Bank'
    test_password = password_gen.generate_password(master_key, service_name)
    assert test_password == expected_result
