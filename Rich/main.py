from rich.console import Console
from rich.table import Table

# SIMPLE EXAMPLE
table = Table(title="People")
rows = [
    ["John", "Doe", "45"],
    ["Jane", "Doe", "32"],
    ["Mary", "Smith", "25"],
]
columns = ["First Name", "Last Name", "Age"]

for column in columns:
    table.add_column(column)

for row in rows:
    table.add_row(*row, style='bright_green')

console = Console()
console.print(table)


# PANDAS EXAMPLE
import pandas as pd

df = pd.read_csv('https://people.sc.fsu.edu/~jburkardt/data/csv/grades.csv', skipinitialspace = True,quotechar='"')
#drop column ssn from df
df.drop(columns=['SSN'], inplace=True)

table = Table(title="Grades")
rows = df.values.tolist()
rows = [[str(el) for el in row] for row in rows]
columns = df.columns.tolist()

for column in columns:
    table.add_column(column)

for row in rows:
    table.add_row(*row, style='bright_green')

console = Console()
console.print(table)
