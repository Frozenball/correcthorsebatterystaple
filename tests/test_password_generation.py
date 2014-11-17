import correcthorsebatterystaple

def test_password_generation():
    assert len(
        correcthorsebatterystaple.generate_password(5).split(" ")
    ) == 5
