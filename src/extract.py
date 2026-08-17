"""
Utilities for loading the Global Health Dataset from disk.

This module provides functions for reading raw data files,
performing basic schema validation, normalizing column names,
and returning the dataset together with associated metadata.
"""

from pathlib import Path

import pandas as pd

from config import (
    EXPECTED_COLUMNS,
    COLUMN_RENAME_MAP,
    NA_VALUES,
)


def load_data(
    file_path: str | Path,
) -> tuple[pd.DataFrame, dict]:
    """
    Load the Global Health Dataset from a CSV file.

    The function validates the raw dataset schema, converts
    configured missing-value representations to NaN, and
    normalizes column names according to the project's
    configured column mapping.

    Parameters
    ----------
    file_path : str or pathlib.Path
        Path to the raw CSV dataset.

    Returns
    -------
    df : pandas.DataFrame
        Loaded and column-normalized dataset.

    metadata : dict
        Metadata describing the source file, encoding,
        number of rows, number of columns, and memory usage.

    Raises
    ------
    FileNotFoundError
        If the specified dataset does not exist.

    ValueError
        If the dataset contains a different number of
        columns, missing expected columns, or unexpected
        columns.
    """

    csv_path = Path(file_path)

    # --------------------------------------------------
    # Check that the dataset exists
    # --------------------------------------------------
    if not csv_path.exists():
        raise FileNotFoundError(
            f"Dataset not found: {csv_path}"
        )

    # --------------------------------------------------
    # Load the raw dataset
    # --------------------------------------------------
    encoding = "cp1252"

    df = pd.read_csv(
        csv_path,
        encoding=encoding,
        low_memory=False,
        keep_default_na=False,
        na_values=NA_VALUES,
    )

    # --------------------------------------------------
    # Validate raw column count
    # --------------------------------------------------
    if len(df.columns) != len(EXPECTED_COLUMNS):
        raise ValueError(
            f"Expected {len(EXPECTED_COLUMNS)} columns "
            f"but found {len(df.columns)}."
        )

    # --------------------------------------------------
    # Check for missing expected columns
    # --------------------------------------------------
    missing_columns = [
        column
        for column in EXPECTED_COLUMNS
        if column not in df.columns
    ]

    # --------------------------------------------------
    # Check for unexpected columns
    # --------------------------------------------------
    unexpected_columns = [
        column
        for column in df.columns
        if column not in EXPECTED_COLUMNS
    ]

    if missing_columns:
        raise ValueError(
            f"Missing columns: {missing_columns}"
        )

    if unexpected_columns:
        raise ValueError(
            f"Unexpected columns: {unexpected_columns}"
        )

    # --------------------------------------------------
    # Normalize column names
    # --------------------------------------------------
    df = df.rename(
        columns=COLUMN_RENAME_MAP
    )

    # --------------------------------------------------
    # Build metadata
    # --------------------------------------------------
    metadata = {
        "source_file": csv_path.name,
        "source_path": str(csv_path),
        "encoding": encoding,
        "rows": len(df),
        "columns": len(df.columns),
        "shape": df.shape,
        "memory_mb": float(
            round(
                df.memory_usage(deep=True).sum()
                / 1024**2,
                2
            )
        ),
    }

    return df, metadata