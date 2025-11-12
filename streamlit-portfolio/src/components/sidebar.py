from __future__ import annotations

from pathlib import Path
from typing import Iterable, Mapping

import streamlit as st


_ROOT_DIR = Path(__file__).resolve().parents[2]


def _render_contact_block(profile: Mapping[str, str]) -> None:
     st.markdown("<hr class='sidebar-divider'>", unsafe_allow_html=True)
     st.markdown("#### Let's Connect")

     email = profile.get("email")
     phone = profile.get("phone")
     availability = profile.get("availability")

     if availability:
          st.caption(availability)

     if email:
          st.markdown(f"📬 <a href='mailto:{email}' target='_blank'>{email}</a>", unsafe_allow_html=True)
     if phone:
          st.markdown(f"📱 {phone}")


def _render_quick_facts(facts: Iterable[Mapping[str, str]]) -> None:
     if not facts:
          return

     st.markdown("<hr class='sidebar-divider'>", unsafe_allow_html=True)
     st.markdown("#### Quick Facts")
     for fact in facts:
          label = fact.get("label", "")
          value = fact.get("value", "")
          hint = fact.get("hint", "")
          icon = fact.get("icon", "")
          st.markdown(
               f"<div class='fact-chip'>{icon} <strong>{value}</strong><span>{label}</span><small>{hint}</small></div>",
               unsafe_allow_html=True,
          )


def _render_socials(socials: Iterable[Mapping[str, str]]) -> None:
     if not socials:
          return

     st.markdown("<hr class='sidebar-divider'>", unsafe_allow_html=True)
     st.markdown("#### Socials")
     for entry in socials:
          label = entry.get("label", "Connect")
          url = entry.get("url", "#")
          icon = entry.get("icon", "🔗")
          st.markdown(f"{icon} <a href='{url}' target='_blank'>{label}</a>", unsafe_allow_html=True)


def _render_resume(resume_info: Mapping[str, str]) -> None:
     if not resume_info:
          return

     rel_path = resume_info.get("file")
     note = resume_info.get("note")

     if not rel_path:
          return

     candidate = _ROOT_DIR / "assets" / rel_path
     if candidate.exists():
          with candidate.open("rb") as resume_handle:
               st.download_button(
                    "📄 Download CV",
                    data=resume_handle.read(),
                    file_name=rel_path,
                    mime="application/pdf",
                    type="primary",
               )
     else:
          st.markdown(
               "<div class='resume-note'>Add your latest CV to `assets/` to enable downloads.</div>",
               unsafe_allow_html=True,
          )

     if note:
          st.caption(note)


def render_sidebar(profile: Mapping[str, str], achievements: Iterable[Mapping[str, str]]) -> None:
     """Render the global sidebar used across all pages."""

     with st.sidebar:
          st.markdown(
               "<div class='sidebar-hero'><span>👋</span><h2>Jared Sheohn Acebes</h2><p>AI Trainee Developer · Community Leader · Full-Stack Builder</p></div>",
               unsafe_allow_html=True,
          )

          location = profile.get("location")
          if location:
               st.markdown(f"📍 {location}")

          summary = profile.get("sidebar_summary")
          if summary:
               st.caption(summary)

          _render_resume(profile.get("resume", {}))
          _render_quick_facts(profile.get("quick_stats", []))

          if achievements:
               st.markdown("<hr class='sidebar-divider'>", unsafe_allow_html=True)
               st.markdown("#### Recent Highlights")
               for item in list(achievements)[:3]:
                    st.markdown(
                         f"<div class='highlight-item'><strong>{item.get('year')}</strong> · {item.get('title')}</div>",
                         unsafe_allow_html=True,
                    )

          _render_socials(profile.get("social_links", []))
          _render_contact_block(profile)