def checkAge(df):
    errors = df["Age"][(df["Age"] > 150) | (df["Age"] < 0)].shape[0]
    return errors, "Checking if age is between 0 and 150"


def checkAgeYearMarried(df):
    rowcount = df.shape[0]
    errors = 0
    for i in range(rowcount):
        if df["Age"][i] > df["yearsmarried"][i]:
            errors = errors + 1
    return errors, "Checking if age is greater than years married"


def checkStatus(df):
    errors = df.shape[0] - \
        df[df["status"].isin(["single", "widowed", "married"])].shape[0]
    return errors, "Checking if status column contains values single, married, widowed"


def checkAgeGroup(df):
    rowcount = df.shape[0]
    errors = 0
    for i in range(rowcount):
        if df["Age"][i] < 18 and df["agegroup"][i] != "child":
            errors = errors + 1
        elif df["Age"][i] >= 18 and df["Age"][i] < 65 and df["agegroup"][i] != "adult":
            errors = errors + 1
        elif df["Age"][i] >= 65 and df["agegroup"][i] != "elderly":
            errors = errors + 1
    return errors, "Checking if age group lies correctly according to age"
