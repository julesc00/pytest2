import sample_module


"""
Monkey patching
"""


def get_sample_data() -> dict:
    return {"user": "jemima123", "id": 12345}


if __name__ == "__main__":
    print("Before:", sample_module.get_data())
    get_data = get_sample_data
    print("After", get_data())
