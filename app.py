# =========================================================
# NEXTGEN DEALER FINANCE LAB
# FULL STREAMLIT APP WITH TAMIL LEARNING SUPPORT
# =========================================================

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import warnings
import random

warnings.filterwarnings("ignore")

np.random.seed(42)

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="NextGen Dealer Finance Lab",
    page_icon="🏢",
    layout="wide"
)

# =========================================================
# HELPERS
# =========================================================

def currency(x):
    return f"₹{x:,.0f}"

def pct(x):
    return f"{round(x,2)}%"

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

.main {
    background-color: #F5F7FA;
}

.stMetric {
    background-color: white;
    padding: 15px;
    border-radius: 10px;
    border: 1px solid #E5E7EB;
}

h1, h2, h3 {
    color: #1F2937;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# TITLE
# =========================================================

st.title("🏢 NextGen Dealer Finance Lab")

st.subheader("Run Smarter. Grow Stronger.")

st.markdown("""

Welcome to the experiential learning platform for
next-generation dealership leaders.

This lab helps participants understand:

✅ Profitability  
✅ Cash Flow  
✅ Credit Control  
✅ Inventory Management  
✅ Business Growth  
✅ Digital Transformation  
✅ Financial Decision Making  

through practical simulations and interactive dashboards.

""")

# =========================================================
# SIDEBAR
# =========================================================

language = st.sidebar.selectbox(

    "🌐 Learning Language",

    [

        "English",
        "English + தமிழ்"

    ]
)

menu = st.sidebar.radio(

    "Choose Business Module",

    [

        "Business Health Dashboard",

        "Profitability Engine",

        "Cash Flow Simulator",

        "Credit Control Lab",

        "Inventory Management",

        "Pricing Decision Game",

        "Dealer Growth Simulator",

        "Working Capital Tracker",

        "Customer Profitability",

        "Break-even Calculator",

        "Digital Transformation Score",

        "NextGen Leadership",

        "Business Decision Challenge",

        "Action Plan Generator"

    ]
)

# =========================================================
# BUSINESS WISDOM
# =========================================================

tips = [

    "Cash flow தான் business-ஓட உயிர்.",

    "Fast collection = strong business.",

    "Inventory control என்பது hidden profit.",

    "Data வைத்து decision எடுத்தால் growth வேகம் அதிகம்.",

    "Digital systems future growth-க்கு மிகவும் முக்கியம்."

]

if language == "English + தமிழ்":

    st.info(f"💡 Business Wisdom: {random.choice(tips)}")

# =========================================================
# BUSINESS DASHBOARD
# =========================================================

if menu == "Business Health Dashboard":

    st.header("📊 Business Health Dashboard")

    col1, col2 = st.columns(2)

    with col1:

        monthly_sales = st.number_input(
            "Monthly Sales",
            value=5000000.0,
            key="sales_dashboard"
        )

        monthly_expenses = st.number_input(
            "Monthly Expenses",
            value=4200000.0,
            key="expense_dashboard"
        )

    with col2:

        receivables = st.number_input(
            "Outstanding Receivables",
            value=2500000.0,
            key="receivable_dashboard"
        )

        inventory = st.number_input(
            "Inventory Value",
            value=3000000.0,
            key="inventory_dashboard"
        )

    profit = monthly_sales - monthly_expenses

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Monthly Profit",
        currency(profit)
    )

    col2.metric(
        "Receivables",
        currency(receivables)
    )

    col3.metric(
        "Inventory",
        currency(inventory)
    )

    health_df = pd.DataFrame({

        "Metric": [

            "Sales",
            "Expenses",
            "Receivables",
            "Inventory"

        ],

        "Value": [

            monthly_sales,
            monthly_expenses,
            receivables,
            inventory

        ]

    })

    fig = px.bar(

        health_df,

        x="Metric",

        y="Value",

        title="Business Snapshot"

    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    health_score = 70

    if profit > 0:
        health_score += 10

    if receivables < monthly_sales:
        health_score += 10

    if inventory < monthly_sales:
        health_score += 10

    fig = go.Figure(go.Indicator(

        mode="gauge+number",

        value=health_score,

        title={'text': "Business Health Score"},

        gauge={

            'axis': {'range': [0, 100]},

            'bar': {'color': "darkblue"},

            'steps': [

                {'range': [0, 40], 'color': "red"},
                {'range': [40, 70], 'color': "orange"},
                {'range': [70, 100], 'color': "green"}

            ]

        }

    ))

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    if language == "English + தமிழ்":

        st.info("""
💡 தமிழ் விளக்கம்:

'Business strong ஆக இருக்க sales மட்டும் போதாது.
Profit, cash flow, collections எல்லாமே முக்கியம்.'
""")

# =========================================================
# PROFITABILITY ENGINE
# =========================================================

elif menu == "Profitability Engine":

    st.header("💰 Profitability Engine")

    sales = st.number_input(
        "Monthly Sales",
        value=5000000.0,
        key="profit_sales"
    )

    gross_margin = st.slider(
        "Gross Margin (%)",
        1,
        50,
        15,
        key="gross_margin"
    )

    operating_expenses = st.number_input(
        "Operating Expenses",
        value=400000.0,
        key="opex"
    )

    transport_cost = st.number_input(
        "Transport Cost",
        value=200000.0,
        key="transport"
    )

    discounts = st.number_input(
        "Discounts Given",
        value=150000.0,
        key="discount"
    )

    gross_profit = sales * gross_margin/100

    net_profit = (
        gross_profit -
        operating_expenses -
        transport_cost -
        discounts
    )

    col1, col2 = st.columns(2)

    col1.metric(
        "Gross Profit",
        currency(gross_profit)
    )

    col2.metric(
        "Net Profit",
        currency(net_profit)
    )

    profit_df = pd.DataFrame({

        "Category": [

            "Operating Expenses",
            "Transport",
            "Discounts",
            "Net Profit"

        ],

        "Value": [

            operating_expenses,
            transport_cost,
            discounts,
            max(net_profit,0)

        ]

    })

    fig = px.pie(

        profit_df,

        names="Category",

        values="Value",

        title="Profit Distribution"

    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    if language == "English + தமிழ்":

        st.success("""
💡 தமிழ் விளக்கம்:

'Sales பெரியதாக இருந்தாலும் profit இருக்க வேண்டும்.'

'Discount அதிகமானால் margin குறையும்.'
""")

# =========================================================
# CASH FLOW SIMULATOR
# =========================================================

elif menu == "Cash Flow Simulator":

    st.header("💸 Cash Flow Simulator")

    opening_cash = st.number_input(
        "Opening Cash Balance",
        value=1000000.0
    )

    monthly_collections = st.number_input(
        "Monthly Collections",
        value=3500000.0
    )

    monthly_payments = st.number_input(
        "Monthly Payments",
        value=3200000.0
    )

    delayed_payments = st.number_input(
        "Delayed Customer Payments",
        value=500000.0
    )

    closing_cash = (

        opening_cash +
        monthly_collections -
        monthly_payments -
        delayed_payments

    )

    st.metric(
        "Closing Cash Balance",
        currency(closing_cash)
    )

    if closing_cash < 0:

        st.error("🔴 Cash Flow Stress")

    elif closing_cash < 500000:

        st.warning("🟠 Tight Cash Position")

    else:

        st.success("🟢 Healthy Cash Flow")

    months = np.arange(1,13)

    cash_path = np.cumsum(

        np.random.normal(
            closing_cash,
            150000,
            12
        )

    )

    cash_df = pd.DataFrame({

        "Month": months,
        "Cash Balance": cash_path

    })

    fig = px.line(

        cash_df,

        x="Month",

        y="Cash Balance",

        title="Projected Cash Flow"

    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    if language == "English + தமிழ்":

        st.warning("""
💡 தமிழ் விளக்கம்:

'லாபம் இருந்தாலும் cash flow இல்லையெனில் business stress வரும்.'

'Collection fast-aa வந்தால் business strong-aa இருக்கும்.'
""")

# =========================================================
# CREDIT CONTROL LAB
# =========================================================

elif menu == "Credit Control Lab":

    st.header("📋 Credit Control Lab")

    customer_name = st.text_input(
        "Customer Name",
        value="ABC Constructions"
    )

    credit_amount = st.number_input(
        "Requested Credit",
        value=2500000.0
    )

    payment_days = st.slider(
        "Credit Period (Days)",
        0,
        180,
        90
    )

    decision = st.radio(

        "Decision",

        [

            "Approve",
            "Reject",
            "Partial Approval"

        ]
    )

    if decision == "Approve":

        st.warning("""
High sales opportunity,
but cash-flow risk increases.
""")

    elif decision == "Reject":

        st.info("""
Cash flow protected,
but sales opportunity lost.
""")

    else:

        st.success("""
Balanced risk approach.
""")

    risk_score = payment_days / 180 * 100

    fig = go.Figure(go.Indicator(

        mode="gauge+number",

        value=risk_score,

        title={'text': "Credit Risk Score"},

        gauge={

            'axis': {'range': [0, 100]},

            'steps': [

                {'range': [0, 40], 'color': "green"},
                {'range': [40, 70], 'color': "orange"},
                {'range': [70, 100], 'color': "red"}

            ]

        }

    ))

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    if language == "English + தமிழ்":

        st.info("""
💡 தமிழ் விளக்கம்:

'அதிக நாட்கள் credit கொடுத்தால் cash cycle slow ஆகும்.'

'Customer relationship முக்கியம்,
ஆனால் financial discipline அதைவிட முக்கியம்.'
""")
```
```python id="7h8x7j"
# =========================================================
# INVENTORY MANAGEMENT
# =========================================================

elif menu == "Inventory Management":

    st.header("📦 Inventory Management")

    inventory = st.number_input(
        "Current Inventory",
        value=3000.0,
        key="inventory_units"
    )

    monthly_demand = st.number_input(
        "Monthly Demand",
        value=2500.0,
        key="monthly_demand"
    )

    reorder_level = st.number_input(
        "Reorder Level",
        value=1000.0,
        key="reorder"
    )

    excess_inventory = inventory - monthly_demand

    st.metric(
        "Excess Inventory",
        round(excess_inventory,2)
    )

    if inventory > monthly_demand * 1.5:

        st.warning("""
Too much stock blocking cash.
""")

    elif inventory < reorder_level:

        st.error("""
Risk of stock-out.
""")

    else:

        st.success("""
Inventory levels healthy.
""")

    inventory_df = pd.DataFrame({

        "Type": [

            "Current Inventory",
            "Monthly Demand"

        ],

        "Units": [

            inventory,
            monthly_demand

        ]

    })

    fig = px.bar(

        inventory_df,

        x="Type",

        y="Units",

        title="Inventory vs Demand"

    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    if language == "English + தமிழ்":

        st.warning("""
💡 தமிழ் விளக்கம்:

'அதிக stock வைத்தால் cash block ஆகிவிடும்.'

'குறைவான stock இருந்தால் sales miss ஆகும்.'
""")

# =========================================================
# PRICING DECISION GAME
# =========================================================

elif menu == "Pricing Decision Game":

    st.header("🏷️ Pricing Decision Game")

    current_price = st.number_input(
        "Current Selling Price",
        value=400.0,
        key="current_price"
    )

    competitor_price = st.number_input(
        "Competitor Price",
        value=380.0,
        key="competitor_price"
    )

    strategy = st.selectbox(

        "Your Strategy",

        [

            "Match Competitor",
            "Maintain Price",
            "Offer Bundle"

        ]
    )

    margin_impact = current_price - competitor_price

    st.metric(
        "Price Difference",
        currency(margin_impact)
    )

    if strategy == "Match Competitor":

        st.warning("""
Sales volume may improve,
but margins reduce.
""")

    elif strategy == "Maintain Price":

        st.success("""
Margin protected,
but volume risk exists.
""")

    else:

        st.info("""
Value-added strategy.
""")

    if language == "English + தமிழ்":

        st.info("""
💡 தமிழ் கருத்து:

'Price குறைப்பது easy.
ஆனால் profit maintain செய்வது தான் smart business.'
""")

# =========================================================
# DEALER GROWTH SIMULATOR
# =========================================================

elif menu == "Dealer Growth Simulator":

    st.header("🚀 Dealer Growth Simulator")

    marketing = st.slider(
        "Investment in Marketing",
        0,
        100,
        25
    )

    technology = st.slider(
        "Investment in Technology",
        0,
        100,
        20
    )

    people = st.slider(
        "Investment in Team",
        0,
        100,
        30
    )

    inventory = st.slider(
        "Investment in Inventory",
        0,
        100,
        25
    )

    growth_score = (

        marketing +
        technology +
        people +
        inventory

    ) / 4

    st.metric(
        "Business Growth Score",
        round(growth_score,2)
    )

    categories = [

        "Marketing",
        "Technology",
        "People",
        "Inventory"

    ]

    values = [

        marketing,
        technology,
        people,
        inventory

    ]

    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(

        r=values,

        theta=categories,

        fill='toself',

        name='Growth Investment'

    ))

    fig.update_layout(

        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0,100]
            )
        ),

        showlegend=False

    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    if language == "English + தமிழ்":

        st.success("""
💡 தமிழ் கருத்து:

'Technology + disciplined finance + strong team = long-term growth.'
""")

# =========================================================
# WORKING CAPITAL TRACKER
# =========================================================

elif menu == "Working Capital Tracker":

    st.header("🏦 Working Capital Tracker")

    receivables = st.number_input(
        "Receivables",
        value=2500000.0
    )

    inventory = st.number_input(
        "Inventory",
        value=3000000.0
    )

    payables = st.number_input(
        "Payables",
        value=1800000.0
    )

    working_capital = (
        receivables +
        inventory -
        payables
    )

    st.metric(
        "Working Capital",
        currency(working_capital)
    )

    wc_df = pd.DataFrame({

        "Component": [

            "Receivables",
            "Inventory",
            "Payables"

        ],

        "Value": [

            receivables,
            inventory,
            payables

        ]

    })

    fig = px.bar(

        wc_df,

        x="Component",

        y="Value",

        title="Working Capital Components"

    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    if language == "English + தமிழ்":

        st.info("""
💡 தமிழ் விளக்கம்:

'Working capital தான் daily business operations-ஓட backbone.'
""")

# =========================================================
# CUSTOMER PROFITABILITY
# =========================================================

elif menu == "Customer Profitability":

    st.header("👥 Customer Profitability")

    customer_sales = st.number_input(
        "Customer Sales",
        value=1500000.0
    )

    customer_cost = st.number_input(
        "Customer Service Cost",
        value=1200000.0
    )

    customer_profit = (
        customer_sales -
        customer_cost
    )

    st.metric(
        "Customer Profit",
        currency(customer_profit)
    )

    customer_df = pd.DataFrame({

        "Metric": [

            "Sales",
            "Cost",
            "Profit"

        ],

        "Value": [

            customer_sales,
            customer_cost,
            customer_profit

        ]

    })

    fig = px.pie(

        customer_df,

        names="Metric",

        values="Value",

        title="Customer Profitability"

    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    if language == "English + தமிழ்":

        st.info("""
💡 தமிழ் கருத்து:

'ஒவ்வொரு customer-உம் profitable ஆக இருக்க வேண்டியது அவசியம்.'
""")
```
```python id="2xqfht"
# =========================================================
# BREAK-EVEN CALCULATOR
# =========================================================

elif menu == "Break-even Calculator":

    st.header("📈 Break-even Calculator")

    fixed_cost = st.number_input(
        "Fixed Costs",
        value=1000000.0
    )

    selling_price = st.number_input(
        "Selling Price Per Unit",
        value=400.0
    )

    variable_cost = st.number_input(
        "Variable Cost Per Unit",
        value=320.0
    )

    contribution = (
        selling_price -
        variable_cost
    )

    if contribution > 0:

        breakeven = fixed_cost / contribution

        st.metric(
            "Break-even Units",
            round(breakeven,2)
        )

        x = np.arange(0, 50000, 1000)

        revenue = x * selling_price
        total_cost = fixed_cost + x * variable_cost

        fig = go.Figure()

        fig.add_trace(go.Scatter(
            x=x,
            y=revenue,
            mode='lines',
            name='Revenue'
        ))

        fig.add_trace(go.Scatter(
            x=x,
            y=total_cost,
            mode='lines',
            name='Total Cost'
        ))

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    if language == "English + தமிழ்":

        st.info("""
💡 தமிழ் விளக்கம்:

'Break-even point தெரிந்தால் business risk குறையும்.'

'Sales எவ்வளவு வந்தால் loss இல்லாமல் இருக்கும் என்பதை இது காட்டும்.'
""")

# =========================================================
# DIGITAL TRANSFORMATION SCORE
# =========================================================

elif menu == "Digital Transformation Score":

    st.header("💻 Digital Transformation Score")

    upi = st.checkbox("UPI Payments")
    erp = st.checkbox("ERP System")
    whatsapp = st.checkbox("WhatsApp Business")
    analytics = st.checkbox("Analytics Dashboard")
    crm = st.checkbox("CRM Usage")

    score = sum([
        upi,
        erp,
        whatsapp,
        analytics,
        crm
    ])

    digital_score = score / 5 * 100

    st.metric(
        "Digital Readiness Score",
        pct(digital_score)
    )

    digital_df = pd.DataFrame({

        "Capability": [

            "UPI",
            "ERP",
            "WhatsApp",
            "Analytics",
            "CRM"

        ],

        "Adoption": [

            int(upi),
            int(erp),
            int(whatsapp),
            int(analytics),
            int(crm)

        ]

    })

    fig = px.bar(

        digital_df,

        x="Capability",

        y="Adoption",

        title="Digital Adoption"

    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    if language == "English + தமிழ்":

        st.success("""
💡 தமிழ் கருத்து:

'Digital tools time-ஐயும் money-ஐயும் save செய்யும்.'

'Technology பயன்படுத்தும் dealers future-ready ஆக இருப்பார்கள்.'
""")

# =========================================================
# NEXTGEN LEADERSHIP
# =========================================================

elif menu == "NextGen Leadership":

    st.header("🌟 NextGen Leadership")

    delegation = st.slider(
        "Delegation Ability",
        0,
        10,
        5
    )

    innovation = st.slider(
        "Innovation Mindset",
        0,
        10,
        7
    )

    discipline = st.slider(
        "Financial Discipline",
        0,
        10,
        6
    )

    leadership_score = (
        delegation +
        innovation +
        discipline
    ) / 3 * 10

    st.metric(
        "Leadership Score",
        pct(leadership_score)
    )

    leadership_categories = [

        "Delegation",
        "Innovation",
        "Discipline"

    ]

    leadership_values = [

        delegation,
        innovation,
        discipline

    ]

    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(

        r=leadership_values,

        theta=leadership_categories,

        fill='toself'

    ))

    fig.update_layout(

        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0,10]
            )
        ),

        showlegend=False

    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    if language == "English + தமிழ்":

        st.info("""
💡 தமிழ் சிந்தனை:

'குடும்ப business-ஐ professional business-ஆக மாற்றுவது next generation பொறுப்பு.'

'Leadership என்பது people + systems + discipline.'
""")

# =========================================================
# BUSINESS DECISION CHALLENGE
# =========================================================

elif menu == "Business Decision Challenge":

    st.header("🎯 Business Decision Challenge")

    st.markdown("""

A large contractor requests:

- ₹40 lakh order
- 120-day credit
- extra discount

What will you do?

""")

    decision = st.radio(

        "Choose Your Action",

        [

            "Accept Full Order",
            "Negotiate Terms",
            "Reject Order"

        ]

    )

    if decision == "Accept Full Order":

        st.warning("""
High sales growth,
but major cash-flow risk.
""")

    elif decision == "Negotiate Terms":

        st.success("""
Balanced business decision.
""")

    else:

        st.info("""
Financially conservative approach.
""")

    if language == "English + தமிழ்":

        st.warning("""
💡 தமிழ் கருத்து:

'Sales மட்டும் பார்க்காமல் risk-யும் evaluate செய்ய வேண்டும்.'

'Smart dealer எப்போதும் cash flow-ஐ கவனிப்பார்.'
""")

# =========================================================
# ACTION PLAN GENERATOR
# =========================================================

elif menu == "Action Plan Generator":

    st.header("📝 My 90-Day Action Plan")

    finance_goal = st.text_input(
        "One Financial Improvement"
    )

    operations_goal = st.text_input(
        "One Operations Improvement"
    )

    digital_goal = st.text_input(
        "One Digital Improvement"
    )

    action_plan = f"""

NEXTGEN DEALER ACTION PLAN

Financial Goal:
{finance_goal}

Operations Goal:
{operations_goal}

Digital Goal:
{digital_goal}

"""

    st.download_button(

        label="Download My Action Plan",

        data=action_plan,

        file_name="nextgen_action_plan.txt"

    )

    st.success("""
Your personalized dealership improvement plan is ready.
""")

    if language == "English + தமிழ்":

        st.success("""
💡 தமிழ் Reflection:

'அடுத்த 90 நாட்களில் உங்கள் business-ல் என்ன மாற்றப் போகிறீர்கள்?'

'Small improvements create long-term growth.'
""")
```
# =========================================================
# FOOTER
# =========================================================

st.markdown("---")

st.caption("""
🏢 NextGen Dealer Finance Lab

Designed for experiential learning in dealership business management.
Developed and Designed by Prof.Shalini Velappan, IIM Trichy

Focus Areas:
Profitability | Cash Flow | Growth | Digital Transformation | Leadership

""")
