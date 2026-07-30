class InvalidError(Exception): pass

def bill (flavour, cups):
    menu = {
        "masala": 20,
        "ginger": 40
    }

    try:
        if flavour not in menu:
            raise InvalidError("Chai is not available")
        if not isinstance(cups, int):
            raise TypeError("number of cups must be an integer")
        total = menu[flavour] * cups
        print(f"Your bill for {cups} cups of {flavour} chai: {total}")
    except Exception as e:
        print("Error: ", e)
    finally:
        print("thank you for visit")


bill("mint", 2)
bill("masala", "three")
bill("ginger", 4)