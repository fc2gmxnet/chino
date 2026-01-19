# PP: general information and applications

import streamlit as st
import os

st.set_page_config(page_title="PDF Quick Links", page_icon="📑", layout="centered")

# --- Dictionary of Links ---
LINKS = {
    'PP_Blow_Molding': 'PP_Blow_Molding_Grades_Explanation.pdf',
    'PP_Blown_Film_Extrusion_Coating': 'PP_Blown_Film_Extrusion_Coating_Grades_Explanation.pdf',
    'PP_BOPP': 'PP_BOPP_Grades_Explanation.pdf',
    'PP_Cast_Film_Extrusion_Coating': 'PP_Cast_Film_Extrusion_Coating_Grades_Explanation.pdf',
    'PP_Compression_Molding': 'PP_Compression_Molding_Grades_Explanation.pdf',
    'PP_Fiber_Extrusion': 'PP_Fiber_Extrusion_Grades_Explanation.pdf',
    'PP_Fiber_Extrusion_Coating': 'PP_Fiber_Extrusion_Coating_Grades_Explanation.pdf',
    'PP_General_Extrusion_Coating': 'PP_General_Extrusion_Coating_Grades_Explanation.pdf',
    'PP_Injection_Molding': 'PP_Injection_Molding_Grades_Explanation.pdf',
    'PP_Raffia_Extrusion': 'PP_Raffia_Extrusion_Grades_Explanation.pdf',
    'PP_Selection_Guide': 'PP_Selection_Guide.pdf',
    'PP_Steel_Pipe_Coating': 'PP_Steel_Pipe_Coating_SPC_Grades_Explanation.pdf',
    'PP_Thermoforming': 'PP_Thermoforming_Grades_Explanation.pdf'
}

st.title("📑 PDF Portal: PP")
st.write("Access your technical grade explanations below.")

# --- Grid Configuration ---
items = sorted(LINKS.items())
cols_per_row = 3  # Adjust this number to change grid width

# Iterate through the items in chunks of 'cols_per_row'
for i in range(0, len(items), cols_per_row):
    row_items = items[i : i + cols_per_row]
    cols = st.columns(cols_per_row)
    
    for j, (label, file_path) in enumerate(row_items):
        with cols[j]:
            # Use os.path.join if your files are in a subfolder, 
            # e.g., os.path.join("PP", file_path)
            if os.path.exists(file_path):
                with open(file_path, "rb") as file:
                    st.download_button(
                        label=f"📕 {label.replace('_', ' ')}",
                        data=file,
                        file_name=file_path,
                        mime="application/pdf",
                        use_container_width=True  # Makes buttons look uniform
                    )
            else:
                st.error(f"Missing: {label}")
