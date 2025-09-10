def create_superuser():
    from . import createsu
    try:
        createsu.run()
    except Exception as e:
        print("Erro ao criar superusuário:", e)

create_superuser()
