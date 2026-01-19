# PP: general information and applications

import streamlit as st
import os

st.set_page_config(page_title="PDF Quick Links", page_icon="📑", layout="centered")

# --- Define names and local paths (relative to your GitHub root) ---
# Update these to match your actual PDF filenames in the repository
LINKS = {'question': ['PP_Thermoforming', 'PP_Steel_Pipe_Coating', 'PP_Selection_Guide', 'PP_Raffia_Extrusion', 'PP_General_Extrusion_Coating', 'PP_Fiber_Extrusion', 'PP_Fiber_Extrusion_Coating', 'PP_Compression_Molding', 'PP_Cast_Film_Extrusion_Coating', 'PP_BOPP', 'PP_Blown_Film_Extrusion_Coating', 'PP_Blow_Molding', 'PP_Injection_Molding'], 'answer': ['PP_Thermoforming_Grades_Explanation.pdf', 'PP_Steel_Pipe_Coating_SPC_Grades_Explanation.pdf', 'PP_Selection_Guide.pdf', 'PP_Raffia_Extrusion_Grades_Explanation.pdf', 'PP_General_Extrusion_Coating_Grades_Explanation.pdf', 'PP_Fiber_Extrusion_Grades_Explanation.pdf', 'PP_Fiber_Extrusion_Coating_Grades_Explanation.pdf', 'PP_Compression_Molding_Grades_Explanation.pdf', 'PP_Cast_Film_Extrusion_Coating_Grades_Explanation.pdf', 'PP_BOPP_Grades_Explanation.pdf', 'PP_Blown_Film_Extrusion_Coating_Grades_Explanation.pdf', 'PP_Blow_Molding_Grades_Explanation.pdf', 'PP_Injection_Molding_Grades_Explanation.pdf']}

st.title("📑 PDF Portal: PP")
st.write("Click to download or view the documents.")

# --- Quick access buttons ---

# Sort items alphabetically
items = sorted(LINKS.items(), key=lambda x: x[0])

# Create columns for a clean UI
cols = st.columns(len(items))

for i, (label, file_path) in enumerate(items):
    with cols[i]:
        if os.path.exists(file_path):
            with open(file_path, "rb") as file:
                st.download_button(
                    label=f"📕 {label}",
                    data=file,
                    file_name=file_path,
                    mime="application/pdf"  # Correct MIME type for PDF
                )
        else:
            st.warning(f"File '{label}' missing.")
