def age_check(df):
    errors = df["Age"][(df["Age"] > 150) | (df["Age"] < 0)].shape[0]
    return errors, "Checking if age is in range 0-150"


def age_check2(df):
    n = df.shape[0]
    errors = 0
    for i in range(n):
        if df["Age"][i] < df["yearsmarried"][i]:
            errors += 1
    return errors, "Checking if age is greater than years married"


def status_check(df):
    errors = df.shape[0] - df[df["status"].isin(['single', 'married', 'widowed'])].shape[0]
    return errors, "Checking if status contains values only from single, married, widowed"


def agegroup_check(df):
    n = df.shape[0]
    errors = 0
    for i in range(n):
        if df["Age"][i] < 18 and df["agegroup"][i] != "child":
            errors += 1
        elif df["Age"][i] >= 18 and df["Age"][i] < 65 and df["agegroup"][i] != "adult":
            errors += 1
        elif df["Age"][i] >= 65 and df["agegroup"][i] != "elderly":
            errors += 1
    return errors, "Checking if age group lies correctly according to age"
