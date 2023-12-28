def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):

    try:
        blocks = ip.split(".")
        if len(blocks) != 4:
            return False

        for block in blocks:
            if int(block) < 0 or int(block) > 255:
                return False
    except ValueError:
        return False

    return True


if __name__ == "__main__":
    main()
