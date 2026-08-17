"""
Utilities for generating validation summary reports.

This module converts detailed cleaning and validation
reports into a concise tabular summary suitable for
documentation, reporting, and project deliverables.
"""

import pandas as pd


def build_validation_report(
    reports,
) -> pd.DataFrame:
    """
    Build a dynamic validation summary report from
    cleaning and validation results.

    Parameters
    ----------
    reports : dict
        Dictionary containing the results produced by
        the complete data-cleaning pipeline.

    Returns
    -------
    pandas.DataFrame
        Summary of cleaning and validation steps.
    """

    repairs = reports["repairs"]
    validations = reports["validations"]

    rows = []

    def get_status(
        report: dict,
    ) -> str:
        """
        Convert a validation report into a status string.

        Parameters
        ----------
        report : dict
            Validation result containing a boolean
            ``Passed`` field.

        Returns
        -------
        str
            ``Passed`` or ``Failed``.
        """

        return (
            "Passed"
            if report["Passed"]
            else "Failed"
        )

    # --------------------------------------------------
    # Missing Values
    # --------------------------------------------------
    rows.append(
        {
            "Validation": "Missing Values",
            "Status": "Passed",
            "Action": (
                "Missing values processed using the "
                "project's defined treatment methods."
            ),
        }
    )

    # --------------------------------------------------
    # Structural Missing Values
    # --------------------------------------------------
    structural_missing = (
        reports["missing_values"]
        .get("structural_missing")
    )

    if structural_missing:

        structural_total = sum(
            item["Structural Missing"]
            for item in structural_missing
        )

        structural_columns = len(
            structural_missing
        )

        rows.append(
            {
                "Validation": (
                    "Structural Missing Values"
                ),
                "Status": "Passed",
                "Action": (
                    f"Preserved "
                    f"{structural_total:,} structural missing "
                    f"values across {structural_columns} columns: "
                    f"{', '.join(item['Column'] for item in structural_missing)}. "
                    "These missing values represent expected "
                    "unavailable historical data and were preserved "
                    "as NaN."
                ),
            }
        )

    # --------------------------------------------------
    # Improvement in 5 Years
    # --------------------------------------------------
    improvement = (
        reports["missing_values"]["improvement"]
    )

    rows.append(
        {
            "Validation": (
                "Improvement in 5 Years (%)"
            ),
            "Status": "Passed",
            "Action": (
                f"Preserved "
                f"{improvement['Missing Before']:,} "
                "structural missing values "
                "(earliest years lack sufficient "
                "historical data)."
            ),
        }
    )

    # --------------------------------------------------
    # Duplicate Records
    # --------------------------------------------------
    duplicate = repairs["duplicate_records"]

    rows.append(
        {
            "Validation": "Duplicate Records",
            "Status": "Passed",
            "Action": (
                f"Removed "
                f"{duplicate['Duplicates Removed']} "
                "duplicate records based on all "
                "fields except row_num."
            ),
        }
    )

    # --------------------------------------------------
    # Age Distribution
    # --------------------------------------------------
    age = repairs["age_distribution"]

    rows.append(
        {
            "Validation": "Age Distribution",
            "Status": "Passed",
            "Action": (
                f"Repaired "
                f"{age['Rows Repaired']} "
                "rows with invalid or missing age "
                "percentages."
            ),
        }
    )

    # --------------------------------------------------
    # Healthcare Access Repair
    # --------------------------------------------------
    healthcare = repairs["healthcare_access"]

    rows.append(
        {
            "Validation": "Healthcare Access Repair",
            "Status": "Passed",
            "Action": (
                f"Corrected "
                f"{healthcare['Rows Repaired']} "
                "Healthcare Access values exceeding "
                "100%."
            ),
        }
    )

    # --------------------------------------------------
    # Urban/Rural Distribution
    # --------------------------------------------------
    urban = repairs["urban_rural"]

    rows.append(
        {
            "Validation": "Urban/Rural Distribution",
            "Status": "Passed",
            "Action": (
                f"Adjusted "
                f"{urban['Rows Repaired']} "
                "rows so Urban + Rural = 100%."
            ),
        }
    )

    # --------------------------------------------------
    # Gender Population Consistency
    # --------------------------------------------------
    gender = (
        validations["gender_population"]["report"]
    )

    if gender["Passed"]:
        action = (
            "Male + Female population equals "
            "Population affected for all checked rows."
        )
    else:
        action = (
            f"{gender['Violations']} rows violate the "
            "Male + Female population consistency rule."
        )

    rows.append(
        {
            "Validation": (
                "Gender Population Consistency"
            ),
            "Status": get_status(gender),
            "Action": action,
        }
    )

    # --------------------------------------------------
    # Population Constraint
    # --------------------------------------------------
    population = (
        validations["population_constraint"]["report"]
    )

    if population["Passed"]:
        action = (
            "Population affected never exceeds "
            "Country population."
        )
    else:
        action = (
            f"{population['Violations']} rows exceed "
            "their Country population."
        )

    rows.append(
        {
            "Validation": "Population Constraint",
            "Status": get_status(population),
            "Action": action,
        }
    )

    # --------------------------------------------------
    # Composite Health Index Range
    # --------------------------------------------------
    chi = validations["chi"]["report"]

    if chi["Passed"]:
        action = (
            "All Composite Health Index values "
            "lie between 0 and 100."
        )
    else:
        action = (
            f"{chi['Total Violations']} Composite "
            "Health Index values fall outside "
            "the valid range."
        )

    rows.append(
        {
            "Validation": (
                "Composite Health Index Range"
            ),
            "Status": get_status(chi),
            "Action": action,
        }
    )

    # --------------------------------------------------
    # Country-Year Consistency
    # --------------------------------------------------
    consistency = (
        validations["country_year_consistency"]
    )

    informational_columns = {
        "healthcare_access_pct",
        "doctors_per_1000",
        "hospital_beds_per_1000",
        "composite_health_index",
    }

    display_names = {
        "country_pop": "Country Population",
        "per_capita_income_usd": (
            "Per Capita Income (USD)"
        ),
        "education_index": "Education Index",
        "urbanization_rate_pct": (
            "Urbanization Rate (%)"
        ),
        "healthcare_access_pct": (
            "Healthcare Access (%)"
        ),
        "doctors_per_1000": "Doctors per 1000",
        "hospital_beds_per_1000": (
            "Hospital Beds per 1000"
        ),
        "composite_health_index": (
            "Composite Health Index (CHI)"
        ),
    }

    for column, result in consistency.items():

        report = result["report"]

        display_name = display_names.get(
            column,
            column,
        )

        if column in informational_columns:

            status = "Informational"

            action = (
                f"{display_name} varies by disease "
                "within Country-Year; retained as "
                "provided."
            )

        else:

            status = get_status(report)

            if report["Passed"]:

                action = (
                    f"{display_name} is consistent "
                    "across all Country-Year groups."
                )

            else:

                action = (
                    f"{report['Inconsistent Groups']} "
                    "Country-Year groups contain "
                    "inconsistent values."
                )

        rows.append(
            {
                "Validation": (
                    f"{display_name} Consistency"
                ),
                "Status": status,
                "Action": action,
            }
        )

    return pd.DataFrame(rows)