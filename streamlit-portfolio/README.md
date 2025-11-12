# 🚀 Personal Portfolio App

A modern Streamlit portfolio showcasing AI development experience, projects, and achievements.

## ✨ Features

- **Modern Design**: Dark theme with glassmorphism effects
- **Interactive Components**: Project filters, skill radar charts, contact form
- **Responsive Layout**: Sidebar navigation with smooth transitions
- **Data-Driven**: Easy updates via YAML files

## 🛠 Quick Start

1. **Install dependencies**:
   ```bash
   pip install streamlit pyyaml plotly
   ```

2. **Run the app**:
   ```bash
   cd src
   streamlit run app.py
   ```
     ```

## 📁 Project Structure

```
streamlit-portfolio/
├── src/
│   ├── app.py              # Main application
│   ├── components/         # Reusable UI components
│   ├── data/              # YAML data files
│   ├── pages/             # Multi-page navigation
│   └── styles/            # CSS themes
├── assets/                # Images, fonts, etc.
├── requirements.txt       # Dependencies
└── README.md             # This file
```

## 🎨 Customization

- **Content**: Edit YAML files in `src/data/`
- **Styling**: Modify `src/styles/theme.css`
- **Components**: Add features in `src/components/`

## 📄 Data Files

- `profile.yaml` - Personal info, skills, experience
- `projects.yaml` - Portfolio projects with filters
- `achievements.yaml` - Awards and certifications
- `testimonials.yaml` - Recommendations

#### 4. **Aesthetic Considerations**
   - **Theme**: Choose a color scheme that reflects your personal brand. You can set a theme in Streamlit using:
     ```python
     st.set_page_config(page_title="My Portfolio", layout="wide", initial_sidebar_state="expanded")
     ```
   - **Fonts and Styles**: Use Markdown for styling text (bold, italics) and headers to create a hierarchy.
   - **Images**: Ensure all images are high quality and properly sized for the layout.
   - **Spacing and Layout**: Use `st.markdown()` with HTML for custom spacing or separators to improve readability.
   - **Background Color**: You can customize the background color using CSS styles in Markdown.

#### 5. **Example Code Snippet**
Here’s a basic example of how the code structure might look:

```python
import streamlit as st

# Set page configuration
st.set_page_config(page_title="My Portfolio", layout="wide")

# Title
st.title("Welcome to My Portfolio")

# Autobiography Section
st.header("About Me")
st.image("path_to_your_image.jpg", width=200)
st.write("Hello! I'm [Your Name], a [Your Profession]. Here's a little about me...")

---

Built with ❤️ using Streamlit