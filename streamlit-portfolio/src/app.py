from __future__ import annotations

from pathlib import Path
from typing import Mapping

import yaml
import streamlit as st

from components import render_biography_page, render_portfolio, render_contact_section, render_sidebar


ROOT = Path(__file__).resolve().parent


def _load_yaml(path: Path):
     if not path.exists():
          return {}
     with path.open("r", encoding="utf-8") as fh:
          return yaml.safe_load(fh) or {}


def _inject_css():
     css_path = ROOT / "styles" / "theme.css"
     if css_path.exists():
          with css_path.open("r", encoding="utf-8") as fh:
               st.markdown(f"<style>{fh.read()}</style>", unsafe_allow_html=True)


def main() -> None:
     st.set_page_config(page_title="Jared — Portfolio", layout="wide")

     _inject_css()

     data_dir = ROOT / "data"
     profile = _load_yaml(data_dir / "profile.yaml") or {}
     achievements = _load_yaml(data_dir / "achievements.yaml") or []
     projects = _load_yaml(data_dir / "projects.yaml") or []

     # Navigation at the top of sidebar
     page = st.sidebar.radio("Navigate", ["About", "Portfolio", "Contact"])
     
     # Sidebar content below navigation
     render_sidebar(profile, achievements)

     if page == "About":
          render_biography_page(profile, achievements)
     elif page == "Portfolio":
          render_portfolio(projects)
     elif page == "Contact":
          render_contact_section(profile)


if __name__ == "__main__":
     main()
