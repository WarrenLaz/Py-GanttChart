import pandas as pd
import plotly.express as px

# Define the data
data = {
    "Task": [
        "Software Project Management Plan (A)", "Requirement Gathering (B)", "Requirement Creation (C)", 
        "Requirement Validation (D)", "UX/UI Design (E)", "Code Development (F)", 
        "Backend API Setup (G)", "Database Initialization and Schema Design (H)", 
        "Physician Registration and Authentication (I)", "Physician Dashboard - Overview Module (J)", 
        "Patient Management - Account and Medication (K)", "Medication Tracking - Monitoring Tools (L)", 
        "Notifications for Physicians (M)", "Patient Dashboard (N)", "Medication Logging (Daily Tracking) (O)", 
        "Refill Request System (Patient Side) (P)", "User Notifications (Patient Side) (Q)", 
        "Refill Suggestion Algorithm (S)", "Batch Request Generation (T)", "Code Reviews (U)", 
        "Unit Testing (V)", "Integration Testing (W)", "System Testing (X)", "Validation Testing (Y)", 
        "Deployment (Z)", "Final Acceptance Validation (Alpha)"
    ],
    "Duration (Hours)": [
        10, 20, 20, 20, 20, 750, 20, 25, 30, 60, 50, 35, 15, 50, 30, 10, 10, 50, 50, 80, 100, 100, 100, 100, 50, 20
    ],
    "Start Date": [
        "2024-09-18", "2024-09-26", "2024-10-03", "2024-10-13", "2024-10-17", "2024-10-22", 
        "2024-10-22", "2024-10-30", "2024-11-04", "2024-11-10", "2024-11-20", "2024-11-28", 
        "2024-01-06", "2024-01-06", "2024-02-01", "2024-12-01", "2024-12-01", "2024-12-01", 
        "2024-02-22", "2024-10-23", "2024-10-25", "2024-11-01", "2024-11-10", "2024-11-20", 
        "2025-02-09", "2025-02-23"
    ],
    "End Date": [
        "2024-09-25", "2024-10-02", "2024-10-11", "2024-10-16", "2024-10-22", "2025-02-08", 
        "2024-10-31", "2024-11-03", "2024-11-07", "2024-11-20", "2024-11-25", "2024-12-05", 
        "2024-01-06", "2024-01-06", "2024-01-06", "2024-12-01", "2024-12-01", "2024-12-01", 
        "2024-03-22", "2025-02-08", "2025-01-20", "2025-02-02", "2025-02-08", "2025-02-06", 
        "2025-02-22", "2025-03-31"
    ],
    "Person Responsible": [
        "Heba", "Celine", "Celine", "Rhonda", "Rhonda", "All", "Warren, Celine", "Warren, Celine", 
        "Warren, Celine", "Heba, Rhonda", "Heba, Rhonda", "Heba, Rhonda", "Celine", "Rhonda", 
        "Heba", "Heba", "Celine", "Warren", "Warren", "Rhonda", "Heba", "Heba", "Celine", "Rhonda", 
        "Warren", "Celine"
    ],
    "Group": [
        "Management", "Management", "Management", "Management", "Frontend", "Development", 
        "Development", "Development", "Development", "Development", "Development", "Development", 
        "Development", "Frontend", "Development", "Backend", "Development", "Backend", 
        "Backend", "Development", "Development", "Development", "Development", "Development", 
        "Backend", "Management"
    ],
    "Complete %": [
        100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 60, 60, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    ]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Convert date columns to datetime format
df['Start Date'] = pd.to_datetime(df['Start Date'])
df['End Date'] = pd.to_datetime(df['End Date'])

# Create the Gantt chart
fig = px.timeline(
    df, x_start="Start Date", x_end="End Date", y="Task", color="Group", 
    title="Project Gantt Chart", labels={"Duration (Hours)": "Duration (hours)"},
    hover_data=["Person Responsible", "Complete %"]
)
fig.update_yaxes(categoryorder="total ascending")  # Order tasks by start date

fig.show()
