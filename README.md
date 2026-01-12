# 📊 Productivity Heatmap

A simple and beginner-friendly Python project that visualizes daily productivity using a heatmap, based on website usage and time spent.

This project helps you understand:
- ⏰ When you are most productive
- 🌐 Which type of websites affect your focus
- 📈 How productivity varies across hours and days


--------------------------------------------------
FEATURES
--------------------------------------------------

- Track website usage with time spent
- Categorize websites into:
  - Productive
  - Neutral
  - Distracting
- Automatically calculate productivity scores
- Visualize productivity using a color-coded heatmap
- Easy to understand and extend


--------------------------------------------------
PRODUCTIVITY SCORING LOGIC
--------------------------------------------------

Each website category is assigned a score:

Productive   → +1  
Neutral      →  0  
Distracting  → -1  

Hourly Productivity Score is calculated as:

Total Productive Minutes − Total Distracting Minutes

Heatmap Colors:
- Green  → Highly productive
- Yellow → Neutral
- Red    → Distracted


--------------------------------------------------
PROJECT STRUCTURE
--------------------------------------------------

productivity_heatmap/
|
|-- activity_log.csv
|-- heatmap.py
|-- README.md


--------------------------------------------------
INPUT DATA FORMAT (activity_log.csv)
--------------------------------------------------

The CSV file must contain the following columns:

date,hour,website,minutes,category

Example:

2026-01-12,9,github.com,40,productive
2026-01-12,9,youtube.com,20,distracting
2026-01-12,10,leetcode.com,60,productive
2026-01-12,11,google.com,30,neutral
2026-01-12,11,instagram.com,30,distracting

Column Description:
- date     → YYYY-MM-DD
- hour     → Hour of the day (0–23)
- website  → Website domain
- minutes  → Time spent during that hour
- category → productive / neutral / distracting


--------------------------------------------------
REQUIREMENTS
--------------------------------------------------

Install the required Python libraries using:

pip install pandas matplotlib seaborn


--------------------------------------------------
HOW TO RUN THE PROJECT
--------------------------------------------------

1. Place activity_log.csv and heatmap.py in the same folder
2. Open terminal or command prompt inside that folder
3. Run the following command:

python heatmap.py

4. A heatmap window will appear showing your productivity pattern


--------------------------------------------------
OUTPUT DETAILS
--------------------------------------------------

- X-axis → Hours of the day (0–23)
- Color intensity → Productivity level
- Visual insight into focus and distraction patterns


--------------------------------------------------
PLANNED UPGRADES
--------------------------------------------------

- Auto-detect hours from timestamps
- Multi-day heatmap (rows = days)
- Interactive Streamlit dashboard
- Automatic browser-based website tracking
- Weekly and monthly productivity analytics


--------------------------------------------------
WHY THIS PROJECT IS USEFUL
--------------------------------------------------

- Solves a real-life productivity problem
- Demonstrates data analysis and visualization skills
- Suitable for beginners
- Strong foundation for data analytics and Python projects
- Easily extendable to a professional-level application


--------------------------------------------------
CONTRIBUTIONS
--------------------------------------------------

Contributions, suggestions, and improvements are welcome.

