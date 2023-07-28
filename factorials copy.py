def get_sales():
    return [
        {
            "status": "CONFIRMED",
            "created_date": "2021-10-07T05:46:11Z",
            "sent_date": "2022-03-22T12:47:23Z",
            "items": [
                {"name": "Milk", "category": "Dairy", "amount": 2, "unit_price": 2.5},
                {
                    "name": "Yellow cheese",
                    "category": "Dairy",
                    "amount": 0.2,
                    "unit_price": 29.99,
                },
                {"name": "Beer", "category": "Drinks", "amount": 4, "unit_price": 3.99},
            ],
        },
        {
            "status": "CANCELLED",
            "created_date": "2021-10-07T05:46:11Z",
            "sent_date": None,
            "items": [
                {
                    "name": "Sausage",
                    "category": "Meat",
                    "amount": 0.3,
                    "unit_price": 39.99,
                },
                {
                    "name": "White cheese",
                    "category": "Dairy",
                    "amount": 0.25,
                    "unit_price": 9.99,
                },
                {
                    "name": "Ham",
                    "category": "Meat",
                    "amount": 0.15,
                    "unit_price": 42.99,
                },
            ],
        },
        {
            "status": "CONFIRMED",
            "created_date": "2021-04-24T22:01:54Z",
            "sent_date": None,
            "items": [
                {"name": "Ham", "category": "Meat", "amount": 0.1, "unit_price": 44.99},
                {
                    "name": "Water",
                    "category": "Drinks",
                    "amount": 6,
                    "unit_price": 1.85,
                },
            ],
        },
    ]


def _get_summaries(sales):
    total_diary = []
    total_drinks = []
    total_meet = []
    for i, el in enumerate(sales):
        if el['status'] == "CONFIRMED":
            for _el in el['items']:
                if _el["category"] == 'Dairy':
                    _diray_el_cost = _el["amount"] * _el["unit_price"]
                    total_diary.append(_diray_el_cost)
                if _el["category"] == 'Drinks':
                    _drinks_el_cost = _el["amount"] * _el["unit_price"]
                    total_drinks.append(_diray_el_cost)
                if _el["category"] == 'Meat':
                    _meet_el_cost = _el["amount"] * _el["unit_price"]
                    total_meet.append(_diray_el_cost) 
                    
            # if el['items']["category"] == "Dairy":
            #     _diray_el_cost = el['items']["amount"] * el['items']["unit_price"]
            #     total_diary.append(_diray_el_cost)
            # if el['items']["category"] == "Drinks":
            #     _drinks_el_cost = el['items']["amount"] * el['items']["unit_price"]
            #     total_drinks.append(_drinks_el_cost)
                
    return sum(total_diary), sum(total_drinks), sum(total_meet),
    #return [{"category": "Dairy", "total": 12.5}, {"category": "Meat", "total": 56.99}]
    

def get_summaries(sales):
    resp = {}
    for i, el in enumerate(sales):
        if el['status'] == "CONFIRMED":
            for _el in el['items']:
                if _el["category"] in resp:
                    resp[_el["category"]] += _el["amount"] * _el["unit_price"]
                else:
                    resp[_el["category"]] = _el["amount"] * _el["unit_price"]
    return [resp]



def main():
    # resp = {}
    # resp['i'] += 1
    # print(resp)
    sales = get_sales()
    summaries = get_summaries(sales)
    print(summaries)
    # render_summaries(summaries)


if __name__ == "__main__":
    main()
