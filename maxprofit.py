import streamlit as st


def calculate_earnings(n, build_time, earn):
    """
    Calculate total earnings if only one type of building is constructed
    """
    t = build_time
    total = 0

    while t <= n:
        total += (n - t) * earn
        t += build_time

    return total


def max_profit_all_solutions(n):
    buildings = {
        "T": {"time": 5, "earning": 1500, "name": "Theatre"},
        "P": {"time": 4, "earning": 1000, "name": "Pub"},
        "C": {"time": 10, "earning": 2000, "name": "Commercial Park"}
    }

    profits = {}
    max_profit = 0

    for b, val in buildings.items():
        profit = calculate_earnings(n, val["time"], val["earning"])
        profits[b] = profit
        max_profit = max(max_profit, profit)

    solutions = []
    for b, profit in profits.items():
        if profit == max_profit and profit > 0:
            count = n // buildings[b]["time"]
            solutions.append({
                "T": count if b == "T" else 0,
                "P": count if b == "P" else 0,
                "C": count if b == "C" else 0
            })

    return max_profit, solutions


# ---------------- Streamlit UI ----------------

st.set_page_config(page_title="Max Profit Problem", layout="wide")

st.title("Max Profit Problem")

# Create two columns
left_col, right_col = st.columns([1, 2])

# -------- LEFT COLUMN: Building Details --------
with left_col:
    st.subheader("Building Details")

    st.markdown("""
    **Theatre (T)**
    - Build Time: **5 units**
    - Earnings: **$1500 / unit**
    - Size: 2×1 parcel  
    - Auditoriums: 8

    **Pub (P)**
    - Build Time: **4 units**
    - Earnings: **$1000 / unit**
    - Size: 1×1 parcel  
    - Dance Floor: 1

    **Commercial Park (C)**
    - Build Time: **10 units**
    - Earnings: **$2000 / unit**
    - Size: 3×1 parcel  
    - Commercial Spaces: 6
    """)

# -------- RIGHT COLUMN: Input & Results --------
with right_col:
    st.subheader("Input")

    time_units = st.number_input(
        "Enter Time Units (n)",
        min_value=1,
        step=1
    )

    if st.button("Calculate"):
        profit, solutions = max_profit_all_solutions(time_units)

        st.subheader(f"Earnings: ${profit}")

        st.subheader("Optimal Solutions")
        for i, s in enumerate(solutions, 1):
            st.write(
                f"**Solution {i}:**  "
                f"T: {s['T']}  |  "
                f"P: {s['P']}  |  "
                f"C: {s['C']}"
            )

        if not solutions:
            st.warning("No buildings can be constructed within the given time.")