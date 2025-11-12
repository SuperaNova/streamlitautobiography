from __future__ import annotations

from typing import Iterable, Mapping, Sequence

import plotly.graph_objects as go
import streamlit as st


def _render_focus_badges(focus_areas: Sequence[str]) -> None:
     if not focus_areas:
          return

     chips = "".join(f"<span class='focus-chip'>{area}</span>" for area in focus_areas)
     st.markdown(f"<div class='focus-chip-row'>{chips}</div>", unsafe_allow_html=True)


def _plot_skill_radar(entries: Sequence[Mapping[str, float]]) -> go.Figure | None:
     if not entries:
          return None

     categories = [entry.get("label", "") for entry in entries]
     scores = [entry.get("score", 0) for entry in entries]

     if not any(scores):
          return None

     categories.append(categories[0])
     scores.append(scores[0])

     fig = go.Figure()
     fig.add_trace(
          go.Scatterpolar(r=scores, theta=categories, fill="toself", name="Proficiency", line=dict(color="#4F46E5"))
     )
     fig.update_layout(
          polar=dict(radialaxis=dict(visible=True, range=[0, 100], showticklabels=False)),
          showlegend=False,
          margin=dict(l=20, r=20, t=40, b=20),
          template="plotly_dark",
     )
     return fig


def render_hero_section(profile: Mapping[str, object]) -> None:
     st.markdown("### Hi, I'm Jared 👋")

     cols = st.columns([2.2, 1.2])
     with cols[0]:
          st.subheader(profile.get("tagline", ""))
          summary_points = profile.get("summary_points", [])
          for point in summary_points:
               st.write(f"- {point}")

          _render_focus_badges(profile.get("focus_areas", []))

     with cols[1]:
          st.markdown("#### Snapshot")
          stats = profile.get("quick_stats", [])
          for stat in stats[:3]:
               label = stat.get("label", "")
               value = stat.get("value", "")
               hint = stat.get("hint", "")
               st.metric(label=label, value=value, delta=hint if hint else None)

     st.markdown(profile.get("hero_quote", ""))


def render_professional_journey(experiences: Iterable[Mapping[str, object]]) -> None:
     st.divider()
     st.markdown("### Professional Journey")
     for exp in experiences:
          with st.container():
               cols = st.columns([1, 3])
               with cols[0]:
                    st.caption(f"{exp.get('start', '')} – {exp.get('end', 'Present')}")
                    st.markdown(f"**{exp.get('company', '')}**")
                    stack = exp.get("stack", [])
                    if stack:
                         st.markdown(
                              "<div class='stack-chip-row'>"
                              + "".join(f"<span class='stack-chip'>{tool}</span>" for tool in stack)
                              + "</div>",
                              unsafe_allow_html=True,
                         )
               with cols[1]:
                    st.subheader(exp.get("title", ""), anchor=False)
                    st.write(exp.get("summary", ""))
                    highlights = exp.get("highlights", [])
                    if highlights:
                         for highlight in highlights:
                              st.markdown(f"- {highlight}")


def render_leadership_and_service(leadership: Mapping[str, Sequence[Mapping[str, object]]]) -> None:
     st.divider()
     st.markdown("### Leadership & Service")

     categories = leadership.get("categories", [])
     if not categories:
          st.info("Leadership stories coming soon.")
          return

     tabs = st.tabs([category.get("name", "") for category in categories])
     for tab, category in zip(tabs, categories):
          with tab:
               for role in category.get("items", []):
                    st.markdown(f"#### {role.get('role', '')}")
                    st.caption(f"{role.get('organization', '')} · {role.get('duration', '')}")
                    scope = role.get("scope")
                    if scope:
                         st.write(scope)
                    bullet_points = role.get("highlights", [])
                    if bullet_points:
                         for item in bullet_points:
                              st.markdown(f"- {item}")


def render_skill_showcase(skills: Mapping[str, object]) -> None:
     st.divider()
     st.markdown("### Skill Showcase")

     radar_fig = _plot_skill_radar(skills.get("radar", []))
     cols = st.columns([1.2, 1])

     with cols[0]:
          categories = skills.get("categories", [])
          for category in categories:
               st.markdown(f"#### {category.get('name', '')}")
               items = category.get("items", [])
               tags = "".join(f"<span class='stack-chip'>{item}</span>" for item in items)
               st.markdown(f"<div class='stack-chip-row'>{tags}</div>", unsafe_allow_html=True)

     with cols[1]:
          if radar_fig:
               st.plotly_chart(radar_fig, use_container_width=True)
          else:
               st.info("Update the radar scores in your profile data to unlock this chart.")

          toolkit = skills.get("toolkit", [])
          if toolkit:
               st.markdown("#### Toolkit Sweet Spot")
               for item in toolkit:
                    st.markdown(f"- {item}")

     soft_skills = skills.get("soft_skills", [])
     if soft_skills:
          with st.expander("Team & Personal Strengths", expanded=False):
               for soft in soft_skills:
                    st.markdown(f"- {soft}")


def render_biography_page(profile: Mapping[str, object], achievements: Sequence[Mapping[str, object]]) -> None:
     """Compose the default "About" page for the portfolio."""

     render_hero_section(profile)

     if achievements:
          st.divider()
          st.markdown("### Spotlight Achievements")
          cols = st.columns(3)
          for col, achievement in zip(cols * ((len(achievements) // 3) + 1), achievements[:6]):
               with col:
                    st.markdown(f"**{achievement.get('year', '')}**")
                    st.caption(achievement.get("issuer", ""))
                    st.write(achievement.get("title", ""))

     render_professional_journey(profile.get("experience", []))
     render_leadership_and_service(profile.get("leadership", {}))
     render_skill_showcase(profile.get("skills", {}))

     education = profile.get("education", [])
     if education:
          st.divider()
          st.markdown("### Education")
          for entry in education:
               st.markdown(f"**{entry.get('institution', '')}** · {entry.get('duration', '')}")
               st.caption(entry.get("program", ""))

     certifications = profile.get("certifications", [])
     if certifications:
          st.markdown("### Certifications & Trainings")
          for cert in certifications:
               st.markdown(f"- {cert}")

     call_to_action = profile.get("call_to_action")
     if call_to_action:
          st.success(call_to_action)