"""Cik Map Standard Model."""

from typing import Optional, Union

from pydantic import Field, field_validator

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)


class CikMapQueryParams(QueryParams):
    """CikMap Query."""

    symbol: str = Field(description=QUERY_DESCRIPTIONS.get("symbol", ""))

    @field_validator("symbol", mode="before", check_fields=False)
    @classmethod
    def upper_symbol(cls, v: str) -> str:
        """Convert symbol to uppercase."""
        return v.upper()


class CikMapData(Data):
    """CikMap Data."""

    cik: Optional[Union[str, int]] = Field(
        default=None, description=DATA_DESCRIPTIONS.get("cik", "")
    )
