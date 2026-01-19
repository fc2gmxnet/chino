# PP: general information and applications

import streamlit as st
import os
from pathlib import Path

st.set_page_config(page_title="PDF Portal", page_icon="📑", layout="wide")

# Get the directory where PP.py is located
# This ensures the app looks in the same folder as the script
BASE_DIR = Path(__file__).parent

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

st.title("📑 Technical PDF Portal: PP")
st.info("If a file shows as 'Missing', ensure the PDF is uploaded to the same folder as your Python script on GitHub.")

# --- Layout Logic ---
items = sorted(LINKS.items())
cols_per_row = 3 

for i in range(0, len(items), cols_per_row):
    row_items = items[i : i + cols_per_row]
    cols = st.columns(cols_per_row)
    
    for j, (label, filename) in enumerate(row_items):
        with cols[j]:
            # Construct the full path to the file
            file_path = BASE_DIR / filename
            
            if file_path.exists():
                with open(file_path, "rb") as file:
                    st.download_button(
                        label=f"✅ {label.replace('_', ' ')}",
                        data=file,
                        file_name=filename,
                        mime="application/pdf",
                        use_container_width=True
                    )
            else:
                # Debugging: Show the path the app is looking at
                st.error(f"Missing: {label}")
                st.caption(f"Search path: `{file_path.name}`")
