import pandas as pd
students = {
    "Suman":{"Maths":90,"Science":99 },
    "Vijay":{"Maths":91,"Science":95 },
}
df = pd.DataFrame(students)
# print(df.head(1))
# print(df.info())
print(df.tail(1))