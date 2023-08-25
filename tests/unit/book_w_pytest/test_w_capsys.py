

def greet(name):
    print(f"hi {name}")


def test_greet(capsys):
    greet("Earthling")
    out, err = capsys.readouterr()
    assert out == "hi Earthling\n"
    assert err == ""

    greet("Jemima")
    greet("Benito")
