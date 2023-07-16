class Vacancy:

    def __init__(self, id, title, area, employer, url, salary_from, salary_to, currency):
        self.id = id
        self.title = title
        self.area = area
        self.employer = employer
        self.url = url
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.currency = currency

    def __str__(self):
        if self.currency is None:
            return f"""
Vacancy id: {self.id}.
Job title: {self.title}.
City: {self.area}.
Employer: {self.employer}.
Salary: {self.salary_from} --> {self.salary_to}
Link: {self.url}"""
        else:
            return f"""
Vacancy id: {self.id}.
Job title: {self.title}
City: {self.area}.
Employer: {self.employer}.
Salary: {self.salary_from} {self.currency} --> {self.salary_to} {self.currency}
Link: {self.url}."""

