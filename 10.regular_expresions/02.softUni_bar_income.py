import re

def bar_closing():
    clients_list = []
    total_income = 0
    while True:
        info = input()
        if info == "end of shift":
            break

        regex = r".*?%(?P<client>[A-Z][a-z]+)%.*?<(?P<product>\w+)>.*?\|(?P<count>[0-9]+)\|.*?(?P<price>[0-9]+[\.]?[0-9]+)\$.*?"
        matches = re.finditer(regex, info)
        if matches:
            for match in matches:
                client = match.group("client")
                product = match.group("product")
                count = int(match.group("count"))
                price = float(match.group("price"))

                bill_payed = count * price
                total_income += bill_payed

                clients_list.append(client)
                clients_list.append(product)
                clients_list.append(bill_payed)

    for i in range(0, len(clients_list)-2, 3):
        print(f"{clients_list[i]}: {clients_list[i+1]} - {clients_list[i+2]:.2f}")
    print(f"Total income: {total_income:.2f}")


bar_closing()
