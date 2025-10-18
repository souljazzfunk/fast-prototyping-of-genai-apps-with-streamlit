# Feature Prioritization Matrix

## MUST-HAVE (MVP - Version 1.0)
*Core features needed to solve the primary problem and deliver value*

### 1. **CSV File Upload**
- **Why:** Entry point for user data
- **User Story:** "As a PM, I need to upload my customer reviews CSV so I can analyze it"
- **Risk if excluded:** App is unusable

### 2. **Sentiment Analysis via OpenAI**
- **Why:** Core value proposition - automated sentiment classification
- **User Story:** "As a PM, I need automatic sentiment tagging so I don't manually read 500 reviews"
- **Risk if excluded:** No differentiation from Excel

### 3. **Basic Bar Chart (Sentiment Distribution)**
- **Why:** Quick visual summary is the primary insight
- **User Story:** "As a PM, I need to see sentiment breakdown at a glance for my weekly report"
- **Risk if excluded:** Users can't quickly understand the data

### 4. **Product Filter (Single or Multi-select)**
- **Why:** Enables drill-down analysis by product line
- **User Story:** "As a PM, I need to filter by product so I can identify which items have issues"
- **Risk if excluded:** Can't isolate problem products

### 5. **Filtered Results Table**
- **Why:** Users need to read actual reviews after filtering
- **User Story:** "As a CS rep, I need to see the actual negative reviews so I can contact customers"
- **Risk if excluded:** No way to validate insights or take action

---

## NICE-TO-HAVE (Enhanced MVP - Version 1.1)
*Features that improve UX but aren't blockers for launch*

### 6. **Sample Data/Demo Mode**
- **Why:** Lowers barrier to entry, lets users try before uploading
- **Effort:** Low (use existing `customer_reviews.csv`)
- **Impact:** Medium (helps adoption)

### 7. **Download Results as CSV**
- **Why:** Users want to share findings with colleagues
- **Effort:** Low (pandas `.to_csv()`)
- **Impact:** Medium (convenience feature)

### 8. **Sentiment Score Display**
- **Why:** Adds nuance beyond positive/neutral/negative
- **Effort:** Low (OpenAI already returns scores)
- **Impact:** Medium (power users appreciate detail)

### 9. **Error Handling & User Feedback**
- **Why:** Graceful handling of bad CSV formats, API errors
- **Effort:** Medium
- **Impact:** High (prevents frustration)
- **Decision:** Include if time permits

### 10. **Loading Indicators & Progress Bars**
- **Why:** Transparency during API calls (can take 30+ seconds)
- **Effort:** Low (`st.spinner()`, `st.progress()`)
- **Impact:** High (perceived performance)
- **Decision:** Include if time permits

---

## NEXT VERSION (Version 2.0+)
*Features requiring more complexity or validation*

### 11. **Time-Series Analysis**
- **Why:** Track sentiment trends over time
- **Why Later:** Requires date parsing, aggregation logic, more complex viz
- **User Story:** "As a PM, I want to see if sentiment improved after our product update"

### 12. **Custom Sentiment Categories**
- **Why:** Some teams want more than 3 categories (e.g., "frustrated", "delighted")
- **Why Later:** Requires prompt engineering, UI complexity

### 13. **Multi-File Upload / Batch Processing**
- **Why:** Enterprise users have data across multiple files
- **Why Later:** Adds complexity, not validated as needed yet

### 14. **Export as PDF Report**
- **Why:** Stakeholder-ready reports
- **Why Later:** Requires report templating, design work

### 15. **Save & Share Analysis**
- **Why:** Collaboration across teams
- **Why Later:** Requires database, user auth, URL routing

### 16. **Custom OpenAI Model Selection**
- **Why:** Power users want to experiment with models
- **Why Later:** Most users don't need this control

### 17. **Keyword/Topic Extraction**
- **Why:** Identify common themes in negative reviews
- **Why Later:** Requires NLP pipeline beyond sentiment

### 18. **Email Alerts for Negative Sentiment Spikes**
- **Why:** Proactive notification system
- **Why Later:** Requires scheduling, monitoring infrastructure

---

## Decision Framework Summary

**Launch with (Must-Have):** Features 1-5
**Add if time permits (Quick wins):** Features 9-10
**Validate demand before building (Nice-to-Have):** Features 6-8
**Defer to V2 (Next Version):** Features 11-18

**Estimated MVP Build Time:** 2-4 hours (for must-haves only)

---

## MVP Scope Statement

*"A single-page Streamlit app where non-technical users can upload a customer review CSV, automatically analyze sentiment using OpenAI, view a bar chart of sentiment distribution, and filter results by product to identify issues—all in under 2 minutes."*
