from __future__ import annotations

from typing import Iterable, Mapping

import streamlit as st


def _collect_unique(items: Iterable[Mapping[str, object]], key: str) -> list[str]:
     values: set[str] = set()
     for item in items:
          raw = item.get(key)
          if isinstance(raw, str):
               values.add(raw)
     return sorted(values)


def _collect_tags(items: Iterable[Mapping[str, object]]) -> list[str]:
     tags: set[str] = set()
     for item in items:
          for tech in item.get("technologies", []) or []:
               tags.add(tech)
     return sorted(tags)


def render_portfolio(projects: Iterable[Mapping[str, object]]) -> None:
     projects = list(projects)
     st.markdown("### Featured Projects")

     if not projects:
          st.info("Projects will appear here once you add them to `src/data/projects.yaml`.")
          return

     categories = _collect_unique(projects, "category")
     tags = _collect_tags(projects)

     filters_col, search_col = st.columns([2, 1])
     with filters_col:
          selected_categories = st.multiselect("Filter by focus area", categories, default=categories[:1])
          selected_tags = st.multiselect("Filter by technology", tags)

     with search_col:
          search_term = st.text_input("Search", placeholder="Try 'LangChain' or 'relief'")

     def matches_filters(project: Mapping[str, object]) -> bool:
          if selected_categories and project.get("category") not in selected_categories:
               return False
          if selected_tags:
               project_tags = set(project.get("technologies", []))
               if not project_tags.issuperset(selected_tags):
                    return False
          if search_term:
               haystack = " ".join(
                    [str(project.get("name", "")), project.get("summary", ""), " ".join(project.get("highlights", []))]
               ).lower()
               if search_term.lower() not in haystack:
                    return False
          return True

     filtered = [project for project in projects if matches_filters(project)]
     if not filtered:
          st.warning("No projects match the current filters—try broadening your selection.")
          return

     # Render each project as a card-like container
     for project in filtered:
          with st.container():
               title_col, status_col = st.columns([3, 1])
               with title_col:
                    st.markdown(f"### {project.get('name', 'Untitled Project')}")
                    role = project.get('role', '')
                    year = project.get('year', '')
                    if role or year:
                         st.caption(f"{role} · {year}")
                    st.write(project.get("summary", ""))

                    tech_tags = "".join(f"<span class='stack-chip'>{tech}</span>" for tech in project.get("technologies", []))
                    if tech_tags:
                         st.markdown(f"<div class='stack-chip-row'>{tech_tags}</div>", unsafe_allow_html=True)

               with status_col:
                    status = project.get("status", "")
                    if status:
                         st.success(status)
                    progress = project.get("maturity", 0)
                    try:
                         progress_val = int(progress)
                    except Exception:
                         progress_val = 0
                    if progress_val:
                         st.progress(min(progress_val, 100))
                    impact = project.get("impact", "")
                    if impact:
                         st.caption(impact)

               highlights = project.get("highlights", [])
               if highlights:
                    with st.expander("What made this special", expanded=False):
                         for highlight in highlights:
                              st.markdown(f"- {highlight}")

               links = project.get("links", {})
               if links:
                    link_fragments = []
                    for label, url in links.items():
                         link_fragments.append(f"[{label.title()}]({url})")
                    st.markdown(" • ".join(link_fragments))