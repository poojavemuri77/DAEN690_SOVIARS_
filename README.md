# Team_SOVIARS_DAEN-690_10
# 🌊 Socioeconomic Vulnerability Index for Adaptation to Rising Seas (SOVIARS)

**Team SOVIARS | George Mason University | Spring 2025**

---

## 📌 Project Overview

Puerto Rico faces growing risks from climate change, including rising sea levels, storm surges, and coastal flooding. Our capstone project develops a **data-driven vulnerability index** that integrates **socioeconomic factors** with **environmental risks** to identify and prioritize at-risk communities for targeted adaptation efforts.

The project outputs three key indices:
- **SOVI**: Social Vulnerability Index.
- **VRS**: Vulnerability to Rising Seas (physical exposure).
- **SOVIARS**: Combined index of social and environmental vulnerability.

---

## 🎯 Objectives

- Develop a composite vulnerability index tailored to Puerto Rico.
- Visualize high-risk zones for policymakers.
- Provide a scalable framework for updating and maintaining the index.
- Highlight data gaps to inform future research and funding priorities.

---

## 📁 Files Included

| File | Description |
|------|-------------|
| `SOVIARS_INDEX.xlsx` | Final compiled index scores (SOVI, VRS, SOVIARS) for all municipalities |
| `readiness.csv` | Readiness infrastructure data used to assess emergency response capacity |
| `SOVI index calc.py` | Python code used to clean data, calculate sub-indices, and compute final SOVI |
| `readiness_index.ipynb` | Jupyter notebook for infrastructure readiness analysis |
| `MAIN_PROJECT.qgz` | QGIS project file containing spatial joins, styling, and all final map layers. |
| `Team SOVIARS Showcase Presentation(Final).pptx` | Final project presentation with visuals, methods, and findings |

---
## 🗺 GIS Project File

The `MAIN_PROJECT.qgz` file contains:
- Styled layers for SOVI, VRS, and SOVIARS
- Facility overlays and exposure zones
- All spatial processing for area and population metrics

To open:
1. Use QGIS 3.22 or later
2. Load project and ensure external raster/shape files are in the same directory

---

## 🛠️ Methodology

### 1. **Data Collection**
- Sources: U.S. Census (ACS 2023), FEMA, NOAA, QGIS.
- Domains: Social, Economic, Housing, Demographic, Environmental.

### 2. **Data Cleaning & Normalization**
- Missing values handled using domain-specific logic.
- All variables scaled using **Min-Max Normalization**.

### 3. **Index Calculation**
- Sub-indices were created by domain and assigned weights:
  - Social (35%), Economic (30%), Demographic (20%), Housing (15%).
- Final SOVI = Weighted average of all sub-indices.

### 4. **VRS Index**
- Based on % of population and land area at or below 7ft elevation or in FEMA flood zones.

### 5. **SOVIARS Index**
- Combines SOVI (60%) and VRS (40%) for integrated vulnerability analysis.

---

## 🧰 Tools & Technologies Used

- **Python** – For data preprocessing, index calculation, and analysis.
- **Excel** – For organizing input data and computing readiness and vrs scores.
- **QGIS** – For geographic mapping and spatial analysis.
- **Tableau** – For dashboard design and interactive data storytelling.
---
## 📊 Visualizations

- **Top 10 Vulnerable Municipalities**
- **Pie Charts** showing variable weights across domains.
- **Bar Graphs** categorizing vulnerability into risk zones (Low, Medium, High).
- **Adaptation Insights** included to guide policy recommendations.

> For visual outputs, see slides in `Team SOVIARS Showcase Presentation(Final).pptx`

---
### 🔗 Interactive Dashboard

Explore our full interactive dashboard here:

👉 [SOVIARS Tableau Dashboard (Public)](https://public.tableau.com/views/SOVIARSInsightsDashboard/Dashboard?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)

Includes:
- Risk classifications across Puerto Rico.
- Adaptation insights and Recommendations.
- Comparison of SOVI, VRS, and SOVIARS scores by municipality.
---

## 🔮 Future Scope

- 📍 **Enhanced Granularity**: Build indices at the *block group or community* level.
- 🛰️ **Spatial Adaptation**: Integrate distance metrics to suggest nearest relocation zones.
- 📈 **Predictive Modeling**: Forecast population shifts and resource demand for better planning.

---

## 👥 Team Members

- Pooja Vemuri. 
- Akarsh Matlaparthi.
- Venkata Naga Sanjay Reddy Narra.
- Abhista Chidamber Atchutuni.
- Manikanteshwar Gandrothula.
- Charan Reddy Thamma. 


---

## 📬 Client: Puerto Rico Science, Technology, and Research Trust

The Puerto Rico Science, Technology, and Research Trust is a private non-profit organization established in 2004 to foster innovation, technology transfer, commercialization, and job creation in Puerto Rico's technology sector. Based in San Juan, the Trust plays a crucial role in shaping public policy related to science, technology, research, and development.
The Trust actively supports technology-driven startups by providing funding and assisting inventors in securing patents. Additionally, its Technology Transfer Office, led by David Gulley (as of 2019), focuses on monetizing scientific advancements to drive Puerto Rico's economic growth.

---

## 📎 License

This repository is for academic purposes only. Please contact the team for permission to reuse or cite this work.

---

