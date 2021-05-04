def get_user(name, sname, year, сity, email, tel):
    return f'{name} {sname} {year} {сity} {email} {tel}'


print(get_user(name="Petr",
               sname="IVANOV",
               year="1890",
               сity="Novgorod",
               email="petr@k.nov",
               tel="11-22-33"))
