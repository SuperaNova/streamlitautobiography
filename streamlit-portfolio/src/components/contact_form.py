from __future__ import annotations

from typing import Mapping

import streamlit as st


def render_contact_section(profile: Mapping[str, object] | None = None) -> None:
     """Render a simple contact form. This does not send emails but shows a success state.

     The function is intentionally local-only to avoid requiring external services.
     """

     st.markdown("### Get in touch")

     with st.form("contact_form", clear_on_submit=True):
          name = st.text_input("Your name")
          email = st.text_input("Your email")
          message = st.text_area("Message")
          send = st.form_submit_button("Send message")

     if send:
          if not name or not email or not message:
               st.error("Please fill all fields before sending.")
               return

          # Basic client-side email validation
          if "@" not in email or "." not in email.split("@")[-1]:
               st.error("Please provide a valid email address.")
               return

          # In a production app you'd call an API or send via SMTP here.
          st.success("Thanks — your message was recorded locally.")
          st.info("(This demo app does not forward messages. Connect an email API to enable delivery.)")

          # Optionally echo back submission (helpful when testing locally)
          st.markdown("---")
          st.markdown(f"**From:** {name} — {email}")
          st.write(message)