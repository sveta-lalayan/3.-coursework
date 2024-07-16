from pprint import pprint

from scripts.scripts import load_data, five_items, correct_date, account_of_sender, account_of_recipent, \
    transfer_ammount, currency


def main():
    data = load_data()
    five_operation = five_items(data)
    for item in five_operation:
        print(f'{correct_date(item["date"])} {item.get("description")}')
        print(f'{account_of_sender(item)} -> {account_of_recipent(five_operation)}')
        print(f'{transfer_ammount(item)} {currency(item)}')
        print()







if __name__ == "__main__":
    main()