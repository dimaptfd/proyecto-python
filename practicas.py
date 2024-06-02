camepers= [
        {
            "19038932": {
                "nombres": "Daniela",
                "apellidos": "Gaviria",
                "documento": 19038932,
                "direccion": "juan #67-3",
                "num_tel": 43753985
            }
        },
        {
            "876543": {
                "nombres": "Fsadjkf",
                "apellidos": "Fsgsrstv",
                "documento": 876543,
                "direccion": "g43",
                "num_tel": 56536452
            }
        },
        {
            "123456789": {
                "nombres": "Carolina",
                "apellidos": "Montero",
                "documento": 123456789,
                "direccion": "fsa6",
                "num_tel": 6765434
            }
        },
        {
            "766456788": {
                "nombres": "Laura Marcela",
                "apellidos": "Gaitan Montero",
                "documento": 766456788,
                "direccion": "calle 45 #f76",
                "num_tel": 12345678
            }
        },
        {
            "7867657": {
                "nombres": "Jhfalskf",
                "apellidos": "Sdgdfg",
                "documento": 7867657,
                "direccion": "hdsgf7a6",
                "num_tel": 67565456
            }
        },
        {
            "123": {
                "nombres": "Cameron",
                "apellidos": "Jomson",
                "documento": 123,
                "direccion": "123",
                "num_tel": 234567
            }
        }
]
documento = int(input("ingrese numero de indentidad: "))
if documento in camepers:

 print(camepers[documento]["estado"])