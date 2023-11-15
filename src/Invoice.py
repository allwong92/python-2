from dataclasses import dataclass

@dataclass(frozen = False, order = True)

class Invoice:
    invoice_id: int
    user_id: int
    amount: float
    paid: str

    def __repr__(self):
        return f"Invoice(invoice_id='{self.invoice_id}', user_id='{self.user_id}', amount='{self.amount}', paid='{self.paid}') \n"