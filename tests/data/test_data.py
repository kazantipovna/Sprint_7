from datetime import datetime, timedelta

register_field_missed = [("Login_no_Name", "Pass_no_Name", ""),
                         ("Login_no_Pass", "", "Name_no_Pass"),
                         ("", "Pass_no_Login", "Name_no_Login")]

register_ok = ["VasiaPupkin", "1qa2ws3ed", "VasiaPupkin"]

order_data = {"firstName": "Вася",
              "lastName": "Пупкин",
              "address": "Красная 1",
              "metroStation": "Охотный ряд",
              "phone": "+79108888666",
              "rentTime": 2,
              "deliveryDate": (datetime.now().date() + timedelta(days=2)).strftime('%Y-%m-%d'),
              "comment": "Позвонить в домофон",
              "color": []}
