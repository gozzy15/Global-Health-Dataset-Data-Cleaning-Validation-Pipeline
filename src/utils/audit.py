import pandas as pd

def basic_information(df):
    """
    Display basic information about the dataset.
    """

    print("=" * 70)
    print("DATASET INFORMATION")
    print("=" * 70)

    print(f"Rows    : {df.shape[0]:,}")
    print(f"Columns : {df.shape[1]}")

    print("\nData Types")

    print(df.dtypes)

    print("\nMemory Usage")

    memory = df.memory_usage(deep=True).sum() / 1024**2

    print(f"{memory:.2f} MB")

def missing_values(df):
    """
    Report missing values.
    """

    print("\n" + "=" * 70)
    print("MISSING VALUES")
    print("=" * 70)

    missing = df.isna().sum()

    missing = missing[missing > 0]

    if missing.empty:
        print("No missing values found.")
        return

    report = pd.DataFrame({
        "Missing": missing,
        "Percent": (
            missing / len(df) * 100
        ).round(2)
    })

    print(report.sort_values(
        by="Missing",
        ascending=False
    ))

def duplicate_rows(df):
    """
    Report duplicate rows.
    """

    duplicates = df.duplicated().sum()

    print("\n" + "=" * 70)
    print("DUPLICATES")
    print("=" * 70)

    print(f"Duplicate rows: {duplicates}")

def missing_by_country(df):
    """
    Show which countries contain missing values.
    """

    print("\n" + "=" * 70)
    print("MISSING VALUES BY COUNTRY")
    print("=" * 70)

    report = (
        df[df.isna().any(axis=1)]
        .groupby("Country")
        .size()
        .sort_values(ascending=False)
    )

    print(report)

def missing_by_disease(df):
    """
    Show which diseases contain missing values.
    """

    print("\n" + "=" * 70)
    print("MISSING VALUES BY DISEASE")
    print("=" * 70)

    report = (
        df[df.isna().any(axis=1)]
        .groupby("Disease Name")
        .size()
        .sort_values(ascending=False)
    )

    print(report)

def missing_by_year(df):
    """
    Show which years contain missing values.
    """

    print("\n" + "=" * 70)
    print("MISSING VALUES BY YEAR")
    print("=" * 70)

    report = (
        df[df.isna().any(axis=1)]
        .groupby("Year")
        .size()
        .sort_values(ascending=False)
    )

    print(report)

def missing_by_treatment(df):
    """
    Show which treatment categories contain missing values.
    """

    print("\n" + "=" * 70)
    print("MISSING VALUES BY TREATMENT TYPE")
    print("=" * 70)

    report = (
        df[df.isna().any(axis=1)]
        .groupby("Treatment type")
        .size()
        .sort_values(ascending=False)
    )

    print(report)

def analyze_missing_patterns(df):
    """
    Analyze how missing values occur together.

    This helps determine whether missing values are:
        - random
        - grouped
        - suitable for rule-based imputation
    """

    print("\n" + "=" * 70)
    print("MISSINGNESS PATTERN ANALYSIS")
    print("=" * 70)

    # Create True/False matrix
    missing_matrix = df.isna()

    # Convert each row's missing pattern into a tuple
    patterns = (
        missing_matrix
        .apply(lambda row: tuple(row), axis=1)
        .value_counts()
    )

    print("\nTop Missingness Patterns:\n")

    for pattern, count in patterns.head(10).items():

        missing_columns = [
            col
            for col, missing
            in zip(df.columns, pattern)
            if missing
        ]

        if missing_columns:
            print(f"{count:>5} rows -> {missing_columns}")
        else:
            print(f"{count:>5} rows -> No missing values")

def run_audit(df, metadata):

    print("\n")

    print("=" * 70)
    print("DATA AUDIT REPORT")
    print("=" * 70)

    print(metadata)

    basic_information(df)

    missing_values(df)

    duplicate_rows(df)

    missing_by_country(df)

    missing_by_disease(df)

    missing_by_year(df)

    missing_by_treatment(df)

    analyze_missing_patterns(df)