# PE: general information and applications

import streamlit as st
import os
from pathlib import Path

st.set_page_config(page_title="PDF Portal", page_icon="📑", layout="wide")

# Get the directory where PE.py is located
# This ensures the app looks in the same folder as the script
BASE_DIR = Path(__file__).parent

LINKS = {
    'PE_Automotive_Blow_Molding': 'PE_Automotive_Blow_Molding_Grades_Explanation.pdf',
    'PE_Blow_Molding': 'PE_Blow_Molding_Grades_Explanation.pdf',
    'PE_Blown_Film': 'PE_Blown_Film_Grades_Explanation.pdf',
    'PE_Extrusion_Cast_Film': 'PE_Extrusion_Cast_Film_Grades_Explanation.pdf',
    'PE_Extrusion_Coating': 'PE_Extrusion_Coating_Grades_Explanation.pdf',
    'PE_Extrusion_Geomembranes': 'PE_Extrusion_Geomembranes_Grades_Explanation.pdf',
    'PE_Extrusion_Wire_Cable': 'PE_Extrusion_Wire_Cable_Grades_Explanation.pdf',
    'PE_Injection_Molding': 'PE_Injection_Molding_Grades_Explanation.pdf',
    'PE_Masterbatches': 'PE_Masterbatches_Grades_Explanation.pdf',
    'PE_Monofilament_Extrusion': 'PE_Monofilament_Extrusion_Grades_Explanation.pdf',
    'PE_Pipes_Non_Pressurized': 'PE_Pipes_Non_Pressurized_Grades_Explanation.pdf',
    'PE_Pipes_Pressurized': 'PE_Pipes_Pressurized_Grades_Explanation.pdf',
    'PE_Rotomolding': 'PE_Rotomolding_Grades_Explanation.pdf',
    'PE_grades': 'PE_Grades_Comparison.pdf',
    'PE_vs_PP': 'PE_vs_PP.pdf',
}

st.title("📑 Technical PDF Portal: PE")
#st.info("If a file shows as 'Missing', ensure the PDF is uploaded to the same folder as your Python script on GitHub.")

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
