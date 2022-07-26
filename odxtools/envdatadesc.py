# SPDX-License-Identifier: MIT
# Copyright (c) 2022 MBition GmbH

from dataclasses import dataclass
from typing import List

from .globals import logger


@dataclass
class EnvDataDesc:
    """This class represents a ENV-DATA-DESC."""

    id: str
    short_name: str
    long_name: str
    param_snref: str
    param_snpathref: str
    env_data_refs: List[str]
    # TODO: Implement ENV-DATA and resolve references

    def __post_init__(self):
        pass

    def _build_id_lookup(self):
        id_lookup = {}
        id_lookup.update({self.id: self})
        return id_lookup

    def _resolve_references(self, id_lookup):
        """Recursively resolve any references (odxlinks or sn-refs)
        """
        pass

    def __repr__(self) -> str:
        return (
            f"EnvDataDesc('{self.short_name}', "
            + ", ".join(
                [
                    f"id='{self.id}'",
                    f"param_snref='{self.param_snref}'",
                    f"env_data_refs='{self.env_data_refs}'",
                ]
            )
            + ")"
        )


def read_env_data_desc_from_odx(et_element):
    """Reads a ENV-DATA-DESC."""
    id = et_element.get("ID")
    short_name = et_element.find("SHORT-NAME").text
    long_name = et_element.find("LONG-NAME").text
    param_snref = ""
    if et_element.find("PARAM-SNREF") is not None:
        param_snref = et_element.find("PARAM-SNREF").get("SHORT-NAME")
    param_snpathref = ""
    if et_element.find("PARAM-SNPATHREF") is not None:
        param_snpathref = et_element.find("PARAM-SNPATHREF").get("SHORT-NAME-PATH")
    env_data_refs = None
    if et_element.find("ENV-DATA-REFS") is not None:
        env_data_refs = [
            env_data_ref.get("ID-REF")
            for env_data_ref in et_element.find("ENV-DATA-REFS").findall("ENV-DATA-REF")
        ]
    logger.debug("Parsing ENV-DATA-DESC " + short_name)

    env_data_desc = EnvDataDesc(
        id=id,
        short_name=short_name,
        long_name=long_name,
        param_snref=param_snref,
        param_snpathref=param_snpathref,
        env_data_refs=env_data_refs,
    )

    return env_data_desc
