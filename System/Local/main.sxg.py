
def save_data_to_file(filename, data):
    with open(filename, "w") as file:
        file.write(data)


def read_data_from_file(filename):
    with open(filename, "r") as file:
        data = file.read()
    return data

if __name__ == "__main__":
    save_data_to_file("data.sxg", "Це мої зашифровані дані.")

    data = read_data_from_file("data.sxg")
    print("Дані з файлу:", data)
