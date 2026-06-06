class EmployeeSalary:
    hourly_payment = 400

    def __init__(self, name: str, rest_days: int, hours=None, email=None):
        self.name = name
        self.rest_days = rest_days
        self.email = email
        self.hours = hours

    @classmethod
    def get_hours(cls, name: str, rest_days: int, hours=None, email=None):
        if hours is None:
            hours = (7 - rest_days) * 8
        return cls(name, rest_days, hours, email)

    @classmethod
    def get_email(cls, name: str, rest_days: int, hours=None, email=None):
        if email is None:
            email = f"{name}@email.com"
        return cls(name, rest_days, hours, email)

    @classmethod
    def set_hourly_payment(cls, new_hourly_payment):
        cls.hourly_payment = new_hourly_payment

    def salary(self):
        return self.hourly_payment * self.hours
