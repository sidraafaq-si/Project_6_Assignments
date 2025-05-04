class Bank:
    bank_name = "Default Bank"

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name
