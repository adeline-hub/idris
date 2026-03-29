<p align="center">
  <a href="https://dankistudio.com">
    <img src="report/assets/logo.png" width="140">
  </a>
</p>

<h1 align="center">Danki Impact Scoring</h1>
<p align="center">
  https://adeline-hub.github.io/danki-impact-scoring/report/app.html
  
  A social-first impact scoring framework for investment due diligence<br/>
  8 dimensions · 5 EU regulatory frameworks · 2,000 synthetic benchmarks · ML-ready
</p>

<p align="center">
  <a href="https://adeline-hub.github.io/danki-impact-scoring/report/app.html">
    <img src="https://img.shields.io/badge/Whitepaper-Live-blue?logo=quarto" alt="Whitepaper Live"/>
  </a>
  <a href="https://adeline-hub.github.io/danki-impact-scoring/report/app.html">
    <img src="https://img.shields.io/badge/Scoring_App-Live-orange?logo=leaflet" alt="Scoring App Live"/>
  </a>
  <a href="LICENSE">
    <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License MIT"/>
  </a>
</p>

---

## Overview

**Danki Impact Scoring** is a dual-layer scoring engine that goes beyond ESG compliance to measure real-world impact. It produces a composite score (0–100) for any investment project across 8 impact dimensions, with full regulatory compliance verification across 5 EU frameworks.

**Key differentiators:**

- **Social-first**: Gender (20%) + Social Mobility (15%) + Governance (15%) = **50% of total weight**
- **Social veto rule**: Gender < 30 or Social Mobility < 30 → band capped at Amber regardless of score
- **Regulatory completeness**: EU Taxonomy, SFDR (Art. 6/8/9), CSRD/ESRS, TCFD, MiFID II
- **Explainable by design**: Every score traces to a published formula — zero black box
- **Fully static**: No server, no database — runs in the browser, works offline

---

## Deliverables

| Deliverable | Description | Link |
|:---|:---|:---|
| **Methodology Whitepaper** | Full scoring framework, formulas, regulatory mapping, EDA, ML methodology, data sources | [index.html](https://adeline-hub.github.io/danki-impact-scoring/) |
| **Scoring App** | Interactive project scorer with radar chart, regulatory gate, PAI dashboard, PDF export | [app.html](https://adeline-hub.github.io/danki-impact-scoring/app.html) |
| **Scoring Engine** | Standalone Python module — accepts any project dict, returns full scored result | `src/scoring.py` |
| **Data Generator** | Synthetic benchmark dataset: 2,000 projects, 50 countries, 20 sectors, 6 asset classes | `src/generate_data.py` |
| **Benchmark Dataset** | CSV with all dimension scores, SFDR classification, band assignment | `data/processed/investment_impacts.csv` |

---

## Scoring Framework

### The 8 Impact Dimensions

| Dimension | Weight | Category |
|:---|:---:|:---|
| Gender & Social Equity | 20% | Social |
| Social Mobility | 15% | Social |
| Governance & Corruption | 15% | Social |
| Climate & Environment | 18% | Environmental |
| Pollution & Health | 10% | Environmental |
| Water & Resources | 8% | Environmental |
| Territory & Local Wealth | 8% | Economic |
| Innovation & Resilience | 6% | Economic |

### Score Bands

| Band | Range | SFDR Alignment |
|:---|:---:|:---|
| 🟢 Dark Green | 75–100 | Article 9 eligible |
| 🟢 Green | 55–74 | Article 8+ eligible |
| 🟡 Amber | 35–54 | Article 8 minimum / Article 6 |
| 🔴 Red | 0–34 | Article 6 only |

### Social Veto Rule

If **Gender < 30** or **Social Mobility < 30**, the project is capped at **Amber** regardless of composite score. This operationalises the principle that no project achieves a Green band if it fails people.

---

## Investment Decision Support Tool

The scoring app provides:

- **Composite score** (0–100) with colour-coded band
- **Radar chart** — 8 dimensions with social overlay
- **Regulatory gate** — EU Taxonomy, SFDR, TCFD, CSRD, MiFID II (pass/fail)
- **PAI dashboard** — 10 key SFDR Principal Adverse Impact indicators
- **Due diligence flags** — warnings and strengths
- **PDF report download** — investor-ready and regulator-ready

All scoring runs **client-side in JavaScript** — no data leaves the user's device.

---

## Strategic Impact

Danki Impact Scoring addresses a gap in the impact investing market:

- **ESG measures risk to the company** — Danki measures **the company's effect on the world**
- **Social dimensions lead** — because gender equality and social mobility are upstream drivers of all other outcomes
- **Handles out-of-scope projects** — uses proxy data when investees are not in CSRD scope (post-Omnibus)
- **Built for the field** — works offline in low-connectivity environments for emerging market due diligence

---

## Why Machine Learning?

The **composite weighted index** is the primary scoring method — fully deterministic and explainable. The ML layer (Phase 3 roadmap) adds **calibration** for:

1. **Country × Sector interactions** — a solar farm in Norway vs. Nigeria has fundamentally different risk profiles
2. **Investment size non-linearity** — €1,500 microfinance vs. €50M infrastructure behave differently
3. **Temporal recalibration** — weights adjust as validated outcome data accumulates

**Approach**: XGBoost regressor with SHAP explainability. ML adjustment capped at ±10 points from composite. Human-in-the-loop validation required.

---

## Project Structure

```
danki-impact-scoring/
├── data/
│   └── processed/
│       └── investment_impacts.csv    ← 2,000-row benchmark dataset
├── docs/                             ← GitHub Pages output
│   └── assets/
│       ├── logo.png
│       └── favicon.ico
├── notebooks/
│   └── eda_marimo.py                 ← exploratory analysis
├── report/
│   ├── index.qmd                     ← methodology whitepaper
│   ├── app.qmd                       ← Danki scoring app
│   ├── report-style.css              ← shared brand stylesheet
│   └── assets/
│       ├── logo.png
│       └── favicon.ico
├── src/
│   ├── generate_data.py              ← synthetic dataset generator
│   ├── scoring.py                    ← composite scoring engine
│   └── viz.py                        ← chart functions for report
├── requirements.txt
├── _quarto.yml
└── README.md
```

---

## Local Development

### 1. Clone Repository

```bash
git clone https://github.com/adeline-hub/danki-impact-scoring.git
cd danki-impact-scoring
```

### 2. Create and Activate Virtual Environment

```bash
# Windows
python -m venv .venv
.\.venv\Scripts\Activate

# macOS / Linux
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

If generating PDF for the first time:

```bash
quarto install tinytex
```

### 4. Generate Dataset

```bash
python src/generate_data.py
```

Output: `data/processed/investment_impacts.csv` (2,000 projects)

### 5. Render HTML Report + Scoring App

```bash
cd report
quarto render index.qmd --to html --output-dir ../docs
quarto render app.qmd --to html --output-dir ../docs
cd ..
```

Open locally: `docs/index.html` and `docs/app.html`

### 6. Render PDF Report

```bash
cd report
quarto render index.qmd --to pdf
cd ..
```

Output: `report/index.pdf`

### 7. Publish to GitHub Pages

```bash
git add .
git commit -m "Update Danki Impact Scoring"
git push origin main
```

Or use Quarto's built-in publish command:

```bash
quarto publish gh-pages
```

---

## Data Sources

### Public (Free)

| Source | Data |
|:---|:---|
| Transparency International CPI | Country corruption index |
| World Bank Open Data | GDP, Gini, education, electricity access |
| ILO STAT | Gender pay gap, labour participation |
| UNDP HDI | Human Development Index, gender inequality |
| ND-GAIN Index | Climate vulnerability and readiness |
| EU Taxonomy Compass | Eligible activities, screening criteria |
| OpenSanctions | Sanctions lists, PEP data |

### Proprietary (Optional, Phase 3+)

MSCI ESG · Sustainalytics · CDP · Refinitiv · RepRisk · Clarity AI · Moody's ESG

---

## References

1. **EU Taxonomy Regulation** (2020/852) — Official Journal of the European Union
2. **SFDR** (2019/2088) — Sustainability-related disclosures in financial services
3. **CSRD** (2022/2464) — Corporate Sustainability Reporting Directive
4. **CSDDD** (2024/1760) — Corporate Sustainability Due Diligence Directive
5. **TCFD Recommendations** (2017) — Task Force on Climate-related Financial Disclosures, FSB
6. **MiFID II** (2014/65/EU) — Markets in Financial Instruments Directive
7. **ESMA/EBA Joint PAI Report** (JC 2024/68) — Principal Adverse Impact disclosures
8. **AMF** — Autorité des Marchés Financiers, sustainable finance regulatory guidance
9. **Transparency International CPI** (2024) — Corruption Perceptions Index
10. **GIIN** — Global Impact Investing Network, Annual Impact Investor Survey (2024)
11. **IFC Performance Standards** (2012) — Environmental and Social Sustainability
12. **OECD Guidelines for MNEs** (2023 update) — Responsible business conduct

---

## Author

**Nambona YANGUERE**
CFA ESG Certified · AMF Certified · MBA Finance (Sorbonne)

---

<p align="center">
  Built by <a href="https://dankistudio.com"><strong>Danki Studio</strong></a> · Nambona YANGUERE
</p>



