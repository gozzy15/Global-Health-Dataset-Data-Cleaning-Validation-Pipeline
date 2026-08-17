# """
# Test suite for extract.py.

# Tests:
# 1. Dataset exists.
# 2. Dataset loads successfully.
# 3. Correct encoding is used.
# 4. Raw schema is validated.
# 5. Column names are normalized.
# 6. Expected number of rows and columns are returned.
# 7. Missing-value representations are converted to NaN.
# 8. Metadata is generated correctly.
# """

# from pathlib import Path

# import pandas as pd

# from config import (
#     RAW_PATH,
#     EXPECTED_COLUMNS,
#     COLUMN_RENAME_MAP,
# )

# from extract import load_data


# def main():

#     print("\n" + "=" * 70)
#     print("EXTRACT MODULE TEST")
#     print("=" * 70)

#     # --------------------------------------------------
#     # 1. Check dataset path
#     # --------------------------------------------------
#     print("\n[1] Checking dataset path...")

#     path = Path(RAW_PATH)

#     if not path.exists():
#         print(f"✗ Dataset not found: {path}")
#         return

#     print(f"✓ Dataset found: {path}")

#     # --------------------------------------------------
#     # 2. Load dataset
#     # --------------------------------------------------
#     print("\n[2] Loading dataset...")

#     try:
#         df, metadata = load_data(path)

#     except Exception as error:
#         print("✗ Dataset loading failed.")
#         print(f"Error: {error}")
#         raise

#     print("✓ Dataset loaded successfully.")

#     # --------------------------------------------------
#     # 3. Display metadata
#     # --------------------------------------------------
#     print("\n[3] Dataset metadata")

#     print(
#         f"Source file: {metadata['source_file']}"
#     )

#     print(
#         f"Encoding: {metadata['encoding']}"
#     )

#     print(
#         f"Rows: {metadata['rows']:,}"
#     )

#     print(
#         f"Columns: {metadata['columns']}"
#     )

#     print(
#         f"Shape: {metadata['shape']}"
#     )

#     print(
#         f"Memory usage: "
#         f"{metadata['memory_mb']:.2f} MB"
#     )

#     # --------------------------------------------------
#     # 4. Check row and column counts
#     # --------------------------------------------------
#     print("\n[4] Checking dataset dimensions...")

#     assert len(df) == 10_005, (
#         f"Expected 10,005 rows, "
#         f"found {len(df):,}"
#     )

#     assert len(df.columns) == 30, (
#         f"Expected 30 columns, "
#         f"found {len(df.columns)}"
#     )

#     print("✓ Row count is correct: 10,005")
#     print("✓ Column count is correct: 30")
#     print(f"✓ Shape: {df.shape}")

#     # --------------------------------------------------
#     # 5. Check normalized column names
#     # --------------------------------------------------
#     print("\n[5] Checking normalized column names...")

#     expected_normalized_columns = list(
#         COLUMN_RENAME_MAP.values()
#     )

#     actual_columns = list(df.columns)

#     if actual_columns != expected_normalized_columns:

#         print("✗ Column normalization failed.")

#         print("\nExpected:")
#         for index, column in enumerate(
#             expected_normalized_columns,
#             start=1
#         ):
#             print(f"{index}. {column}")

#         print("\nActual:")
#         for index, column in enumerate(
#             actual_columns,
#             start=1
#         ):
#             print(f"{index}. {column}")

#         raise AssertionError(
#             "Normalized column names do not match."
#         )

#     print(
#         "✓ All 30 columns were normalized correctly."
#     )

#     # --------------------------------------------------
#     # 6. Check important normalized columns
#     # --------------------------------------------------
#     print(
#         "\n[6] Checking critical normalized columns..."
#     )

#     required_columns = [
#         "row_num",
#         "country",
#         "year",
#         "disease_name",
#         "country_pop",
#         "incidence_rate_pct",
#         "prevalence_rate_pct",
#         "mortality_rate_pct",
#         "population_affected",
#         "healthcare_access_pct",
#         "doctors_per_1000",
#         "hospital_beds_per_1000",
#         "composite_health_index",
#     ]

#     missing = [
#         column
#         for column in required_columns
#         if column not in df.columns
#     ]

#     assert not missing, (
#         f"Missing normalized columns: {missing}"
#     )

#     print(
#         "✓ All critical normalized columns exist."
#     )

#     # --------------------------------------------------
#     # 7. Check missing-value handling
#     # --------------------------------------------------
#     print(
#         "\n[7] Checking configured missing values..."
#     )

#     total_missing = int(
#         df.isna().sum().sum()
#     )

#     print(
#         f"Total missing values detected: "
#         f"{total_missing:,}"
#     )

#     if total_missing == 0:
#         print(
#             "⚠ No missing values detected."
#         )
#         print(
#             "This is not necessarily an error, "
#             "but verify the raw dataset."
#         )
#     else:
#         print(
#             "✓ Missing values were converted "
#             "to pandas NaN."
#         )

#     # --------------------------------------------------
#     # 8. Check data types at extraction stage
#     # --------------------------------------------------
#     print(
#         "\n[8] Inspecting extracted data types..."
#     )

#     print(df.dtypes.to_string())

#     # --------------------------------------------------
#     # 9. Display sample data
#     # --------------------------------------------------
#     print("\n[9] First five rows")

#     print(
#         df.head().to_string()
#     )

#     # --------------------------------------------------
#     # 10. Check metadata consistency
#     # --------------------------------------------------
#     print(
#         "\n[10] Checking metadata consistency..."
#     )

#     assert metadata["rows"] == len(df)
#     assert metadata["columns"] == len(df.columns)
#     assert metadata["shape"] == df.shape

#     assert metadata["encoding"] == "cp1252"

#     print(
#         "✓ Metadata is consistent with the "
#         "returned DataFrame."
#     )

#     # --------------------------------------------------
#     # 11. Final result
#     # --------------------------------------------------
#     print("\n" + "=" * 70)
#     print("✓ EXTRACT MODULE TEST PASSED")
#     print("=" * 70)

#     print(
#         "\nThe extract module successfully:"
#     )

#     print("  ✓ Located the dataset")
#     print("  ✓ Loaded the CSV")
#     print("  ✓ Used cp1252 encoding")
#     print("  ✓ Validated the raw schema")
#     print("  ✓ Normalized column names")
#     print("  ✓ Preserved the expected 10,005 rows")
#     print("  ✓ Preserved the expected 30 columns")
#     print("  ✓ Converted configured missing values")
#     print("  ✓ Generated consistent metadata")
#     print(list(df.columns))


# if __name__ == "__main__":
#     main()








# """
# Test suite for text_cleaning.py.

# Tests:
# 1. Country corrections.
# 2. Disease corrections.
# 3. Treatment normalization.
# 4. Availability normalization.
# 5. Missing-value preservation.
# 6. General whitespace normalization.
# 7. No unintended DataFrame mutation.
# """

# import pandas as pd

# from extract import load_data
# from text_cleaning import (
#     normalize_text,
#     clean_country,
#     clean_disease,
#     clean_treatment_type,
#     clean_availability,
#     clean_text_columns,
# )
# from config import RAW_PATH


# def main():

#     print("\n" + "=" * 70)
#     print("TEXT CLEANING MODULE TEST")
#     print("=" * 70)

#     # --------------------------------------------------
#     # 1. Load dataset through extract.py
#     # --------------------------------------------------
#     print("\n[1] Loading dataset through extract.py...")

#     df, metadata = load_data(RAW_PATH)

#     print("✓ Dataset loaded.")
#     print(
#         f"Rows: {len(df):,}"
#     )
#     print(
#         f"Columns: {len(df.columns)}"
#     )

#     # --------------------------------------------------
#     # 2. Test normalize_text()
#     # --------------------------------------------------
#     print("\n[2] Testing normalize_text()...")

#     test_value = "   Italy    Test   "

#     result = normalize_text(test_value)

#     assert result == "Italy Test", (
#         f"Unexpected normalization result: {result!r}"
#     )

#     print(
#         "✓ Whitespace normalization works."
#     )

#     # --------------------------------------------------
#     # 3. Test missing-value preservation
#     # --------------------------------------------------
#     print(
#         "\n[3] Testing missing-value preservation..."
#     )

#     result = normalize_text(float("nan"))

#     assert pd.isna(result), (
#         "Missing value was not preserved."
#     )

#     print(
#         "✓ Missing values are preserved."
#     )

#     # --------------------------------------------------
#     # 4. Test country cleaning
#     # --------------------------------------------------
#     print("\n[4] Testing country cleaning...")

#     country_test = pd.Series(
#         [
#             "It@l¥",
#             "It@lĄ",
#             "T?u?r?k?e?y?",
#             "Can@da",
#             "Mex!co",
#             "G%rmany",
#             "?r?zil",
#             "Ind!a",
#             "France",
#             None,
#         ]
#     )

#     cleaned_country = clean_country(
#         country_test
#     )

#     expected_country = [
#         "Italy",
#         "Italy",
#         "Turkey",
#         "Canada",
#         "Mexico",
#         "Germany",
#         "Brazil",
#         "India",
#         "France",
#         None,
#     ]

#     for actual, expected in zip(
#         cleaned_country,
#         expected_country,
#     ):

#         if expected is None:
#             assert pd.isna(actual)
#         else:
#             assert actual == expected, (
#                 f"Expected {expected!r}, "
#                 f"got {actual!r}"
#             )

#     print(
#         "✓ Country corrections passed."
#     )

#     # --------------------------------------------------
#     # 5. Test disease cleaning
#     # --------------------------------------------------
#     print("\n[5] Testing disease cleaning...")

#     disease_test = pd.Series(
#         [
#             "Tub?rculosis",
#             "Influen&za",
#             "Pol!o",
#             "HIV/A!DS",
#             "Malaria",
#             None,
#         ]
#     )

#     cleaned_disease = clean_disease(
#         disease_test
#     )

#     expected_disease = [
#         "Tuberculosis",
#         "Influenza",
#         "Polio",
#         "HIV/AIDS",
#         "Malaria",
#         None,
#     ]

#     for actual, expected in zip(
#         cleaned_disease,
#         expected_disease,
#     ):

#         if expected is None:
#             assert pd.isna(actual)
#         else:
#             assert actual == expected, (
#                 f"Expected {expected!r}, "
#                 f"got {actual!r}"
#             )

#     print(
#         "✓ Disease corrections passed."
#     )

#     # --------------------------------------------------
#     # 6. Test treatment cleaning
#     # --------------------------------------------------
#     print(
#         "\n[6] Testing treatment-type cleaning..."
#     )

#     treatment_test = pd.Series(
#         [
#             "Medication",
#             "MEDICATION",
#             " therapy ",
#             "Surgery",
#             "vaccination",
#             None,
#         ]
#     )

#     cleaned_treatment = clean_treatment_type(
#         treatment_test
#     )

#     expected_treatment = [
#         "Medication",
#         "Medication",
#         "Therapy",
#         "Surgery",
#         "Vaccination",
#         None,
#     ]

#     for actual, expected in zip(
#         cleaned_treatment,
#         expected_treatment,
#     ):

#         if expected is None:
#             assert pd.isna(actual)
#         else:
#             assert actual == expected, (
#                 f"Expected {expected!r}, "
#                 f"got {actual!r}"
#             )

#     print(
#         "✓ Treatment-type normalization passed."
#     )

#     # --------------------------------------------------
#     # 7. Test availability cleaning
#     # --------------------------------------------------
#     print(
#         "\n[7] Testing availability cleaning..."
#     )

#     availability_test = pd.Series(
#         [
#             "high",
#             "HIGH",
#             "medium",
#             "m?dium",
#             "low",
#             "none",
#             "~none~",
#             None,
#         ]
#     )

#     cleaned_availability = clean_availability(
#         availability_test
#     )

#     expected_availability = [
#         "High",
#         "High",
#         "Medium",
#         "Medium",
#         "Low",
#         "None",
#         "None",
#         None,
#     ]

#     for actual, expected in zip(
#         cleaned_availability,
#         expected_availability,
#     ):

#         if expected is None:
#             assert pd.isna(actual)
#         else:
#             assert actual == expected, (
#                 f"Expected {expected!r}, "
#                 f"got {actual!r}"
#             )

#     print(
#         "✓ Availability normalization passed."
#     )

#     # --------------------------------------------------
#     # 8. Test complete DataFrame cleaning
#     # --------------------------------------------------
#     print(
#         "\n[8] Running complete text cleaning..."
#     )

#     original_df = df.copy(
#         deep=True
#     )

#     cleaned_df = clean_text_columns(df)

#     print(
#         "✓ Complete text cleaning executed."
#     )

#     # --------------------------------------------------
#     # 9. Verify original DataFrame was not mutated
#     # --------------------------------------------------
#     print(
#         "\n[9] Checking input DataFrame preservation..."
#     )

#     pd.testing.assert_frame_equal(
#         df,
#         original_df,
#     )

#     print(
#         "✓ Original DataFrame was not modified."
#     )

#     # --------------------------------------------------
#     # 10. Check cleaned countries
#     # --------------------------------------------------
#     print(
#         "\n[10] Checking cleaned country values..."
#     )

#     dirty_countries = {
#         "It@l¥",
#         "It@lĄ",
#         "T?u?r?k?e?y?",
#         "Can@da",
#         "Mex!co",
#         "G%rmany",
#         "?r?zil",
#         "Ind!a",
#     }

#     remaining_dirty_countries = set(
#         cleaned_df["country"].dropna()
#     ).intersection(
#         dirty_countries
#     )

#     assert not remaining_dirty_countries, (
#         "Uncorrected country values remain: "
#         f"{remaining_dirty_countries}"
#     )

#     print(
#         "✓ Configured country corrections "
#         "were applied."
#     )

#     # --------------------------------------------------
#     # 11. Check cleaned disease values
#     # --------------------------------------------------
#     print(
#         "\n[11] Checking cleaned disease values..."
#     )

#     dirty_diseases = {
#         "Tub?rculosis",
#         "Influen&za",
#         "Pol!o",
#         "HIV/A!DS",
#     }

#     remaining_dirty_diseases = set(
#         cleaned_df["disease_name"].dropna()
#     ).intersection(
#         dirty_diseases
#     )

#     assert not remaining_dirty_diseases, (
#         "Uncorrected disease values remain: "
#         f"{remaining_dirty_diseases}"
#     )

#     print(
#         "✓ Configured disease corrections "
#         "were applied."
#     )

#     # --------------------------------------------------
#     # 12. Check treatment categories
#     # --------------------------------------------------
#     print(
#         "\n[12] Checking treatment categories..."
#     )

#     treatment_values = set(
#         cleaned_df["treatment_type"].dropna()
#     )

#     allowed_treatments = {
#         "Medication",
#         "Therapy",
#         "Surgery",
#         "Vaccination",
#     }

#     unexpected_treatments = (
#         treatment_values
#         - allowed_treatments
#     )

#     assert not unexpected_treatments, (
#         "Unexpected treatment values found: "
#         f"{unexpected_treatments}"
#     )

#     print(
#         "✓ Treatment values are standardized."
#     )

#     # --------------------------------------------------
#     # 13. Check availability categories
#     # --------------------------------------------------
#     print(
#         "\n[13] Checking availability categories..."
#     )

#     availability_values = set(
#         cleaned_df[
#             "availability_of_vaccines_treatment"
#         ].dropna()
#     )

#     allowed_availability = {
#         "High",
#         "Medium",
#         "Low",
#         "None",
#     }

#     unexpected_availability = (
#         availability_values
#         - allowed_availability
#     )

#     assert not unexpected_availability, (
#         "Unexpected availability values found: "
#         f"{unexpected_availability}"
#     )

#     print(
#         "✓ Availability values are standardized."
#     )

#     # --------------------------------------------------
#     # 14. Final sample
#     # --------------------------------------------------
#     print(
#         "\n[14] Sample cleaned text values..."
#     )

#     print(
#         cleaned_df[
#             [
#                 "country",
#                 "disease_name",
#                 "treatment_type",
#                 "availability_of_vaccines_treatment",
#             ]
#         ]
#         .head(10)
#         .to_string(index=False)
#     )

#     # --------------------------------------------------
#     # 15. Final result
#     # --------------------------------------------------
#     print("\n" + "=" * 70)
#     print("✓ TEXT CLEANING MODULE TEST PASSED")
#     print("=" * 70)

#     print(
#         "\nThe text-cleaning module successfully:"
#     )

#     print("  ✓ Normalized whitespace")
#     print("  ✓ Preserved missing values")
#     print("  ✓ Corrected country names")
#     print("  ✓ Corrected disease names")
#     print("  ✓ Standardized treatment types")
#     print("  ✓ Standardized availability values")
#     print("  ✓ Preserved the original DataFrame")
#     print("  ✓ Cleaned the complete DataFrame")


# if __name__ == "__main__":
#     main()









# """
# Test suite for the numeric_cleaning module.

# This test verifies:

# 1. Single-value numeric conversion.
# 2. Handling of commas, currency symbols,
#    percentage signs, and apostrophes.
# 3. Missing-value handling.
# 4. Non-convertible value handling.
# 5. Conversion of all configured numeric columns.
# 6. Correct conversion reports.
# 7. Preservation of the input DataFrame.
# 8. No unexpected loss of data.
# """

# from pathlib import Path

# import numpy as np
# import pandas as pd

# from config import (
#     RAW_PATH,
#     NUMERIC_COLUMNS,
# )

# from extract import load_data
# from text_cleaning import clean_text_columns
# from numeric_cleaning import (
#     clean_numeric_value,
#     convert_numeric_columns,
# )


# def check(condition, success_message, failure_message):
#     """
#     Print a test result and raise AssertionError on failure.
#     """

#     if condition:
#         print(f"✓ {success_message}")
#     else:
#         print(f"✗ {failure_message}")
#         raise AssertionError(failure_message)


# def main():

#     print("=" * 70)
#     print("NUMERIC CLEANING MODULE TEST")
#     print("=" * 70)

#     # --------------------------------------------------
#     # 1. Load dataset through extract.py
#     # --------------------------------------------------
#     print("\n[1] Loading dataset through extract.py...")

#     raw_path = Path(RAW_PATH)

#     check(
#         raw_path.exists(),
#         f"Dataset found: {raw_path}",
#         f"Dataset not found: {raw_path}",
#     )

#     df, metadata = load_data(raw_path)

#     print("✓ Dataset loaded.")
#     print(f"Rows: {len(df):,}")
#     print(f"Columns: {len(df.columns)}")

#     # --------------------------------------------------
#     # 2. Apply text cleaning first
#     # --------------------------------------------------
#     print("\n[2] Running text cleaning before numeric conversion...")

#     cleaned_text_df = clean_text_columns(df)

#     check(
#         cleaned_text_df.shape == df.shape,
#         "Text cleaning completed successfully.",
#         "Text cleaning changed the dataset shape.",
#     )

#     # --------------------------------------------------
#     # 3. Test clean_numeric_value()
#     # --------------------------------------------------
#     print("\n[3] Testing clean_numeric_value()...")

#     test_values = {
#         "plain integer": (123, 123.0),
#         "plain decimal": (123.45, 123.45),
#         "apostrophe": ("'1167", 1167.0),
#         "apostrophe decimal": ("'35500.22", 35500.22),
#         "comma": ("1,234,567", 1234567.0),
#         "currency": ("$12,500", 12500.0),
#         "percentage": ("85.5%", 85.5),
#         "currency + comma": ("$35,500.22", 35500.22),
#         "apostrophe + comma": ("'35,500.22", 35500.22),
#         "whitespace": ("  123.45  ", 123.45),
#     }

#     for description, (value, expected) in test_values.items():

#         result = clean_numeric_value(value)

#         check(
#             result == expected,
#             f"{description}: {value!r} → {result}",
#             (
#                 f"{description} failed: "
#                 f"expected {expected}, got {result}"
#             ),
#         )

#     print("✓ Numeric formatting conversions passed.")

#     # --------------------------------------------------
#     # 4. Test missing values
#     # --------------------------------------------------
#     print("\n[4] Testing missing-value handling...")

#     missing_values = [
#         None,
#         np.nan,
#         "",
#         " ",
#     ]

#     for value in missing_values:

#         result = clean_numeric_value(value)

#         check(
#             pd.isna(result),
#             f"Missing value {value!r} converted to NaN.",
#             (
#                 f"Missing value {value!r} "
#                 f"was not converted to NaN."
#             ),
#         )

#     print("✓ Missing-value handling passed.")

#     # --------------------------------------------------
#     # 5. Test invalid numeric values
#     # --------------------------------------------------
#     print("\n[5] Testing non-convertible values...")

#     invalid_values = [
#         "abc",
#         "hello",
#         "not available",
#         "xyz123",
#     ]

#     for value in invalid_values:

#         result = clean_numeric_value(value)

#         check(
#             pd.isna(result),
#             f"Invalid value {value!r} converted to NaN.",
#             (
#                 f"Invalid value {value!r} "
#                 f"did not convert to NaN."
#             ),
#         )

#     print("✓ Non-convertible values handled correctly.")

#     # --------------------------------------------------
#     # 6. Preserve original DataFrame
#     # --------------------------------------------------
#     print("\n[6] Checking input DataFrame preservation...")

#     text_cleaned_original = cleaned_text_df.copy(deep=True)

#     converted_df, conversion_report = (
#         convert_numeric_columns(cleaned_text_df)
#     )

#     check(
#         cleaned_text_df.equals(text_cleaned_original),
#         "Original DataFrame was not modified.",
#         "Input DataFrame was modified in place.",
#     )

#     # --------------------------------------------------
#     # 7. Check all configured numeric columns
#     # --------------------------------------------------
#     print("\n[7] Checking configured numeric columns...")

#     missing_numeric_columns = [
#         column
#         for column in NUMERIC_COLUMNS
#         if column not in converted_df.columns
#     ]

#     check(
#         not missing_numeric_columns,
#         (
#             f"All {len(NUMERIC_COLUMNS)} configured "
#             "numeric columns exist."
#         ),
#         (
#             "Missing configured numeric columns: "
#             f"{missing_numeric_columns}"
#         ),
#     )

#     # --------------------------------------------------
#     # 8. Check numeric dtypes
#     # --------------------------------------------------
#     print("\n[8] Checking numeric data types...")

#     non_numeric_columns = [
#         column
#         for column in NUMERIC_COLUMNS
#         if not pd.api.types.is_numeric_dtype(
#             converted_df[column]
#         )
#     ]

#     check(
#         not non_numeric_columns,
#         "All configured numeric columns have numeric dtypes.",
#         (
#             "The following columns are not numeric: "
#             f"{non_numeric_columns}"
#         ),
#     )

#     # --------------------------------------------------
#     # 9. Check no unexpected row loss
#     # --------------------------------------------------
#     print("\n[9] Checking row preservation...")

#     check(
#         len(converted_df) == len(cleaned_text_df),
#         (
#             f"Row count preserved: "
#             f"{len(converted_df):,}"
#         ),
#         (
#             "Row count changed during numeric conversion."
#         ),
#     )

#     # --------------------------------------------------
#     # 10. Check column preservation
#     # --------------------------------------------------
#     print("\n[10] Checking column preservation...")

#     check(
#         list(converted_df.columns)
#         == list(cleaned_text_df.columns),
#         "All columns were preserved.",
#         "Column structure changed during numeric conversion.",
#     )

#     # --------------------------------------------------
#     # 11. Check conversion report
#     # --------------------------------------------------
#     print("\n[11] Checking conversion report...")

#     check(
#         isinstance(conversion_report, list),
#         "Conversion report is a list.",
#         "Conversion report is not a list.",
#     )

#     check(
#         len(conversion_report) == len(NUMERIC_COLUMNS),
#         (
#             f"Conversion report contains "
#             f"{len(conversion_report)} entries."
#         ),
#         (
#             f"Expected {len(NUMERIC_COLUMNS)} report entries "
#             f"but found {len(conversion_report)}."
#         ),
#     )

#     # --------------------------------------------------
#     # 12. Check report structure
#     # --------------------------------------------------
#     print("\n[12] Checking conversion report structure...")

#     required_report_fields = {
#         "Column",
#         "Original dtype",
#         "Final dtype",
#         "Missing Before",
#         "Missing After",
#         "New NaNs",
#     }

#     invalid_reports = []

#     for report in conversion_report:

#         missing_fields = (
#             required_report_fields
#             - set(report.keys())
#         )

#         if missing_fields:
#             invalid_reports.append(
#                 {
#                     "column": report.get("Column"),
#                     "missing_fields": missing_fields,
#                 }
#             )

#     check(
#         not invalid_reports,
#         "All conversion reports contain the required fields.",
#         (
#             "Some conversion reports are missing fields: "
#             f"{invalid_reports}"
#         ),
#     )

#     # --------------------------------------------------
#     # 13. Check reported columns
#     # --------------------------------------------------
#     print("\n[13] Checking reported column names...")

#     reported_columns = [
#         report["Column"]
#         for report in conversion_report
#     ]

#     check(
#         reported_columns == NUMERIC_COLUMNS,
#         "All configured numeric columns were reported.",
#         (
#             "Reported columns do not match "
#             "NUMERIC_COLUMNS."
#         ),
#     )

#     # --------------------------------------------------
#     # 14. Check missing-value accounting
#     # --------------------------------------------------
#     print("\n[14] Checking missing-value accounting...")

#     invalid_missing_counts = []

#     for report in conversion_report:

#         if (
#             report["Missing After"]
#             < report["Missing Before"]
#         ):
#             invalid_missing_counts.append(
#                 report["Column"]
#             )

#         expected_new_nans = max(
#             0,
#             (
#                 report["Missing After"]
#                 - report["Missing Before"]
#             ),
#         )

#         if report["New NaNs"] != expected_new_nans:
#             invalid_missing_counts.append(
#                 report["Column"]
#             )

#     check(
#         not invalid_missing_counts,
#         "Missing-value accounting is internally consistent.",
#         (
#             "Invalid missing-value accounting found in: "
#             f"{invalid_missing_counts}"
#         ),
#     )

#     # --------------------------------------------------
#     # 15. Display conversion summary
#     # --------------------------------------------------
#     print("\n[15] Numeric conversion summary...")

#     conversion_df = pd.DataFrame(conversion_report)

#     print(
#         conversion_df.to_string(index=False)
#     )

#     # --------------------------------------------------
#     # 16. Inspect selected converted values
#     # --------------------------------------------------
#     print("\n[16] Inspecting converted values...")

#     sample_columns = [
#         "incidence_rate_pct",
#         "prevalence_rate_pct",
#         "ages_0_18_pct",
#         "average_annual_treatment_cost_usd",
#         "per_capita_income_usd",
#     ]

#     print(
#         converted_df[sample_columns].head(10).to_string(
#             index=False
#         )
#     )

#     # --------------------------------------------------
#     # 17. Final checks
#     # --------------------------------------------------
#     print("\n[17] Final numeric-column verification...")

#     for column in NUMERIC_COLUMNS:

#         check(
#             pd.api.types.is_numeric_dtype(
#                 converted_df[column]
#             ),
#             f"{column}: numeric dtype confirmed.",
#             f"{column}: numeric dtype check failed.",
#         )

#     # --------------------------------------------------
#     # Final result
#     # --------------------------------------------------
#     print("\n" + "=" * 70)
#     print("✓ NUMERIC CLEANING MODULE TEST PASSED")
#     print("=" * 70)

#     print(
#         "\nThe numeric-cleaning module successfully:"
#     )

#     print("  ✓ Converted numeric values")
#     print("  ✓ Removed apostrophes from numeric strings")
#     print("  ✓ Removed commas from numeric strings")
#     print("  ✓ Removed currency symbols")
#     print("  ✓ Removed percentage signs")
#     print("  ✓ Preserved missing values as NaN")
#     print("  ✓ Converted invalid values to NaN")
#     print("  ✓ Converted all configured numeric columns")
#     print("  ✓ Preserved the original DataFrame")
#     print("  ✓ Preserved row count")
#     print("  ✓ Preserved column structure")
#     print("  ✓ Generated conversion statistics")
#     print("  ✓ Generated a complete conversion report")


# if __name__ == "__main__":
#     main()











# """
# Tests for the missing_values module in the
# Global Health Dataset cleaning project.

# This test module verifies:

# - Missing-value summaries
# - Identifier-row removal
# - Group-median imputation
# - Structural missing-value identification
# - Peer-country median imputation
# - Per-capita income interpolation
# - Education Index interpolation
# - Preservation of five-year improvement missing values
# - Complete missing-value handling
# - Input DataFrame preservation
# - Row and column preservation
# - Imputation reports
# """

# import sys
# from pathlib import Path

# import numpy as np
# import pandas as pd


# # -------------------------------------------------------------------
# # Make src directory importable
# # -------------------------------------------------------------------

# PROJECT_ROOT = Path(__file__).resolve().parent.parent
# SRC_PATH = PROJECT_ROOT / "src"

# if str(SRC_PATH) not in sys.path:
#     sys.path.insert(0, str(SRC_PATH))


# # -------------------------------------------------------------------
# # Imports
# # -------------------------------------------------------------------

# from extract import load_data
# from text_cleaning import clean_text_columns
# from numeric_cleaning import convert_numeric_columns

# from missing_values import (
#     summarize_missing,
#     drop_missing_identifiers,
#     fill_with_group_median,
#     identify_structural_missingness,
#     fill_peer_country_median,
#     impute_per_capita_income,
#     impute_education_index,
#     preserve_improvement_missing,
#     handle_missing_values,
# )

# from config import (
#     RAW_PATH,
#     IDENTIFIER_COLUMNS,
#     STRUCTURAL_MISSING_COLUMNS,
#     PEER_COUNTRIES,
#     PEER_IMPUTATION_COLUMNS,
# )


# # -------------------------------------------------------------------
# # Helper function
# # -------------------------------------------------------------------

# def load_clean_numeric_data():
#     """
#     Load the raw dataset and prepare it for missing-value testing.

#     The missing-value module expects normalized column names and
#     numeric columns, so extraction, text cleaning, and numeric
#     conversion are performed first.
#     """

#     df, metadata = load_data(RAW_PATH)

#     df = clean_text_columns(df)

#     df, conversion_report = convert_numeric_columns(df)

#     return df


# # -------------------------------------------------------------------
# # Main test
# # -------------------------------------------------------------------

# def main():

#     print("=" * 70)
#     print("MISSING VALUES MODULE TEST")
#     print("=" * 70)

#     # ================================================================
#     # 1. Load and prepare dataset
#     # ================================================================

#     print("\n[1] Loading dataset through previous modules...")

#     df = load_clean_numeric_data()

#     print("✓ Dataset loaded and prepared.")
#     print(f"Rows: {len(df):,}")
#     print(f"Columns: {len(df.columns)}")

#     assert len(df) == 10_005, (
#         f"Expected 10,005 rows, found {len(df):,}"
#     )

#     assert len(df.columns) == 30, (
#         f"Expected 30 columns, found {len(df.columns)}"
#     )

#     print("✓ Expected dataset dimensions confirmed.")

#     # Keep a copy to verify that functions do not mutate inputs.
#     original_df = df.copy(deep=True)

#     # ================================================================
#     # 2. Test summarize_missing()
#     # ================================================================

#     print("\n[2] Testing summarize_missing()...")

#     missing_summary = summarize_missing(df)

#     assert isinstance(
#         missing_summary,
#         pd.DataFrame,
#     ), "Missing summary must be a DataFrame."

#     assert list(missing_summary.columns) == [
#         "Missing Count",
#         "Missing Percent",
#     ], "Unexpected missing-summary columns."

#     # Every returned column must actually contain missing values.
#     assert (
#         missing_summary["Missing Count"] > 0
#     ).all(), "Summary contains a column with zero missing values."

#     # Verify descending order.
#     counts = missing_summary["Missing Count"].tolist()

#     assert counts == sorted(
#         counts,
#         reverse=True,
#     ), "Missing summary is not sorted descending."

#     print("✓ Missing-value summary generated correctly.")

#     print("\nTop missing-value columns:")
#     print(missing_summary.head(10).to_string())


#     # ================================================================
#     # 3. Test drop_missing_identifiers()
#     # ================================================================

#     print("\n[3] Testing drop_missing_identifiers()...")

#     test_identifiers = pd.DataFrame(
#         {
#             "country": [
#                 "Nigeria",
#                 None,
#                 "Ghana",
#                 "Kenya",
#             ],
#             "year": [
#                 2020,
#                 2021,
#                 None,
#                 2023,
#             ],
#             "disease_name": [
#                 "Malaria",
#                 "Cancer",
#                 "Diabetes",
#                 "Cholera",
#             ],
#             "value": [
#                 10,
#                 20,
#                 30,
#                 40,
#             ],
#         }
#     )

#     cleaned_identifiers, identifier_report = (
#         drop_missing_identifiers(
#             test_identifiers
#         )
#     )

#     assert len(cleaned_identifiers) == 2, (
#         "Expected two rows to remain after "
#         "removing rows with missing identifiers."
#     )

#     assert identifier_report["Rows Before"] == 4
#     assert identifier_report["Rows After"] == 2
#     assert identifier_report["Rows Removed"] == 2
#     assert identifier_report[
#         "Rows With Missing Identifiers"
#     ] == 2

#     print("✓ Missing identifier rows were removed correctly.")
#     print(f"✓ Identifier report: {identifier_report}")


#     # ================================================================
#     # 4. Test fill_with_group_median()
#     # ================================================================

#     print("\n[4] Testing fill_with_group_median()...")

#     test_group = pd.DataFrame(
#         {
#             "country": [
#                 "Nigeria",
#                 "Nigeria",
#                 "Nigeria",
#                 "Ghana",
#                 "Ghana",
#             ],
#             "year": [
#                 2020,
#                 2021,
#                 2022,
#                 2020,
#                 2021,
#             ],
#             "value": [
#                 10.0,
#                 np.nan,
#                 30.0,
#                 100.0,
#                 np.nan,
#             ],
#         }
#     )

#     group_result, group_report = (
#         fill_with_group_median(
#             test_group,
#             column="value",
#             group_cols=["country"],
#         )
#     )

#     # Nigeria median = 20.
#     # Ghana has only one valid value = 100.
#     assert group_result.loc[
#         1, "value"
#     ] == 20.0

#     assert group_result.loc[
#         4, "value"
#     ] == 100.0

#     assert group_result["value"].isna().sum() == 0

#     assert group_report["Missing Before"] == 2
#     assert group_report["Filled by Group Median"] == 2
#     assert group_report["Filled by Global Median"] == 0
#     assert group_report["Missing After"] == 0

#     print("✓ Group-median imputation works correctly.")
#     print(f"✓ Group-median report: {group_report}")


#     # ================================================================
#     # 5. Test global-median fallback
#     # ================================================================

#     print("\n[5] Testing global-median fallback...")

#     test_global = pd.DataFrame(
#         {
#             "country": [
#                 "Nigeria",
#                 "Nigeria",
#                 "Ghana",
#             ],
#             "value": [
#                 10.0,
#                 np.nan,
#                 np.nan,
#             ],
#         }
#     )

#     global_result, global_report = (
#         fill_with_group_median(
#             test_global,
#             column="value",
#             group_cols=["country"],
#         )
#     )

#     # The Nigeria missing value can use Nigeria's
#     # group median of 10.
#     # Ghana has no group value, so it falls back
#     # to the global median of 10.
#     assert (
#         global_result["value"].isna().sum() == 0
#     )

#     assert global_report[
#         "Filled by Group Median"
#     ] == 1

#     assert global_report[
#         "Filled by Global Median"
#     ] == 1

#     print("✓ Global-median fallback works correctly.")


#     # ================================================================
#     # 6. Test identify_structural_missingness()
#     # ================================================================

#     print(
#         "\n[6] Testing identify_structural_missingness()..."
#     )

#     structural_before = df[
#         STRUCTURAL_MISSING_COLUMNS
#     ].isna().sum()

#     structural_result, structural_report = (
#         identify_structural_missingness(df)
#     )

#     assert isinstance(
#         structural_result,
#         pd.DataFrame,
#     )

#     assert len(structural_report) == len(
#         STRUCTURAL_MISSING_COLUMNS
#     )

#     reported_columns = [
#         item["Column"]
#         for item in structural_report
#     ]

#     assert reported_columns == (
#         STRUCTURAL_MISSING_COLUMNS
#     )

#     for item in structural_report:

#         column = item["Column"]

#         assert (
#             item["Structural Missing"]
#             == int(structural_before[column])
#         )

#         assert item["Action"] == (
#             "Preserve as NaN"
#         )

#     # Verify no values were changed.
#     pd.testing.assert_frame_equal(
#         df,
#         structural_result,
#     )

#     print(
#         "✓ Structural missing values were identified "
#         "and preserved."
#     )

#     print("\nStructural missing-value summary:")

#     structural_display = pd.DataFrame(
#         structural_report
#     )

#     print(
#         structural_display.to_string(
#             index=False
#         )
#     )


#     # ================================================================
#     # 7. Test fill_peer_country_median()
#     # ================================================================

#     print(
#         "\n[7] Testing fill_peer_country_median()..."
#     )

#     # Construct a controlled example using the configured
#     # United Kingdom peer countries.
#     peer_test = pd.DataFrame(
#         {
#             "country": [
#                 "United Kingdom",
#                 "Canada",
#                 "France",
#                 "Germany",
#                 "Australia",
#                 "Japan",
#             ],
#             "year": [
#                 2020,
#                 2020,
#                 2020,
#                 2020,
#                 2020,
#                 2020,
#             ],
#             "disease_name": [
#                 "Malaria",
#                 "Malaria",
#                 "Malaria",
#                 "Malaria",
#                 "Malaria",
#                 "Malaria",
#             ],
#             "healthcare_access_pct": [
#                 np.nan,
#                 60.0,
#                 70.0,
#                 80.0,
#                 90.0,
#                 100.0,
#             ],
#         }
#     )

#     peer_result, peer_report = (
#         fill_peer_country_median(
#             peer_test,
#             column="healthcare_access_pct",
#         )
#     )

#     # Peer values:
#     # 60, 70, 80, 90, 100
#     # Median = 80
#     assert (
#         peer_result.loc[
#             0,
#             "healthcare_access_pct",
#         ]
#         == 80.0
#     )

#     assert peer_report["Missing Before"] == 1
#     assert peer_report["Filled"] == 1
#     assert peer_report["Missing After"] == 0

#     print("✓ Peer-country median imputation works correctly.")
#     print(f"✓ Peer-country report: {peer_report}")


#     # ================================================================
#     # 8. Test peer-country preservation when no peer exists
#     # ================================================================

#     print(
#         "\n[8] Testing peer-country missing-value preservation..."
#     )

#     peer_missing = pd.DataFrame(
#         {
#             "country": [
#                 "United Kingdom",
#             ],
#             "year": [
#                 2020,
#             ],
#             "disease_name": [
#                 "Malaria",
#             ],
#             "healthcare_access_pct": [
#                 np.nan,
#             ],
#         }
#     )

#     peer_missing_result, peer_missing_report = (
#         fill_peer_country_median(
#             peer_missing,
#             column="healthcare_access_pct",
#         )
#     )

#     assert (
#         peer_missing_result[
#             "healthcare_access_pct"
#         ].isna().sum()
#         == 1
#     )

#     assert peer_missing_report["Filled"] == 0
#     assert peer_missing_report["Missing After"] == 1

#     print(
#         "✓ Missing values are preserved when "
#         "no valid peer value exists."
#     )


#     # ================================================================
#     # 9. Test per-capita income interpolation
#     # ================================================================

#     print(
#         "\n[9] Testing impute_per_capita_income()..."
#     )

#     income_test = pd.DataFrame(
#         {
#             "country": [
#                 "Nigeria",
#                 "Nigeria",
#                 "Nigeria",
#                 "Ghana",
#             ],
#             "year": [
#                 2020,
#                 2021,
#                 2022,
#                 2020,
#             ],
#             "per_capita_income_usd": [
#                 1000.0,
#                 np.nan,
#                 1400.0,
#                 2000.0,
#             ],
#         }
#     )

#     income_result, income_report = (
#         impute_per_capita_income(
#             income_test
#         )
#     )

#     # 2021 should be interpolated halfway between
#     # 1000 and 1400.
#     nigeria_2021 = income_result.loc[
#         income_result["year"] == 2021,
#         "per_capita_income_usd",
#     ].iloc[0]

#     assert nigeria_2021 == 1200.0

#     assert income_report[
#         "Missing Before"
#     ] == 1

#     assert income_report[
#         "Filled by Interpolation"
#     ] == 1

#     assert income_report[
#         "Missing After"
#     ] == 0

#     print(
#         "✓ Per-capita income interpolation works correctly."
#     )
#     print(f"✓ Income report: {income_report}")


#     # ================================================================
#     # 10. Test education index interpolation and filling
#     # ================================================================

#     print(
#         "\n[10] Testing impute_education_index()..."
#     )

#     education_test = pd.DataFrame(
#         {
#             "country": [
#                 "Nigeria",
#                 "Nigeria",
#                 "Nigeria",
#                 "Ghana",
#                 "Ghana",
#                 "Kenya",
#             ],
#             "year": [
#                 2020,
#                 2021,
#                 2022,
#                 2020,
#                 2021,
#                 2020,
#             ],
#             "education_index": [
#                 0.60,
#                 np.nan,
#                 0.80,
#                 0.70,
#                 np.nan,
#                 np.nan,
#             ],
#         }
#     )

#     education_result, education_report = (
#         impute_education_index(
#             education_test
#         )
#     )

#     # Nigeria 2021 should interpolate to 0.70.
#     nigeria_2021_education = (
#         education_result.loc[
#             (
#                 education_result["country"]
#                 == "Nigeria"
#             )
#             &
#             (
#                 education_result["year"]
#                 == 2021
#             ),
#             "education_index",
#         ].iloc[0]
#     )

#     assert nigeria_2021_education == 0.70

#     # Ghana has one known value, so the missing value
#     # should be filled using bfill/ffill.
#     ghana_2021_education = (
#         education_result.loc[
#             (
#                 education_result["country"]
#                 == "Ghana"
#             )
#             &
#             (
#                 education_result["year"]
#                 == 2021
#             ),
#             "education_index",
#         ].iloc[0]
#     )

#     assert ghana_2021_education == 0.70

#     # Kenya has no valid value at all, so it should
#     # remain missing.
#     kenya_value = (
#         education_result.loc[
#             education_result["country"]
#             == "Kenya",
#             "education_index",
#         ].iloc[0]
#     )

#     assert pd.isna(kenya_value)

#     assert education_report[
#         "Missing Before"
#     ] == 3

#     assert education_report[
#         "Filled"
#     ] == 2

#     assert education_report[
#         "Missing After"
#     ] == 1

#     print(
#         "✓ Education Index interpolation and "
#         "country-wise filling work correctly."
#     )

#     print(
#         f"✓ Education report: {education_report}"
#     )


#     # ================================================================
#     # 11. Test preserve_improvement_missing()
#     # ================================================================

#     print(
#         "\n[11] Testing preserve_improvement_missing()..."
#     )

#     improvement_test = pd.DataFrame(
#         {
#             "improvement_in_5_years_pct": [
#                 20.0,
#                 np.nan,
#                 -10.0,
#                 np.nan,
#             ],
#         }
#     )

#     improvement_result, improvement_report = (
#         preserve_improvement_missing(
#             improvement_test
#         )
#     )

#     assert (
#         improvement_result[
#             "improvement_in_5_years_pct"
#         ].isna().sum()
#         == 2
#     )

#     assert improvement_report[
#         "Missing Before"
#     ] == 2

#     assert improvement_report[
#         "Missing After"
#     ] == 2

#     print(
#         "✓ Structural improvement missing values "
#         "were preserved."
#     )

#     print(
#         f"✓ Improvement report: {improvement_report}"
#     )


#     # ================================================================
#     # 12. Check complete handle_missing_values()
#     # ================================================================

#     print(
#         "\n[12] Running complete handle_missing_values()..."
#     )

#     pipeline_input = df.copy(deep=True)

#     cleaned_df, reports = (
#         handle_missing_values(
#             pipeline_input
#         )
#     )

#     assert isinstance(
#         cleaned_df,
#         pd.DataFrame,
#     )

#     assert isinstance(
#         reports,
#         dict,
#     )

#     print(
#         "✓ Complete missing-value handling executed."
#     )


#     # ================================================================
#     # 13. Check expected reports
#     # ================================================================

#     print(
#         "\n[13] Checking missing-value reports..."
#     )

#     expected_reports = [
#         "identifier_rows",
#         "healthcare_access",
#         "doctors_per_1000",
#         "hospital_beds_per_1000",
#         "per_capita_income",
#         "education_index",
#         "structural_missing",
#         "improvement",
#     ]

#     for report_name in expected_reports:

#         assert report_name in reports, (
#             f"Missing report: {report_name}"
#         )

#         print(
#             f"✓ Report found: {report_name}"
#         )


#     # ================================================================
#     # 14. Check row preservation
#     # ================================================================

#     print(
#         "\n[14] Checking row preservation..."
#     )

#     rows_removed = reports[
#         "identifier_rows"
#     ]["Rows Removed"]

#     expected_rows = (
#         len(df) - rows_removed
#     )

#     assert len(cleaned_df) == expected_rows

#     print(
#         f"✓ Rows before: {len(df):,}"
#     )

#     print(
#         f"✓ Rows removed: {rows_removed:,}"
#     )

#     print(
#         f"✓ Rows after: {len(cleaned_df):,}"
#     )


#     # ================================================================
#     # 15. Check column preservation
#     # ================================================================

#     print(
#         "\n[15] Checking column preservation..."
#     )

#     assert list(cleaned_df.columns) == list(
#         df.columns
#     )

#     print(
#         "✓ All original columns were preserved."
#     )


#     # ================================================================
#     # 16. Check input DataFrame preservation
#     # ================================================================

#     print(
#         "\n[16] Checking input DataFrame preservation..."
#     )

#     pd.testing.assert_frame_equal(
#         df,
#         original_df,
#     )

#     print(
#         "✓ Original DataFrame was not modified."
#     )


#     # ================================================================
#     # 17. Check peer-country imputation results
#     # ================================================================

#     print(
#         "\n[17] Checking configured peer-country "
#         "imputation columns..."
#     )

#     for column in PEER_IMPUTATION_COLUMNS:

#         assert column in cleaned_df.columns

#         print(
#             f"✓ {column}: column exists."
#         )


#     # ================================================================
#     # 18. Check structural missing values remain NaN
#     # ================================================================

#     print(
#         "\n[18] Checking structural missing values..."
#     )

#     for column in STRUCTURAL_MISSING_COLUMNS:

#         before = df[column].isna().sum()
#         after = cleaned_df[column].isna().sum()

#         # The missing-value handler should not fill
#         # these columns.
#         assert after == before, (
#             f"Structural missing count changed "
#             f"for {column}: "
#             f"{before} → {after}"
#         )

#         print(
#             f"✓ {column}: "
#             f"{after:,} structural missing values preserved."
#         )


#     # ================================================================
#     # 19. Check improvement missing values remain preserved
#     # ================================================================

#     print(
#         "\n[19] Checking five-year improvement missing values..."
#     )

#     improvement_column = (
#         "improvement_in_5_years_pct"
#     )

#     before = df[
#         improvement_column
#     ].isna().sum()

#     after = cleaned_df[
#         improvement_column
#     ].isna().sum()

#     assert before == after

#     print(
#         f"✓ Improvement missing values preserved: "
#         f"{after:,}"
#     )


#     # ================================================================
#     # 20. Display complete missing-value reports
#     # ================================================================

#     print(
#         "\n[20] Missing-value treatment summary..."
#     )

#     for name, report in reports.items():

#         print(
#             f"\n--- {name} ---"
#         )

#         if isinstance(report, dict):

#             for key, value in report.items():

#                 print(
#                     f"{key}: {value}"
#                 )

#         elif isinstance(report, list):

#             report_df = pd.DataFrame(
#                 report
#             )

#             print(
#                 report_df.to_string(
#                     index=False
#                 )
#             )


#     # ================================================================
#     # Final result
#     # ================================================================

#     print("\n" + "=" * 70)
#     print("✓ MISSING VALUES MODULE TEST PASSED")
#     print("=" * 70)

#     print(
#         """
# The missing-values module successfully:

#   ✓ Summarized missing values
#   ✓ Removed rows with missing identifiers
#   ✓ Filled values using group medians
#   ✓ Used global median fallback where required
#   ✓ Identified structural missing values
#   ✓ Preserved structural missing values
#   ✓ Filled peer-country values using contextual medians
#   ✓ Preserved missing values when no peer value was available
#   ✓ Interpolated per-capita income by country
#   ✓ Interpolated Education Index by country
#   ✓ Used country-wise backfill/forward-fill for Education Index
#   ✓ Preserved five-year improvement missing values
#   ✓ Executed the complete missing-value treatment
#   ✓ Generated all expected reports
#   ✓ Preserved the expected column structure
#   ✓ Preserved the input DataFrame
# """
#     )


# if __name__ == "__main__":
#     main()













# """
# Test suite for the validation module.

# This test verifies duplicate handling, range validation,
# data-quality repairs, consistency checks, and the complete
# validation workflow.
# """

# import numpy as np
# import pandas as pd

# from extract import load_data
# from text_cleaning import clean_text_columns
# from numeric_cleaning import convert_numeric_columns
# from missing_values import handle_missing_values

# from validation import (
#     check_duplicates,
#     remove_duplicate_records,
#     validate_numeric_range,
#     show_range_violations,
#     repair_age_distribution,
#     repair_healthcare_access,
#     validate_gender_population,
#     validate_urban_rural_distribution,
#     repair_urban_rural_distribution,
#     validate_population_affected,
#     validate_chi,
#     validate_country_year_consistency,
#     clean_and_validate_data,
# )

# from config import (
#     RAW_PATH,
#     VALID_RANGES,
#     COUNTRY_YEAR_COLUMNS,
# )


# print("=" * 70)
# print("VALIDATION MODULE TEST")
# print("=" * 70)


# # ==============================================================
# # 1. Load and prepare dataset
# # ==============================================================

# print("\n[1] Loading dataset through previous modules...")

# df, metadata = load_data(RAW_PATH)

# df = clean_text_columns(df)

# df, conversion_report = convert_numeric_columns(df)

# df, missing_reports = handle_missing_values(df)

# print("✓ Dataset loaded and prepared.")
# print(f"Rows: {len(df):,}")
# print(f"Columns: {len(df.columns)}")


# # ==============================================================
# # 2. Check expected dimensions
# # ==============================================================

# assert len(df) == 10_005
# assert len(df.columns) == 30

# print("✓ Expected dataset dimensions confirmed.")


# # ==============================================================
# # 3. Test check_duplicates()
# # ==============================================================

# print("\n[2] Testing check_duplicates()...")

# # --------------------------------------------------
# # Test 1: Exact duplicate rows
# # --------------------------------------------------
# exact_duplicate_df = pd.DataFrame(
#     {
#         "row_num": [1, 2, 3, 1],
#         "country": [
#             "Testland",
#             "Examplestan",
#             "Sampleland",
#             "Testland",
#         ],
#         "year": [2020, 2021, 2022, 2020],
#         "disease_name": [
#             "Disease A",
#             "Disease B",
#             "Disease C",
#             "Disease A",
#         ],
#         "value": [10, 20, 30, 10],
#     }
# )

# report = check_duplicates(exact_duplicate_df)

# print("Exact duplicate test report:")
# print(report)

# assert report["Total Rows"] == 4
# assert report["Duplicate Rows"] == 1
# assert report["Duplicate Country-Year-Disease"] == 1

# print("✓ Exact duplicate detection works correctly.")


# # --------------------------------------------------
# # Test 2: Country-Year-Disease duplicate
# # --------------------------------------------------
# key_duplicate_df = pd.DataFrame(
#     {
#         "row_num": [1, 2, 3],
#         "country": [
#             "Testland",
#             "Examplestan",
#             "Testland",
#         ],
#         "year": [2020, 2021, 2020],
#         "disease_name": [
#             "Disease A",
#             "Disease B",
#             "Disease A",
#         ],
#         "value": [10, 20, 99],
#     }
# )

# report = check_duplicates(key_duplicate_df)

# print("Country-Year-Disease duplicate test report:")
# print(report)

# assert report["Total Rows"] == 3
# assert report["Duplicate Rows"] == 0
# assert report["Duplicate Country-Year-Disease"] == 1

# print(
#     "✓ Country-Year-Disease duplicate detection "
#     "works correctly."
# )


# # --------------------------------------------------
# # Test 3: No duplicates
# # --------------------------------------------------
# unique_df = pd.DataFrame(
#     {
#         "row_num": [1, 2, 3],
#         "country": [
#             "Testland",
#             "Examplestan",
#             "Sampleland",
#         ],
#         "year": [2020, 2021, 2022],
#         "disease_name": [
#             "Disease A",
#             "Disease B",
#             "Disease C",
#         ],
#         "value": [10, 20, 30],
#     }
# )

# report = check_duplicates(unique_df)

# print("Unique-data test report:")
# print(report)

# assert report["Total Rows"] == 3
# assert report["Duplicate Rows"] == 0
# assert report["Duplicate Country-Year-Disease"] == 0

# print("✓ No-duplicate detection works correctly.")

# print("✓ check_duplicates() tests passed.")


# # ==============================================================
# # 4. Test remove_duplicate_records()
# # ==============================================================

# print("\n[3] Testing remove_duplicate_records()...")

# duplicate_test = pd.DataFrame(
#     {
#         "row_num": [1, 2, 3],
#         "country": ["Nigeria", "Nigeria", "Ghana"],
#         "year": [2020, 2020, 2021],
#         "disease_name": [
#             "Malaria",
#             "Malaria",
#             "Ebola",
#         ],
#         "value": [10, 10, 20],
#     }
# )

# cleaned, report = remove_duplicate_records(
#     duplicate_test
# )

# assert len(cleaned) == 2
# assert report["Rows Before"] == 3
# assert report["Duplicates Removed"] == 1
# assert report["Rows After"] == 2

# print("✓ Duplicate records were removed correctly.")
# print(f"✓ Duplicate-removal report: {report}")


# # ==============================================================
# # 5. Test validate_numeric_range()
# # ==============================================================

# print("\n[4] Testing validate_numeric_range()...")

# range_test = pd.DataFrame(
#     {
#         "value": [
#             0,
#             25,
#             50,
#             75,
#             100,
#             -5,
#             105,
#             np.nan,
#         ]
#     }
# )

# report = validate_numeric_range(
#     range_test,
#     "value",
#     minimum=0,
#     maximum=100,
# )

# assert report["Below Minimum"] == 1
# assert report["Above Maximum"] == 1
# assert report["Total Violations"] == 2
# assert report["Passed"] is False

# print("✓ Numeric range violations detected correctly.")
# print(f"✓ Range report: {report}")


# # ==============================================================
# # 6. Test show_range_violations()
# # ==============================================================

# print("\n[5] Testing show_range_violations()...")

# violations = show_range_violations(
#     range_test,
#     "value",
#     minimum=0,
#     maximum=100,
# )

# assert len(violations) == 2
# assert set(violations["value"].tolist()) == {-5, 105}

# print("✓ Range-violation rows returned correctly.")


# # ==============================================================
# # 7. Test repair_age_distribution()
# # ==============================================================

# print("\n[6] Testing repair_age_distribution()...")

# age_test = pd.DataFrame(
#     {
#         "ages_0_18_pct": [20, 150],
#         "ages_19_35_pct": [30, 25],
#         "ages_36_60_pct": [30, 25],
#         "ages_61_plus_pct": [20, 25],
#     }
# )

# repaired, report = repair_age_distribution(
#     age_test
# )

# assert report["Rows Repaired"] == 1

# assert (
#     repaired.loc[1, "ages_0_18_pct"]
#     == 25
# )

# print("✓ Single invalid age-group value was repaired.")
# print(f"✓ Age-repair report: {report}")


# # ==============================================================
# # 8. Test age distribution with multiple invalid values
# # ==============================================================

# print("\n[7] Testing multiple invalid age values...")

# multiple_invalid = pd.DataFrame(
#     {
#         "ages_0_18_pct": [150],
#         "ages_19_35_pct": [130],
#         "ages_36_60_pct": [20],
#         "ages_61_plus_pct": [10],
#     }
# )

# repaired, report = repair_age_distribution(
#     multiple_invalid
# )

# assert report["Rows Repaired"] == 0

# assert repaired.loc[0, "ages_0_18_pct"] == 150
# assert repaired.loc[0, "ages_19_35_pct"] == 130

# print("✓ Rows with multiple invalid age values were preserved.")


# # ==============================================================
# # 9. Test age distribution with missing value
# # ==============================================================

# print("\n[8] Testing age-distribution missing-value edge case...")

# age_missing_test = pd.DataFrame(
#     {
#         "ages_0_18_pct": [150],
#         "ages_19_35_pct": [np.nan],
#         "ages_36_60_pct": [30],
#         "ages_61_plus_pct": [20],
#     }
# )

# repaired, report = repair_age_distribution(
#     age_missing_test
# )

# print("Current function result:")
# print(repaired)

# print(
#     "Checking that invalid age values are not "
#     "repaired when another age-group value is missing..."
# )

# assert report["Rows Repaired"] == 0

# assert (
#     repaired.loc[0, "ages_0_18_pct"]
#     == 150
# )

# print(
#     "✓ Rows with missing age-group values "
#     "were correctly preserved."
# )


# # ==============================================================
# # 10. Test healthcare-access repair
# # ==============================================================

# print("\n[9] Testing repair_healthcare_access()...")

# healthcare_test = pd.DataFrame(
#     {
#         "healthcare_access_pct": [
#             85,
#             100,
#             850,
#             1200,
#             np.nan,
#         ]
#     }
# )

# repaired, report = repair_healthcare_access(
#     healthcare_test
# )

# assert repaired.loc[0, "healthcare_access_pct"] == 85
# assert repaired.loc[1, "healthcare_access_pct"] == 100
# assert repaired.loc[2, "healthcare_access_pct"] == 85
# assert repaired.loc[3, "healthcare_access_pct"] == 12
# assert pd.isna(
#     repaired.loc[4, "healthcare_access_pct"]
# )

# assert report["Rows Above 100 Before"] == 2
# assert report["Rows Above 100 After"] == 0
# assert report["Rows Repaired"] == 2

# print("✓ Healthcare-access decimal errors were repaired.")
# print(f"✓ Healthcare-access report: {report}")


# # ==============================================================
# # 11. Test gender population consistency
# # ==============================================================

# print("\n[10] Testing validate_gender_population()...")

# gender_test = pd.DataFrame(
#     {
#         "population_affected": [
#             100,
#             100,
#             100,
#             np.nan,
#         ],
#         "pop_affected_male": [
#             50,
#             50,
#             40,
#             50,
#         ],
#         "pop_affected_female": [
#             50,
#             51,
#             50,
#             50,
#         ],
#     }
# )

# report, violations = (
#     validate_gender_population(
#         gender_test
#     )
# )

# assert report["Rows Checked"] == 3
# assert report["Rows Skipped (Missing)"] == 1
# assert report["Violations"] == 1
# assert report["Passed"] is False

# print("✓ Gender population consistency validation works.")
# print(f"✓ Gender report: {report}")


# # ==============================================================
# # 12. Test urban/rural validation
# # ==============================================================

# print("\n[11] Testing validate_urban_rural_distribution()...")

# urban_test = pd.DataFrame(
#     {
#         "country": [
#             "Nigeria",
#             "Ghana",
#             "Kenya",
#             "Egypt",
#         ],
#         "year": [
#             2020,
#             2020,
#             2020,
#             2020,
#         ],
#         "disease_name": [
#             "Malaria",
#             "Malaria",
#             "Malaria",
#             "Malaria",
#         ],
#         "pop_affected_urban_pct": [
#             60,
#             70,
#             40,
#             np.nan,
#         ],
#         "pop_affected_rural_pct": [
#             40,
#             25,
#             60,
#             50,
#         ],
#     }
# )

# report, violations = (
#     validate_urban_rural_distribution(
#         urban_test
#     )
# )

# assert report["Rows Checked"] == 3
# assert report["Rows Skipped (Missing)"] == 1
# assert report["Violations"] == 1
# assert report["Passed"] is False

# print("✓ Urban/Rural distribution validation works.")
# print(f"✓ Urban/Rural report: {report}")


# # ==============================================================
# # 13. Test urban/rural repair
# # ==============================================================

# print("\n[12] Testing repair_urban_rural_distribution()...")

# urban_rural_test = pd.DataFrame(
#     {
#         "country": [
#             "Testland",
#             "Examplestan",
#             "Sampleland",
#             "Missingland",
#         ],
#         "year": [
#             2020,
#             2020,
#             2020,
#             2020,
#         ],
#         "disease_name": [
#             "Disease A",
#             "Disease B",
#             "Disease C",
#             "Disease D",
#         ],
#         "pop_affected_urban_pct": [
#             70,
#             30,
#             60,
#             np.nan,
#         ],
#         "pop_affected_rural_pct": [
#             31,
#             69,
#             39,
#             40,
#         ],
#     }
# )

# repaired, repair_report = (
#     repair_urban_rural_distribution(
#         urban_rural_test
#     )
# )

# # --------------------------------------------------
# # 101% total
# # --------------------------------------------------
# # 70 + 31 = 101
# # Urban is larger, so Urban should decrease by 1.
# assert (
#     repaired.loc[0, "pop_affected_urban_pct"]
#     == 69
# )

# assert (
#     repaired.loc[0, "pop_affected_rural_pct"]
#     == 31
# )

# assert (
#     repaired.loc[0, "pop_affected_urban_pct"]
#     + repaired.loc[0, "pop_affected_rural_pct"]
#     == 100
# )

# # --------------------------------------------------
# # 99% total
# # --------------------------------------------------
# # 30 + 69 = 99
# # Rural is larger, so Rural should increase by 1.
# assert (
#     repaired.loc[1, "pop_affected_urban_pct"]
#     == 30
# )

# assert (
#     repaired.loc[1, "pop_affected_rural_pct"]
#     == 70
# )

# assert (
#     repaired.loc[1, "pop_affected_urban_pct"]
#     + repaired.loc[1, "pop_affected_rural_pct"]
#     == 100
# )

# # --------------------------------------------------
# # Another 99% case
# # --------------------------------------------------
# # 60 + 39 = 99
# # Urban is larger, so Urban should increase by 1.
# assert (
#     repaired.loc[2, "pop_affected_urban_pct"]
#     == 61
# )

# assert (
#     repaired.loc[2, "pop_affected_rural_pct"]
#     == 39
# )

# assert (
#     repaired.loc[2, "pop_affected_urban_pct"]
#     + repaired.loc[2, "pop_affected_rural_pct"]
#     == 100
# )

# # --------------------------------------------------
# # Missing-value case
# # --------------------------------------------------
# # Rows with missing Urban/Rural values should not
# # be modified.
# assert pd.isna(
#     repaired.loc[3, "pop_affected_urban_pct"]
# )

# assert (
#     repaired.loc[3, "pop_affected_rural_pct"]
#     == 40
# )

# # --------------------------------------------------
# # Check repair report
# # --------------------------------------------------
# assert repair_report["Rows Repaired"] == 3

# print(
#     "✓ Urban/Rural rounding errors were repaired correctly."
# )

# print(
#     f"✓ Urban/Rural repair report: {repair_report}"
# )


# # ==============================================================
# # 14. Test population affected constraint
# # ==============================================================

# print("\n[13] Testing validate_population_affected()...")

# population_test = pd.DataFrame(
#     {
#         "country": [
#             "Nigeria",
#             "Ghana",
#             "Kenya",
#         ],
#         "year": [
#             2020,
#             2020,
#             2020,
#         ],
#         "disease_name": [
#             "Malaria",
#             "Ebola",
#             "Dengue",
#         ],
#         "population_affected": [
#             100,
#             200,
#             np.nan,
#         ],
#         "country_pop": [
#             150,
#             150,
#             100,
#         ],
#     }
# )

# report, violations = (
#     validate_population_affected(
#         population_test
#     )
# )

# assert report["Rows Checked"] == 2
# assert report["Rows Skipped (Missing)"] == 1
# assert report["Violations"] == 1
# assert report["Passed"] is False

# print("✓ Population constraint validation works.")
# print(f"✓ Population report: {report}")


# # ==============================================================
# # 15. Test Composite Health Index validation
# # ==============================================================

# print("\n[14] Testing validate_chi()...")

# chi_test = pd.DataFrame(
#     {
#         "composite_health_index": [
#             0,
#             25,
#             50,
#             100,
#             -1,
#             101,
#             np.nan,
#         ]
#     }
# )

# report = validate_chi(chi_test)

# assert report["Below Minimum"] == 1
# assert report["Above Maximum"] == 1
# assert report["Total Violations"] == 2
# assert report["Passed"] is False

# print("✓ Composite Health Index range validation works.")
# print(f"✓ CHI report: {report}")


# # ==============================================================
# # 16. Test country-year consistency
# # ==============================================================

# print("\n[15] Testing validate_country_year_consistency()...")

# consistency_test = pd.DataFrame(
#     {
#         "country": [
#             "Nigeria",
#             "Nigeria",
#             "Nigeria",
#             "Ghana",
#             "Ghana",
#         ],
#         "year": [
#             2020,
#             2020,
#             2020,
#             2020,
#             2020,
#         ],
#         "disease_name": [
#             "Malaria",
#             "Ebola",
#             "Dengue",
#             "Malaria",
#             "Ebola",
#         ],
#         "country_pop": [
#             200,
#             200,
#             250,
#             300,
#             300,
#         ],
#     }
# )

# report, violations = (
#     validate_country_year_consistency(
#         consistency_test,
#         "country_pop",
#     )
# )

# assert report["Country-Year Groups Checked"] == 2
# assert report["Inconsistent Groups"] == 1
# assert report["Passed"] is False
# assert len(violations) == 3

# print("✓ Country-Year consistency validation works.")
# print(f"✓ Consistency report: {report}")


# # ==============================================================
# # 17. Test clean_and_validate_data()
# # ==============================================================

# print("\n[16] Running complete clean_and_validate_data()...")

# prepared_df = df.copy()

# original_rows = len(prepared_df)
# original_columns = list(prepared_df.columns)

# validated_df, reports = (
#     clean_and_validate_data(
#         prepared_df
#     )
# )

# print("✓ Complete validation workflow executed.")


# # ==============================================================
# # 18. Check report structure
# # ==============================================================

# print("\n[17] Checking validation report structure...")

# assert isinstance(reports, dict)

# assert "repairs" in reports
# assert "validations" in reports

# expected_repairs = {
#     "duplicate_records",
#     "age_distribution",
#     "healthcare_access",
#     "urban_rural",
# }

# for key in expected_repairs:
#     assert key in reports["repairs"]
#     print(f"✓ Repair report found: {key}")


# expected_validations = {
#     "duplicate",
#     "chi",
#     "gender_population",
#     "urban_rural",
#     "population_constraint",
#     "country_year_consistency",
# }

# for key in expected_validations:
#     assert key in reports["validations"]
#     print(f"✓ Validation report found: {key}")


# # ==============================================================
# # 19. Check country-year validation reports
# # ==============================================================

# print("\n[18] Checking configured Country-Year validations...")

# for column in COUNTRY_YEAR_COLUMNS:

#     assert column in (
#         reports["validations"][
#             "country_year_consistency"
#         ]
#     )

#     print(
#         f"✓ Country-Year validation found: {column}"
#     )


# # ==============================================================
# # 20. Check row preservation
# # ==============================================================

# print("\n[19] Checking final row count...")

# print(
#     f"Rows before validation: {original_rows:,}"
# )

# print(
#     f"Rows after validation: {len(validated_df):,}"
# )

# duplicates_removed = reports[
#     "repairs"
# ]["duplicate_records"][
#     "Duplicates Removed"
# ]

# assert (
#     len(validated_df)
#     == original_rows - duplicates_removed
# )

# print("✓ Final row count is consistent with duplicate removal.")


# # ==============================================================
# # 21. Check column preservation
# # ==============================================================

# print("\n[20] Checking column preservation...")

# assert list(validated_df.columns) == original_columns

# print("✓ All original columns were preserved.")


# # ==============================================================
# # 22. Check input DataFrame preservation
# # ==============================================================

# print("\n[21] Checking input DataFrame preservation...")

# assert list(prepared_df.columns) == original_columns
# assert len(prepared_df) == original_rows

# print("✓ Original DataFrame was not modified.")


# # ==============================================================
# # 23. Inspect final validation results
# # ==============================================================

# print("\n[22] Validation summary...")

# print("\n--- Repairs ---")

# for name, report in reports["repairs"].items():

#     print(f"\n{name}")

#     if isinstance(report, dict):

#         for key, value in report.items():
#             print(f"{key}: {value}")

#     else:
#         print(report)


# print("\n--- Validations ---")

# for name, result in reports["validations"].items():

#     print(f"\n{name}")

#     if name == "country_year_consistency":

#         for column, result_data in result.items():

#             print(
#                 f"{column}: "
#                 f"{result_data['report']}"
#             )

#     else:

#         print(
#             result["report"]
#         )


# # ==============================================================
# # Final result
# # ==============================================================

# print("\n" + "=" * 70)
# print("✓ VALIDATION MODULE TEST PASSED")
# print("=" * 70)

# print(
#     """
# The validation module successfully:

#   ✓ Detected exact duplicate records
#   ✓ Detected Country-Year-Disease duplicates
#   ✓ Removed duplicate records
#   ✓ Validated numeric ranges
#   ✓ Returned range-violation rows
#   ✓ Repaired single invalid age-group values
#   ✓ Preserved rows with multiple invalid age values
#   ✓ Repaired healthcare-access decimal errors
#   ✓ Validated gender population consistency
#   ✓ Validated Urban/Rural population distribution
#   ✓ Repaired small Urban/Rural rounding errors
#   ✓ Validated population affected constraints
#   ✓ Validated Composite Health Index ranges
#   ✓ Validated Country-Year consistency
#   ✓ Executed the complete validation workflow
#   ✓ Generated all expected repair reports
#   ✓ Generated all expected validation reports
#   ✓ Preserved the expected column structure
#   ✓ Preserved the input DataFrame
# """
# )















# ==============================================================
# Testing repair_age_distribution()
# ==============================================================
from validation import repair_age_distribution
import pandas as pd
import numpy as np

# print("\n[6] Testing repair_age_distribution()...")

# age_test_df = pd.DataFrame({
#     "ages_0_18_pct": [150],
#     "ages_19_35_pct": [20],
#     "ages_36_60_pct": [30],
#     "ages_61_plus_pct": [20],
# })

# repaired, report = repair_age_distribution(
#     age_test_df
# )

# assert report["Rows Repaired"] == 1

# assert repaired.loc[
#     0,
#     "ages_0_18_pct"
# ] == 30

# assert (
#     repaired.loc[
#         0,
#         [
#             "ages_0_18_pct",
#             "ages_19_35_pct",
#             "ages_36_60_pct",
#             "ages_61_plus_pct",
#         ],
#     ].sum()
#     == 100
# )

# print("✓ Single invalid age-group value was repaired.")
# print(f"✓ Age-repair report: {report}")


# # ==============================================================
# # Test multiple invalid age values
# # ==============================================================

# print("\n[7] Testing multiple invalid age values...")

# multiple_invalid_df = pd.DataFrame({
#     "ages_0_18_pct": [150],
#     "ages_19_35_pct": [-10],
#     "ages_36_60_pct": [30],
#     "ages_61_plus_pct": [20],
# })

# repaired, report = repair_age_distribution(
#     multiple_invalid_df
# )

# assert report["Rows Repaired"] == 0

# assert repaired.loc[
#     0,
#     "ages_0_18_pct"
# ] == 150

# assert repaired.loc[
#     0,
#     "ages_19_35_pct"
# ] == -10

# print("✓ Rows with multiple invalid age values were preserved.")


# # ==============================================================
# # Test invalid value with another missing value
# # ==============================================================

# print("\n[8] Testing invalid age value with another missing value...")

# invalid_missing_df = pd.DataFrame({
#     "ages_0_18_pct": [150],
#     "ages_19_35_pct": [np.nan],
#     "ages_36_60_pct": [30],
#     "ages_61_plus_pct": [20],
# })

# repaired, report = repair_age_distribution(
#     invalid_missing_df
# )

# assert report["Rows Repaired"] == 0

# assert repaired.loc[
#     0,
#     "ages_0_18_pct"
# ] == 150

# assert pd.isna(
#     repaired.loc[
#         0,
#         "ages_19_35_pct"
#     ]
# )

# print("✓ Invalid values were preserved when another age-group value was missing.")


# # ==============================================================
# # Test exactly one missing age-group value
# # ==============================================================

# print("\n[9] Testing single missing age-group value...")

# single_missing_df = pd.DataFrame({
#     "ages_0_18_pct": [20],
#     "ages_19_35_pct": [30],
#     "ages_36_60_pct": [25],
#     "ages_61_plus_pct": [np.nan],
# })

# repaired, report = repair_age_distribution(
#     single_missing_df
# )

# assert report["Rows Repaired"] == 1

# assert repaired.loc[
#     0,
#     "ages_61_plus_pct"
# ] == 25

# assert (
#     repaired.loc[
#         0,
#         [
#             "ages_0_18_pct",
#             "ages_19_35_pct",
#             "ages_36_60_pct",
#             "ages_61_plus_pct",
#         ],
#     ].sum()
#     == 100
# )

# print("✓ Single missing age-group value was correctly calculated.")
# print(f"✓ Missing-value repair report: {report}")


# # ==============================================================
# # Test multiple missing age-group values
# # ==============================================================

# print("\n[10] Testing multiple missing age-group values...")

# multiple_missing_df = pd.DataFrame({
#     "ages_0_18_pct": [20],
#     "ages_19_35_pct": [np.nan],
#     "ages_36_60_pct": [np.nan],
#     "ages_61_plus_pct": [25],
# })

# repaired, report = repair_age_distribution(
#     multiple_missing_df
# )

# assert report["Rows Repaired"] == 0

# assert pd.isna(
#     repaired.loc[
#         0,
#         "ages_19_35_pct"
#     ]
# )

# assert pd.isna(
#     repaired.loc[
#         0,
#         "ages_36_60_pct"
#     ]
# )

# print("✓ Rows with multiple missing age-group values were preserved.")


# # ==============================================================
# # Test missing value where known values sum to 100
# # ==============================================================

# print("\n[11] Testing missing value when known values already sum to 100...")

# invalid_missing_sum_df = pd.DataFrame({
#     "ages_0_18_pct": [40],
#     "ages_19_35_pct": [30],
#     "ages_36_60_pct": [30],
#     "ages_61_plus_pct": [np.nan],
# })

# repaired, report = repair_age_distribution(
#     invalid_missing_sum_df
# )

# assert report["Rows Repaired"] == 0

# assert pd.isna(
#     repaired.loc[
#         0,
#         "ages_61_plus_pct"
#     ]
# )

# print("✓ Missing value was preserved when no valid percentage remained.")


# # ==============================================================
# # Test missing value where known values exceed 100
# # ==============================================================

# print("\n[12] Testing missing value when known values exceed 100...")

# excessive_sum_df = pd.DataFrame({
#     "ages_0_18_pct": [50],
#     "ages_19_35_pct": [40],
#     "ages_36_60_pct": [20],
#     "ages_61_plus_pct": [np.nan],
# })

# repaired, report = repair_age_distribution(
#     excessive_sum_df
# )

# assert report["Rows Repaired"] == 0

# assert pd.isna(
#     repaired.loc[
#         0,
#         "ages_61_plus_pct"
#     ]
# )

# print("✓ Missing value was preserved when known percentages exceeded 100.")


# # ==============================================================
# # Test complete valid distribution
# # ==============================================================

# print("\n[13] Testing already-valid age distribution...")

# valid_age_df = pd.DataFrame({
#     "ages_0_18_pct": [20],
#     "ages_19_35_pct": [30],
#     "ages_36_60_pct": [25],
#     "ages_61_plus_pct": [25],
# })

# repaired, report = repair_age_distribution(
#     valid_age_df
# )

# assert report["Rows Repaired"] == 0

# pd.testing.assert_frame_equal(
#     repaired,
#     valid_age_df,
# )

# print("✓ Valid age distributions were left unchanged.")


# print("\n✓ repair_age_distribution() tests passed.")












# # ==========================================================
# # VALIDATION REPORT MODULE TEST
# # ==========================================================

# print("\n" + "=" * 70)
# print("VALIDATION REPORT MODULE TEST")
# print("=" * 70)

# from validation_report import build_validation_report


# # ----------------------------------------------------------
# # Test 1: Build complete validation report
# # ----------------------------------------------------------

# print("\n[1] Testing build_validation_report()...")

# test_reports = {
#     "missing_values": {
#         "improvement": {
#             "Column": "improvement_in_5_years_pct",
#             "Action": (
#                 "Preserved structural missing values "
#                 "(earliest years lack sufficient historical data)"
#             ),
#             "Missing Before": 2002,
#             "Missing After": 2002,
#         }
#     },

#     "repairs": {
#         "duplicate_records": {
#             "Rows Before": 10005,
#             "Duplicates Removed": 5,
#             "Rows After": 10000,
#         },

#         "age_distribution": {
#             "Rows Repaired": 4,
#         },

#         "healthcare_access": {
#             "Column": "healthcare_access_pct",
#             "Rows Above 100 Before": 5,
#             "Rows Above 100 After": 0,
#             "Rows Repaired": 5,
#         },

#         "urban_rural": {
#             "Rows Repaired": 702,
#         },
#     },

#     "validations": {
#         "gender_population": {
#             "report": {
#                 "Rows Checked": 9000,
#                 "Rows Skipped (Missing)": 1000,
#                 "Violations": 0,
#                 "Passed": True,
#             },
#             "violations": None,
#         },

#         "population_constraint": {
#             "report": {
#                 "Rows Checked": 9000,
#                 "Rows Skipped (Missing)": 1000,
#                 "Violations": 0,
#                 "Passed": True,
#             },
#             "violations": None,
#         },

#         "chi": {
#             "report": {
#                 "Column": "composite_health_index",
#                 "Minimum": 0,
#                 "Maximum": 100,
#                 "Below Minimum": 0,
#                 "Above Maximum": 0,
#                 "Total Violations": 0,
#                 "Passed": True,
#             },
#             "violations": None,
#         },

#         "country_year_consistency": {
#             "country_pop": {
#                 "report": {
#                     "Column": "country_pop",
#                     "Country-Year Groups Checked": 500,
#                     "Inconsistent Groups": 0,
#                     "Passed": True,
#                 },
#                 "violations": None,
#             },

#             "per_capita_income_usd": {
#                 "report": {
#                     "Column": "per_capita_income_usd",
#                     "Country-Year Groups Checked": 500,
#                     "Inconsistent Groups": 0,
#                     "Passed": True,
#                 },
#                 "violations": None,
#             },

#             "education_index": {
#                 "report": {
#                     "Column": "education_index",
#                     "Country-Year Groups Checked": 500,
#                     "Inconsistent Groups": 0,
#                     "Passed": True,
#                 },
#                 "violations": None,
#             },

#             "urbanization_rate_pct": {
#                 "report": {
#                     "Column": "urbanization_rate_pct",
#                     "Country-Year Groups Checked": 500,
#                     "Inconsistent Groups": 0,
#                     "Passed": True,
#                 },
#                 "violations": None,
#             },

#             # These are expected to vary by disease.
#             "healthcare_access_pct": {
#                 "report": {
#                     "Column": "healthcare_access_pct",
#                     "Country-Year Groups Checked": 500,
#                     "Inconsistent Groups": 500,
#                     "Passed": False,
#                 },
#                 "violations": None,
#             },

#             "doctors_per_1000": {
#                 "report": {
#                     "Column": "doctors_per_1000",
#                     "Country-Year Groups Checked": 500,
#                     "Inconsistent Groups": 500,
#                     "Passed": False,
#                 },
#                 "violations": None,
#             },

#             "hospital_beds_per_1000": {
#                 "report": {
#                     "Column": "hospital_beds_per_1000",
#                     "Country-Year Groups Checked": 500,
#                     "Inconsistent Groups": 500,
#                     "Passed": False,
#                 },
#                 "violations": None,
#             },

#             "composite_health_index": {
#                 "report": {
#                     "Column": "composite_health_index",
#                     "Country-Year Groups Checked": 500,
#                     "Inconsistent Groups": 500,
#                     "Passed": False,
#                 },
#                 "violations": None,
#             },
#         },
#     },
# }

# validation_report = build_validation_report(
#     test_reports
# )

# print(validation_report)

# assert isinstance(
#     validation_report,
#     pd.DataFrame,
# )

# print("✓ Validation report DataFrame generated correctly.")


# # ----------------------------------------------------------
# # Test 2: Check required columns
# # ----------------------------------------------------------

# print("\n[2] Checking report columns...")

# expected_columns = [
#     "Validation",
#     "Status",
#     "Action",
# ]

# assert list(validation_report.columns) == expected_columns

# print("✓ Expected report columns are present.")


# # ----------------------------------------------------------
# # Test 3: Check expected number of rows
# # ----------------------------------------------------------

# print("\n[3] Checking report row count...")

# # 2 missing-value entries
# # 4 repair entries
# # 3 direct validations
# # 8 Country-Year consistency entries
# #
# # Total = 18

# expected_rows = 18

# assert len(validation_report) == expected_rows

# print(
#     f"✓ Expected number of report rows confirmed: "
#     f"{expected_rows}"
# )


# # ----------------------------------------------------------
# # Test 4: Check Missing Values report
# # ----------------------------------------------------------

# print("\n[4] Checking Missing Values report...")

# missing_row = validation_report[
#     validation_report["Validation"]
#     == "Missing Values"
# ]

# assert len(missing_row) == 1

# assert missing_row.iloc[0]["Status"] == "Passed"

# print("✓ Missing Values report generated correctly.")


# # ----------------------------------------------------------
# # Test 5: Check Improvement in 5 Years report
# # ----------------------------------------------------------

# print("\n[5] Checking Improvement in 5 Years report...")

# improvement_row = validation_report[
#     validation_report["Validation"]
#     == "Improvement in 5 Years (%)"
# ]

# assert len(improvement_row) == 1

# assert improvement_row.iloc[0]["Status"] == "Passed"

# assert "2,002" in improvement_row.iloc[0]["Action"]

# assert "structural missing values" in (
#     improvement_row.iloc[0]["Action"]
# )

# print("✓ Improvement report generated correctly.")


# # ----------------------------------------------------------
# # Test 6: Check repair summaries
# # ----------------------------------------------------------

# print("\n[6] Checking repair summaries...")

# duplicate_row = validation_report[
#     validation_report["Validation"]
#     == "Duplicate Records"
# ]

# assert len(duplicate_row) == 1
# assert duplicate_row.iloc[0]["Status"] == "Passed"
# assert "5" in duplicate_row.iloc[0]["Action"]


# age_row = validation_report[
#     validation_report["Validation"]
#     == "Age Distribution"
# ]

# assert len(age_row) == 1
# assert age_row.iloc[0]["Status"] == "Passed"
# assert "4" in age_row.iloc[0]["Action"]


# healthcare_row = validation_report[
#     validation_report["Validation"]
#     == "Healthcare Access Repair"
# ]

# assert len(healthcare_row) == 1
# assert healthcare_row.iloc[0]["Status"] == "Passed"
# assert "5" in healthcare_row.iloc[0]["Action"]


# urban_row = validation_report[
#     validation_report["Validation"]
#     == "Urban/Rural Distribution"
# ]

# assert len(urban_row) == 1
# assert urban_row.iloc[0]["Status"] == "Passed"
# assert "702" in urban_row.iloc[0]["Action"]

# print("✓ Repair summaries generated correctly.")


# # ----------------------------------------------------------
# # Test 7: Check passed validations
# # ----------------------------------------------------------

# print("\n[7] Checking passed validations...")

# gender_row = validation_report[
#     validation_report["Validation"]
#     == "Gender Population Consistency"
# ]

# assert gender_row.iloc[0]["Status"] == "Passed"

# assert (
#     "Male + Female population equals"
#     in gender_row.iloc[0]["Action"]
# )


# population_row = validation_report[
#     validation_report["Validation"]
#     == "Population Constraint"
# ]

# assert population_row.iloc[0]["Status"] == "Passed"

# assert (
#     "never exceeds"
#     in population_row.iloc[0]["Action"]
# )


# chi_row = validation_report[
#     validation_report["Validation"]
#     == "Composite Health Index Range"
# ]

# assert chi_row.iloc[0]["Status"] == "Passed"

# assert (
#     "between 0 and 100"
#     in chi_row.iloc[0]["Action"]
# )

# print("✓ Passed validation summaries generated correctly.")


# # ----------------------------------------------------------
# # Test 8: Check informational validations
# # ----------------------------------------------------------

# print("\n[8] Checking informational Country-Year validations...")

# informational_columns = [
#     "Healthcare Access (%) Consistency",
#     "Doctors per 1000 Consistency",
#     "Hospital Beds per 1000 Consistency",
#     "Composite Health Index (CHI) Consistency",
# ]

# for validation_name in informational_columns:

#     row = validation_report[
#         validation_report["Validation"]
#         == validation_name
#     ]

#     assert len(row) == 1

#     assert row.iloc[0]["Status"] == "Informational"

#     assert (
#         "varies by disease"
#         in row.iloc[0]["Action"]
#     )

# print(
#     "✓ Informational Country-Year validations "
#     "were handled correctly."
# )


# # ----------------------------------------------------------
# # Test 9: Check standard Country-Year validations
# # ----------------------------------------------------------

# print("\n[9] Checking standard Country-Year validations...")

# standard_consistency_columns = [
#     "Country Population Consistency",
#     "Per Capita Income (USD) Consistency",
#     "Education Index Consistency",
#     "Urbanization Rate (%) Consistency",
# ]

# for validation_name in standard_consistency_columns:

#     row = validation_report[
#         validation_report["Validation"]
#         == validation_name
#     ]

#     assert len(row) == 1

#     assert row.iloc[0]["Status"] == "Passed"

#     assert (
#         "consistent across all Country-Year groups"
#         in row.iloc[0]["Action"]
#     )

# print(
#     "✓ Standard Country-Year validations "
#     "were handled correctly."
# )


# # ----------------------------------------------------------
# # Test 10: Test failed validation handling
# # ----------------------------------------------------------

# print("\n[10] Testing failed validation handling...")

# failed_reports = test_reports.copy()

# failed_reports["validations"] = {
#     **test_reports["validations"],
#     "gender_population": {
#         "report": {
#             "Rows Checked": 10,
#             "Rows Skipped (Missing)": 0,
#             "Violations": 3,
#             "Passed": False,
#         },
#         "violations": None,
#     },
# }

# failed_report = build_validation_report(
#     failed_reports
# )

# failed_gender_row = failed_report[
#     failed_report["Validation"]
#     == "Gender Population Consistency"
# ]

# assert len(failed_gender_row) == 1

# assert (
#     failed_gender_row.iloc[0]["Status"]
#     == "Failed"
# )

# assert (
#     "3 rows violate"
#     in failed_gender_row.iloc[0]["Action"]
# )

# print("✓ Failed validation status handled correctly.")


# # ----------------------------------------------------------
# # Test 11: Check display names
# # ----------------------------------------------------------

# print("\n[11] Checking Country-Year display names...")

# expected_display_names = [
#     "Country Population Consistency",
#     "Per Capita Income (USD) Consistency",
#     "Education Index Consistency",
#     "Urbanization Rate (%) Consistency",
#     "Healthcare Access (%) Consistency",
#     "Doctors per 1000 Consistency",
#     "Hospital Beds per 1000 Consistency",
#     "Composite Health Index (CHI) Consistency",
# ]

# for name in expected_display_names:

#     assert name in (
#         validation_report["Validation"].values
#     )

# print("✓ Human-readable Country-Year labels are correct.")


# # ----------------------------------------------------------
# # Test 12: Check no unexpected statuses
# # ----------------------------------------------------------

# print("\n[12] Checking report status values...")

# allowed_statuses = {
#     "Passed",
#     "Failed",
#     "Informational",
# }

# actual_statuses = set(
#     validation_report["Status"]
# )

# assert actual_statuses.issubset(
#     allowed_statuses
# )

# print(
#     "✓ All report statuses use valid "
#     "status values."
# )


# # ----------------------------------------------------------
# # Test 13: Check action descriptions are populated
# # ----------------------------------------------------------

# print("\n[13] Checking report action descriptions...")

# assert (
#     validation_report["Action"]
#     .notna()
#     .all()
# )

# assert (
#     validation_report["Action"]
#     .astype(str)
#     .str.strip()
#     .ne("")
#     .all()
# )

# print("✓ All validation rows contain action descriptions.")


# # ----------------------------------------------------------
# # Final result
# # ----------------------------------------------------------

# print("\n" + "=" * 70)
# print("✓ VALIDATION REPORT MODULE TEST PASSED")
# print("=" * 70)

# print(
#     """
# The validation-report module successfully:

#   ✓ Built the validation summary DataFrame
#   ✓ Generated all expected report sections
#   ✓ Preserved the expected report structure
#   ✓ Generated missing-value summaries
#   ✓ Generated improvement-in-five-years summaries
#   ✓ Generated duplicate-removal summaries
#   ✓ Generated age-distribution repair summaries
#   ✓ Generated healthcare-access repair summaries
#   ✓ Generated Urban/Rural repair summaries
#   ✓ Generated gender-population validation summaries
#   ✓ Generated population-constraint summaries
#   ✓ Generated Composite Health Index summaries
#   ✓ Correctly handled Country-Year consistency checks
#   ✓ Correctly classified informational validations
#   ✓ Correctly converted passed validations to "Passed"
#   ✓ Correctly converted failed validations to "Failed"
#   ✓ Generated human-readable indicator names
#   ✓ Generated non-empty action descriptions
# """
# )









# # ============================================================
# # PIPELINE MODULE TEST
# # ============================================================

# print("\n" + "=" * 70)
# print("PIPELINE MODULE TEST")
# print("=" * 70)


# # ------------------------------------------------------------
# # Imports
# # ------------------------------------------------------------
# from pipeline import run_pipeline
# from config import RAW_PATH


# # ------------------------------------------------------------
# # [1] Running complete pipeline
# # ------------------------------------------------------------
# print("\n[1] Running complete data-cleaning pipeline...")

# clean_df, reports, summary_report = run_pipeline(RAW_PATH)

# print("✓ Pipeline executed successfully.")


# # ------------------------------------------------------------
# # [2] Checking final dataset dimensions
# # ------------------------------------------------------------
# print("\n[2] Checking final dataset dimensions...")

# print(f"Rows: {len(clean_df):,}")
# print(f"Columns: {len(clean_df.columns)}")

# assert len(clean_df) == 10_000, (
#     f"Expected 10,000 rows, got {len(clean_df)}"
# )

# assert len(clean_df.columns) == 30, (
#     f"Expected 30 columns, got {len(clean_df.columns)}"
# )

# print("✓ Final dataset dimensions are correct.")


# # ------------------------------------------------------------
# # [3] Checking that column names are normalized
# # ------------------------------------------------------------
# print("\n[3] Checking normalized column names...")

# expected_columns = {
#     "country",
#     "year",
#     "disease_name",
#     "treatment_type",
#     "population_affected",
#     "pop_affected_male",
#     "pop_affected_female",
#     "pop_affected_urban_pct",
#     "pop_affected_rural_pct",
#     "ages_0_18_pct",
#     "ages_19_35_pct",
#     "ages_36_60_pct",
#     "ages_61_plus_pct",
#     "healthcare_access_pct",
#     "country_pop",
#     "per_capita_income_usd",
#     "education_index",
#     "urbanization_rate_pct",
#     "doctors_per_1000",
#     "hospital_beds_per_1000",
#     "composite_health_index",
# }

# missing_columns = (
#     expected_columns
#     - set(clean_df.columns)
# )

# assert not missing_columns, (
#     f"Expected normalized columns missing: "
#     f"{missing_columns}"
# )

# print("✓ Column names are normalized correctly.")


# # ------------------------------------------------------------
# # [4] Checking pipeline report structure
# # ------------------------------------------------------------
# print("\n[4] Checking pipeline report structure...")

# expected_report_sections = {
#     "pipeline",
#     "numeric_conversion",
#     "missing_values",
#     "repairs",
#     "validations",
# }

# assert set(reports.keys()) == expected_report_sections

# print("✓ All expected pipeline report sections are present.")


# # ------------------------------------------------------------
# # [5] Checking pipeline metadata
# # ------------------------------------------------------------
# print("\n[5] Checking pipeline metadata...")

# pipeline_report = reports["pipeline"]

# assert (
#     pipeline_report["rows_after_pipeline"]
#     == len(clean_df)
# )

# assert (
#     pipeline_report["columns_after_pipeline"]
#     == len(clean_df.columns)
# )

# print(
#     "✓ Pipeline metadata matches the final dataset."
# )


# # ------------------------------------------------------------
# # [6] Checking numeric conversion report
# # ------------------------------------------------------------
# print("\n[6] Checking numeric conversion report...")

# assert reports["numeric_conversion"] is not None

# print(
#     "✓ Numeric conversion report generated."
# )

# print(
#     "Numeric conversion report type:",
#     type(
#         reports["numeric_conversion"]
#     ).__name__,
# )


# # ------------------------------------------------------------
# # [7] Checking missing-value report
# # ------------------------------------------------------------
# print("\n[7] Checking missing-value report...")

# assert reports["missing_values"] is not None

# print(
#     "✓ Missing-value report generated."
# )

# print(
#     "Missing-value report type:",
#     type(
#         reports["missing_values"]
#     ).__name__,
# )


# # ------------------------------------------------------------
# # [8] Checking repair reports
# # ------------------------------------------------------------
# print("\n[8] Checking repair reports...")

# expected_repairs = {
#     "duplicate_records",
#     "age_distribution",
#     "healthcare_access",
#     "urban_rural",
# }

# assert expected_repairs.issubset(
#     reports["repairs"].keys()
# )

# for repair in expected_repairs:
#     print(f"✓ Repair report found: {repair}")


# # ------------------------------------------------------------
# # [9] Checking validation reports
# # ------------------------------------------------------------
# print("\n[9] Checking validation reports...")

# expected_validations = {
#     "duplicate",
#     "chi",
#     "gender_population",
#     "urban_rural",
#     "population_constraint",
#     "country_year_consistency",
# }

# assert expected_validations.issubset(
#     reports["validations"].keys()
# )

# for validation in expected_validations:
#     print(f"✓ Validation report found: {validation}")


# # ------------------------------------------------------------
# # [10] Checking Country-Year validations
# # ------------------------------------------------------------
# print("\n[10] Checking Country-Year validations...")

# expected_country_year_columns = {
#     "country_pop",
#     "per_capita_income_usd",
#     "education_index",
#     "urbanization_rate_pct",
#     "healthcare_access_pct",
#     "doctors_per_1000",
#     "hospital_beds_per_1000",
#     "composite_health_index",
# }

# country_year_reports = reports[
#     "validations"
# ]["country_year_consistency"]

# assert expected_country_year_columns.issubset(
#     country_year_reports.keys()
# )

# for column in expected_country_year_columns:
#     print(
#         f"✓ Country-Year validation found: {column}"
#     )


# # ------------------------------------------------------------
# # [11] Checking validation summary
# # ------------------------------------------------------------
# print("\n[11] Checking validation summary...")

# assert isinstance(
#     summary_report,
#     pd.DataFrame,
# )

# expected_summary_columns = {
#     "Validation",
#     "Status",
#     "Action",
# }

# assert expected_summary_columns.issubset(
#     summary_report.columns
# )

# print("✓ Validation summary DataFrame generated.")
# print(summary_report)


# # ------------------------------------------------------------
# # [12] Checking validation summary row count
# # ------------------------------------------------------------
# print("\n[12] Checking validation summary row count...")

# assert len(summary_report) == 18, (
#     f"Expected 18 summary rows, "
#     f"got {len(summary_report)}"
# )

# print(
#     f"✓ Expected validation summary rows confirmed: "
#     f"{len(summary_report)}"
# )


# # ------------------------------------------------------------
# # [13] Checking final duplicate status
# # ------------------------------------------------------------
# print("\n[13] Checking duplicate validation...")

# duplicate_report = (
#     reports["validations"]["duplicate"]["report"]
# )

# assert duplicate_report["Duplicate Rows"] == 0
# assert (
#     duplicate_report["Duplicate Country-Year-Disease"]
#     == 0
# )

# print("✓ Final dataset contains no duplicate records.")


# # ------------------------------------------------------------
# # [14] Checking final validation results
# # ------------------------------------------------------------
# print("\n[14] Checking final validation results...")

# chi_report = (
#     reports["validations"]["chi"]["report"]
# )

# gender_report = (
#     reports["validations"]["gender_population"]
#     ["report"]
# )

# urban_report = (
#     reports["validations"]["urban_rural"]
#     ["report"]
# )

# population_report = (
#     reports["validations"]["population_constraint"]
#     ["report"]
# )

# assert chi_report["Passed"] is True
# assert gender_report["Passed"] is True
# assert urban_report["Passed"] is True
# assert population_report["Passed"] is True

# print("✓ Core validation checks passed.")


# # ------------------------------------------------------------
# # [15] Checking repair counts
# # ------------------------------------------------------------
# print("\n[15] Checking repair results...")

# repairs = reports["repairs"]

# print(
#     "Duplicate records removed:",
#     repairs["duplicate_records"][
#         "Duplicates Removed"
#     ],
# )

# print(
#     "Age distributions repaired:",
#     repairs["age_distribution"][
#         "Rows Repaired"
#     ],
# )

# print(
#     "Healthcare access values repaired:",
#     repairs["healthcare_access"][
#         "Rows Repaired"
#     ],
# )

# print(
#     "Urban/Rural distributions repaired:",
#     repairs["urban_rural"][
#         "Rows Repaired"
#     ],
# )

# assert (
#     repairs["duplicate_records"]
#     ["Duplicates Removed"] == 5
# )

# assert (
#     repairs["age_distribution"]
#     ["Rows Repaired"] == 4
# )

# assert (
#     repairs["healthcare_access"]
#     ["Rows Repaired"] == 5
# )

# assert (
#     repairs["urban_rural"]
#     ["Rows Repaired"] == 702
# )

# print("✓ Expected repair counts confirmed.")


# # ------------------------------------------------------------
# # [16] Checking input pipeline path
# # ------------------------------------------------------------
# print("\n[16] Checking pipeline input...")

# assert RAW_PATH is not None

# print(f"✓ Pipeline input path configured: {RAW_PATH}")


# # ------------------------------------------------------------
# # [17] Final summary
# # ------------------------------------------------------------
# print("\n" + "=" * 70)
# print("✓ PIPELINE MODULE TEST PASSED")
# print("=" * 70)

# print(
#     """
# The pipeline successfully:

#   ✓ Loaded the raw dataset
#   ✓ Applied upstream column-name normalization
#   ✓ Cleaned text columns
#   ✓ Converted numeric columns
#   ✓ Handled missing values
#   ✓ Removed duplicate records
#   ✓ Repaired age distributions
#   ✓ Repaired healthcare-access values
#   ✓ Repaired Urban/Rural percentages
#   ✓ Performed validation checks
#   ✓ Generated pipeline reports
#   ✓ Generated validation summary
#   ✓ Preserved the expected dataset dimensions
#   ✓ Produced the expected repair results
# """
# )







# # ======================================================================
# # EXPORT MODULE TEST
# # ======================================================================

# import os
# import tempfile
# from pathlib import Path

# import pandas as pd

# from export import (
#     save_cleaned_data,
#     save_validation_report,
# )


# print()
# print("=" * 70)
# print("EXPORT MODULE TEST")
# print("=" * 70)


# # ----------------------------------------------------------------------
# # Test data
# # ----------------------------------------------------------------------

# test_clean_df = pd.DataFrame(
#     {
#         "country": ["Nigeria", "Canada", "Italy"],
#         "year": [2020, 2021, 2022],
#         "disease_name": [
#             "Malaria",
#             "Cancer",
#             "Diabetes",
#         ],
#         "population_affected": [
#             100000,
#             200000,
#             150000,
#         ],
#     }
# )


# test_validation_report = pd.DataFrame(
#     {
#         "Validation": [
#             "Missing Values",
#             "Duplicate Records",
#             "Population Constraint",
#         ],
#         "Status": [
#             "Passed",
#             "Passed",
#             "Passed",
#         ],
#         "Action": [
#             "Missing values processed.",
#             "Duplicate records removed.",
#             "Population constraint passed.",
#         ],
#     }
# )


# # ----------------------------------------------------------------------
# # Use a temporary directory so the test does not modify the project
# # ----------------------------------------------------------------------

# with tempfile.TemporaryDirectory() as temp_dir:

#     temp_path = Path(temp_dir)

#     # ==============================================================
#     # [1] Testing save_cleaned_data()
#     # ==============================================================

#     print()
#     print("[1] Testing save_cleaned_data()...")

#     cleaned_output = (
#         temp_path
#         / "processed"
#         / "cleaned_data.csv"
#     )

#     cleaned_report = save_cleaned_data(
#         test_clean_df,
#         str(cleaned_output),
#     )

#     assert cleaned_output.exists()
#     assert cleaned_output.is_file()

#     print("✓ Cleaned dataset file was created.")
#     print(
#         f"✓ Export report: {cleaned_report}"
#     )


#     # ==============================================================
#     # [2] Checking cleaned dataset contents
#     # ==============================================================

#     print()
#     print("[2] Checking cleaned dataset contents...")

#     exported_clean_df = pd.read_csv(
#         cleaned_output
#     )

#     pd.testing.assert_frame_equal(
#         exported_clean_df,
#         test_clean_df,
#     )

#     print(
#         "✓ Exported cleaned dataset matches "
#         "the original DataFrame."
#     )


#     # ==============================================================
#     # [3] Checking cleaned dataset export report
#     # ==============================================================

#     print()
#     print(
#         "[3] Checking cleaned dataset export report..."
#     )

#     assert isinstance(
#         cleaned_report,
#         dict,
#     )

#     assert (
#         cleaned_report["Output Path"]
#         == str(cleaned_output)
#     )

#     assert (
#         cleaned_report["Rows"]
#         == len(test_clean_df)
#     )

#     assert (
#         cleaned_report["Columns"]
#         == len(test_clean_df.columns)
#     )

#     print(
#         "✓ Cleaned dataset export report "
#         "contains the expected information."
#     )


#     # ==============================================================
#     # [4] Testing save_validation_report()
#     # ==============================================================

#     print()
#     print("[4] Testing save_validation_report()...")

#     validation_output = (
#         temp_path
#         / "processed"
#         / "validation_report.csv"
#     )

#     validation_export_report = (
#         save_validation_report(
#             test_validation_report,
#             str(validation_output),
#         )
#     )

#     assert validation_output.exists()
#     assert validation_output.is_file()

#     print("✓ Validation report file was created.")
#     print(
#         f"✓ Export report: "
#         f"{validation_export_report}"
#     )


#     # ==============================================================
#     # [5] Checking validation report contents
#     # ==============================================================

#     print()
#     print(
#         "[5] Checking validation report contents..."
#     )

#     exported_validation_report = pd.read_csv(
#         validation_output
#     )

#     pd.testing.assert_frame_equal(
#         exported_validation_report,
#         test_validation_report,
#     )

#     print(
#         "✓ Exported validation report matches "
#         "the original DataFrame."
#     )


#     # ==============================================================
#     # [6] Checking validation report export report
#     # ==============================================================

#     print()
#     print(
#         "[6] Checking validation report export report..."
#     )

#     assert isinstance(
#         validation_export_report,
#         dict,
#     )

#     assert (
#         validation_export_report["Output Path"]
#         == str(validation_output)
#     )

#     assert (
#         validation_export_report["Rows"]
#         == len(test_validation_report)
#     )

#     assert (
#         validation_export_report["Columns"]
#         == len(test_validation_report.columns)
#     )

#     print(
#         "✓ Validation report export report "
#         "contains the expected information."
#     )


#     # ==============================================================
#     # [7] Testing automatic directory creation
#     # ==============================================================

#     print()
#     print(
#         "[7] Testing automatic directory creation..."
#     )

#     nested_output = (
#         temp_path
#         / "new"
#         / "nested"
#         / "folder"
#         / "data.csv"
#     )

#     save_cleaned_data(
#         test_clean_df,
#         str(nested_output),
#     )

#     assert nested_output.exists()

#     print(
#         "✓ Missing parent directories were "
#         "created automatically."
#     )


#     # ==============================================================
#     # [8] Testing empty DataFrame rejection
#     # ==============================================================

#     print()
#     print(
#         "[8] Testing empty DataFrame rejection..."
#     )

#     empty_df = pd.DataFrame()

#     try:

#         save_cleaned_data(
#             empty_df,
#             str(
#                 temp_path
#                 / "empty.csv"
#             ),
#         )

#         raise AssertionError(
#             "save_cleaned_data() should reject "
#             "an empty DataFrame."
#         )

#     except ValueError as error:

#         assert (
#             str(error)
#             == "Cannot export an empty DataFrame."
#         )

#         print(
#             "✓ Empty cleaned DataFrame was "
#             "correctly rejected."
#         )


#     # ==============================================================
#     # [9] Testing empty validation report rejection
#     # ==============================================================

#     print()
#     print(
#         "[9] Testing empty validation report rejection..."
#     )

#     empty_report = pd.DataFrame()

#     try:

#         save_validation_report(
#             empty_report,
#             str(
#                 temp_path
#                 / "empty_report.csv"
#             ),
#         )

#         raise AssertionError(
#             "save_validation_report() should reject "
#             "an empty validation report."
#         )

#     except ValueError as error:

#         assert (
#             str(error)
#             == "Cannot export an empty validation report."
#         )

#         print(
#             "✓ Empty validation report was "
#             "correctly rejected."
#         )


#     # ==============================================================
#     # [10] Checking that temporary files are inside the test
#     # directory
#     # ==============================================================

#     print()
#     print(
#         "[10] Checking test output isolation..."
#     )

#     assert str(cleaned_output).startswith(
#         str(temp_path)
#     )

#     assert str(validation_output).startswith(
#         str(temp_path)
#     )

#     print(
#         "✓ Test outputs were isolated inside "
#         "the temporary test directory."
#     )


# print()
# print("=" * 70)
# print("✓ EXPORT MODULE TEST PASSED")
# print("=" * 70)

# print()
# print(
#     "The export module successfully:"
# )

# print(
#     """
#   ✓ Saved the cleaned dataset
#   ✓ Preserved the cleaned dataset contents
#   ✓ Generated the cleaned-data export report
#   ✓ Saved the validation summary
#   ✓ Preserved the validation report contents
#   ✓ Generated the validation-report export report
#   ✓ Created missing output directories automatically
#   ✓ Rejected empty cleaned DataFrames
#   ✓ Rejected empty validation reports
#   ✓ Kept test outputs isolated from the project files
# """
# )


















# ======================================================================
# END-TO-END PIPELINE INTEGRATION TEST
# ======================================================================

import tempfile
from pathlib import Path

import pandas as pd

from config import RAW_PATH
from pipeline import run_pipeline
from export import (
    save_cleaned_data,
    save_validation_report,
)


print()
print("=" * 70)
print("END-TO-END PIPELINE INTEGRATION TEST")
print("=" * 70)


# ----------------------------------------------------------------------
# Create temporary output directory
# ----------------------------------------------------------------------

with tempfile.TemporaryDirectory() as temp_dir:

    temp_path = Path(temp_dir)

    cleaned_output = (
        temp_path
        / "processed"
        / "Global Health Dataset_cleaned.csv"
    )

    validation_output = (
        temp_path
        / "processed"
        / "validation_report.csv"
    )


    # ==============================================================
    # [1] Running complete pipeline
    # ==============================================================

    print()
    print("[1] Running complete pipeline...")

    clean_df, reports, summary_report = (
        run_pipeline(RAW_PATH)
    )

    print(
        "✓ Complete pipeline executed successfully."
    )


    # ==============================================================
    # [2] Checking final dataset dimensions
    # ==============================================================

    print()
    print("[2] Checking final dataset dimensions...")

    assert clean_df.shape == (10000, 30)

    print(
        f"✓ Final dataset dimensions confirmed: "
        f"{clean_df.shape[0]:,} rows × "
        f"{clean_df.shape[1]} columns."
    )


    # ==============================================================
    # [3] Checking pipeline reports
    # ==============================================================

    print()
    print("[3] Checking pipeline reports...")

    expected_report_sections = [
        "pipeline",
        "numeric_conversion",
        "missing_values",
        "repairs",
        "validations",
    ]

    for section in expected_report_sections:

        assert section in reports

        print(
            f"✓ Pipeline report found: {section}"
        )


    # ==============================================================
    # [4] Checking repair results
    # ==============================================================

    print()
    print("[4] Checking repair results...")

    repairs = reports["repairs"]

    assert (
        repairs["duplicate_records"]["Duplicates Removed"]
        == 5
    )

    assert (
        repairs["age_distribution"]["Rows Repaired"]
        == 4
    )

    assert (
        repairs["healthcare_access"]["Rows Repaired"]
        == 5
    )

    assert (
        repairs["urban_rural"]["Rows Repaired"]
        == 702
    )

    print(
        "✓ Expected repair results confirmed."
    )

    print(
        f"  Duplicate records removed: "
        f"{repairs['duplicate_records']['Duplicates Removed']}"
    )

    print(
        f"  Age distributions repaired: "
        f"{repairs['age_distribution']['Rows Repaired']}"
    )

    print(
        f"  Healthcare access repaired: "
        f"{repairs['healthcare_access']['Rows Repaired']}"
    )

    print(
        f"  Urban/Rural distributions repaired: "
        f"{repairs['urban_rural']['Rows Repaired']}"
    )


    # ==============================================================
    # [5] Checking validation results
    # ==============================================================

    print()
    print("\n[5] Checking validation results...")

    validations = reports["validations"]

    # --------------------------------------------------
    # Duplicate validation
    # --------------------------------------------------
    duplicate_report = validations["duplicate"]["report"]

    assert duplicate_report["Duplicate Rows"] == 0
    assert duplicate_report["Duplicate Country-Year-Disease"] == 0

    print("✓ Duplicate validation passed.")

    # --------------------------------------------------
    # Gender population validation
    # --------------------------------------------------
    gender_report = validations["gender_population"]["report"]

    assert gender_report["Passed"] is True

    print("✓ Gender population validation passed.")

    # --------------------------------------------------
    # Urban/Rural validation
    # --------------------------------------------------
    urban_report = validations["urban_rural"]["report"]

    assert urban_report["Passed"] is True

    print("✓ Urban/Rural validation passed.")

    # --------------------------------------------------
    # Population constraint validation
    # --------------------------------------------------
    population_report = validations["population_constraint"]["report"]

    assert population_report["Passed"] is True

    print("✓ Population constraint validation passed.")

    # --------------------------------------------------
    # Composite Health Index validation
    # --------------------------------------------------
    chi_report = validations["chi"]["report"]

    assert chi_report["Passed"] is True

    print("✓ Composite Health Index validation passed.")

    # --------------------------------------------------
    # Country-Year consistency validation
    # --------------------------------------------------
    consistency = validations["country_year_consistency"]

    # These four are expected to be genuinely consistent
    # across Country-Year groups.
    standard_consistency_columns = [
        "country_pop",
        "per_capita_income_usd",
        "education_index",
        "urbanization_rate_pct",
    ]

    for column in standard_consistency_columns:

        report = consistency[column]["report"]

        assert report["Passed"] is True

        print(
            f"✓ Country-Year consistency passed: {column}"
        )

    print("✓ All core validation results passed.")


    # ==============================================================
    # [6] Checking Country-Year validations
    # ==============================================================

    print()
    print(
        "[6] Checking Country-Year validations..."
    )

    country_year = (
        validations["country_year_consistency"]
    )

    expected_country_year_columns = [
        "country_pop",
        "per_capita_income_usd",
        "education_index",
        "urbanization_rate_pct",
        "healthcare_access_pct",
        "doctors_per_1000",
        "hospital_beds_per_1000",
        "composite_health_index",
    ]

    for column in expected_country_year_columns:

        assert column in country_year

        print(
            f"✓ Country-Year validation found: "
            f"{column}"
        )


    # ==============================================================
    # [7] Checking validation summary
    # ==============================================================

    print()
    print("\n[7] Checking validation summary...")

    assert isinstance(
        summary_report,
        pd.DataFrame,
    )

    assert summary_report.shape[0] == 18

    assert set(
        ["Validation", "Status", "Action"]
    ).issubset(
        summary_report.columns
    )

    print(
        "✓ Validation summary structure confirmed."
    )

    print(
        f"✓ Validation summary contains "
        f"{summary_report.shape[0]} rows."
    )


    # ==============================================================
    # [8] Exporting cleaned dataset
    # ==============================================================

    print()
    print("[8] Exporting cleaned dataset...")

    cleaned_export_report = save_cleaned_data(
        clean_df,
        str(cleaned_output),
    )

    assert cleaned_output.exists()
    assert cleaned_output.is_file()

    print(
        "✓ Cleaned dataset exported successfully."
    )

    print(
        f"✓ Output path: {cleaned_output}"
    )


    # ==============================================================
    # [9] Exporting validation report
    # ==============================================================

    print()
    print(
        "[9] Exporting validation report..."
    )

    validation_export_report = (
        save_validation_report(
            summary_report,
            str(validation_output),
        )
    )

    assert validation_output.exists()
    assert validation_output.is_file()

    print(
        "✓ Validation report exported successfully."
    )

    print(
        f"✓ Output path: {validation_output}"
    )


    # ==============================================================
    # [10] Reloading exported cleaned dataset
    # ==============================================================

    print()
    print(
        "[10] Reloading exported cleaned dataset..."
    )

    exported_clean_df = pd.read_csv(
        cleaned_output
    )

    assert exported_clean_df.shape == (
        10000,
        30,
    )

    print(
        "✓ Exported cleaned dataset has the "
        "expected dimensions."
    )


    #==============================================================
    # [11] Comparing exported cleaned dataset with pipeline output
    # ==============================================================
    print("\n[11a] Inspecting availability column before export comparison...")

    column = "availability_of_vaccines_treatment"

    print("\nPipeline values:")
    print(
        clean_df[column]
        .value_counts(dropna=False)
    )

    print("\nPipeline value types:")
    print(
        clean_df[column]
        .map(type)
        .value_counts()
    )

    print("\nPipeline rows considered missing:")
    print(
        clean_df[column]
        .isna()
        .sum()
    )

    print("\nExported values:")
    print(
        exported_clean_df[column]
        .value_counts(dropna=False)
    )

    print("\nExported rows considered missing:")
    print(
        exported_clean_df[column]
        .isna()
        .sum()
    )


    print("\n[11b] Comparing exported data with pipeline output...")

    exported_compare = exported_clean_df.copy()
    pipeline_compare = clean_df.copy()

    # --------------------------------------------------
    # Normalize CSV-specific missing-value interpretation.
    #
    # The pipeline intentionally stores the categorical value
    # "None" as a string. When the CSV is reloaded with
    # pandas.read_csv(), "None" is interpreted as NaN.
    #
    # Convert those exported NaN values back to the literal
    # "None" so that the exported data can be compared with
    # the original pipeline output.
    # --------------------------------------------------
    availability_column = (
        "availability_of_vaccines_treatment"
    )

    exported_compare[availability_column] = (
        exported_compare[availability_column]
        .fillna("None")
    )

    # --------------------------------------------------
    # Compare the exported data with the pipeline output.
    # --------------------------------------------------
    pd.testing.assert_frame_equal(
        exported_compare,
        pipeline_compare,
        check_dtype=False,
        check_names=True,
    )

    print(
        "✓ Exported cleaned dataset matches "
        "the pipeline output."
    )


    # ==============================================================
    # [12] Reloading exported validation report
    # ==============================================================

    print()
    print(
        "[12] Reloading exported validation report..."
    )

    exported_validation_report = pd.read_csv(
        validation_output
    )

    assert exported_validation_report.shape == (
        18,
        3,
    )

    print(
        "✓ Exported validation report has "
        "the expected dimensions."
    )


    # ==============================================================
    # [13] Comparing exported validation report
    # ==============================================================

    print()
    print(
        "[13] Comparing exported validation "
        "report with pipeline output..."
    )

    assert list(
        exported_validation_report.columns
    ) == list(summary_report.columns)

    pd.testing.assert_frame_equal(
        exported_validation_report,
        summary_report,
        check_dtype=False,
    )

    print(
        "✓ Exported validation report matches "
        "the pipeline output."
    )


    # ==============================================================
    # [14] Checking export reports
    # ==============================================================

    print()
    print("[14] Checking export reports...")

    assert isinstance(
        cleaned_export_report,
        dict,
    )

    assert isinstance(
        validation_export_report,
        dict,
    )

    assert (
        cleaned_export_report["Rows"]
        == 10000
    )

    assert (
        cleaned_export_report["Columns"]
        == 30
    )

    assert (
        validation_export_report["Rows"]
        == 18
    )

    assert (
        validation_export_report["Columns"]
        == 3
    )

    print(
        "✓ Export reports contain the expected "
        "metadata."
    )


    # ==============================================================
    # [15] Checking that original dataset was not modified
    # ==============================================================

    print()
    print(
        "[15] Checking source-file preservation..."
    )

    assert Path(RAW_PATH).exists()

    print(
        "✓ Original raw dataset remains available."
    )


    # ==============================================================
    # [16] Checking temporary output isolation
    # ==============================================================

    print()
    print(
        "[16] Checking output isolation..."
    )

    assert str(cleaned_output).startswith(
        str(temp_path)
    )

    assert str(validation_output).startswith(
        str(temp_path)
    )

    print(
        "✓ Integration-test outputs were isolated "
        "from the project files."
    )


# ======================================================================
# FINAL RESULT
# ======================================================================

print()
print("=" * 70)
print("✓ END-TO-END PIPELINE INTEGRATION TEST PASSED")
print("=" * 70)

print()
print(
    """
The complete data-cleaning workflow successfully:

  ✓ Loaded the raw dataset
  ✓ Applied column-name normalization
  ✓ Cleaned text values
  ✓ Converted numeric columns
  ✓ Handled missing values
  ✓ Removed duplicate records
  ✓ Repaired age distributions
  ✓ Repaired healthcare-access values
  ✓ Repaired Urban/Rural distributions
  ✓ Performed validation checks
  ✓ Generated validation reports
  ✓ Generated the validation summary
  ✓ Exported the cleaned dataset
  ✓ Exported the validation summary
  ✓ Reloaded both exported files successfully
  ✓ Confirmed exported data matches pipeline output
  ✓ Preserved the original source dataset
  ✓ Kept integration-test outputs isolated
"""
)








# from config import (
#     RAW_PATH,
#     CLEANED_DATA_PATH,
#     VALIDATION_REPORT_PATH,
# )

# from pipeline import run_pipeline

# from export import (
#     save_cleaned_data,
#     save_validation_report,
# )


# clean_df, reports, summary_report = (
#     run_pipeline(RAW_PATH)
# )

# cleaned_report = save_cleaned_data(
#     clean_df,
#     CLEANED_DATA_PATH,
# )

# validation_report = save_validation_report(
#     summary_report,
#     VALIDATION_REPORT_PATH,
# )