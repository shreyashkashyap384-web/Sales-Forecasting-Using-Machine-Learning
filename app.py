
"""
Improved Streamlit Dashboard
Replace your existing app.py with this file.
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import joblib

st.set_page_config(page_title="Sales Forecasting Dashboard",
                   page_icon="📊",
                   layout="wide")

st.markdown("""
<style>
.block-container{padding-top:1rem;}
.metric-card{
background:#1f2937;
padding:18px;
border-radius:12px;
border:1px solid #3b82f6;
text-align:center;
}
.small{color:#cbd5e1;font-size:13px;}
.footer{text-align:center;color:#bdbdbd;font-size:14px;padding:20px;}
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    return pd.read_csv("data/clean_sales.csv")

@st.cache_resource
def load_model():
    return joblib.load("models/sales_model.pkl")

@st.cache_resource
def load_cols():
    return joblib.load("models/feature_cols.pkl")

df=load_data()
model=load_model()
feature_cols=load_cols()

st.title("📈 Sales Forecasting Using ML with Python")
st.caption("Shreyash Kashyap | NAVIOTECH SOLUTIONS PVT. LTD.")

c1,c2,c3,c4=st.columns(4)
c1.metric("💰 Total Sales",f"${df['Sales'].sum():,.0f}")
c2.metric("💵 Total Profit",f"${df['Profit'].sum():,.0f}")
c3.metric("📦 Orders",len(df))
c4.metric("📊 Avg Sale",f"${df['Sales'].mean():.2f}")

st.divider()

st.sidebar.header("Prediction")

ship=st.sidebar.selectbox("Ship Mode",sorted(df["Ship Mode"].unique()))
segment=st.sidebar.selectbox("Segment",sorted(df["Segment"].unique()))
country=st.sidebar.selectbox("Country",sorted(df["Country"].unique()))
city=st.sidebar.selectbox("City",sorted(df["City"].unique()))
state=st.sidebar.selectbox("State",sorted(df["State"].unique()))
region=st.sidebar.selectbox("Region",sorted(df["Region"].unique()))
sub=st.sidebar.selectbox("Sub-Category",sorted(df["Sub-Category"].unique()))
prod=st.sidebar.selectbox("Product",sorted(df["Product Name"].unique()))
qty=st.sidebar.number_input("Quantity",1,20,2)
discount_percent = st.sidebar.slider("Discount (%)", 0, 100, 0)

# Convert percentage to decimal for prediction
discount = discount_percent / 100
predict=st.sidebar.button("Predict")

left,right=st.columns(2)

with left:
    monthly=df.groupby("Month",as_index=False)["Sales"].sum()
    st.plotly_chart(px.line(monthly,x="Month",y="Sales",markers=True,title="Monthly Sales Trend"),width="stretch")

with right:
    reg=df.groupby("Region",as_index=False)["Sales"].sum()
    st.plotly_chart(px.bar(reg,x="Region",y="Sales",title="Sales by Region"),width="stretch")

a,b=st.columns(2)

with a:
    seg=df.groupby("Segment",as_index=False)["Sales"].sum()
    st.plotly_chart(px.pie(seg,names="Segment",values="Sales",title="Sales by Segment"),width="stretch")

with b:
    prof=df.groupby("Sub-Category",as_index=False)["Profit"].sum().sort_values("Profit")
    st.plotly_chart(px.bar(prof,x="Profit",y="Sub-Category",orientation="h",
                           title="Profit by Sub-Category"),width="stretch")

c,d=st.columns(2)

with c:
    st.plotly_chart(px.scatter(df,x="Discount",y="Sales",color="Region",
                               title="Discount vs Sales"),width="stretch")

with d:
    st.plotly_chart(px.histogram(df,x="Sales",nbins=30,title="Sales Distribution"),
                    width="stretch")

st.subheader("📂 Dataset Explorer")
r=st.selectbox("Filter Region",["All"]+sorted(df["Region"].unique().tolist()))
show=df if r=="All" else df[df["Region"]==r]
st.dataframe(show,width="stretch",height=250)

st.subheader("🤖 Prediction Result")

if predict:
    sample=df.iloc[0].copy()
    sample["Ship Mode"]=ship
    sample["Segment"]=segment
    sample["Country"]=country
    sample["City"]=city
    sample["State"]=state
    sample["Region"]=region
    sample["Sub-Category"]=sub
    sample["Product Name"]=prod
    sample["Quantity"]=qty
    sample["Discount"]=disc

    sample["Order Date"]=pd.to_datetime(sample["Order Date"]).toordinal()
    sample["Ship Date"]=pd.to_datetime(sample["Ship Date"]).toordinal()

    tmp=pd.concat([df,pd.DataFrame([sample])],ignore_index=True)
    cat=["Order ID","Ship Mode","Customer ID","Customer Name","Segment",
         "Country","City","State","Region","Product ID","Category",
         "Sub-Category","Product Name","DayOfWeek"]
    for col in cat:
        tmp[col],_=pd.factorize(tmp[col])

    sample=tmp.iloc[-1]
    if "Sales" in sample: sample=sample.drop("Sales")
    if "Profit" in sample: sample=sample.drop("Profit")
    sample=sample[feature_cols]

    pred=model.predict(pd.DataFrame([sample]))[0]

    st.success(f"Predicted Sales : ${pred:,.2f}")

    x,y=st.columns(2)
    with x:
        st.info(f"""
**Model Used**

Random Forest Regressor

**Region:** {region}

**State:** {state}
""")
    with y:
        st.info(f"""
**Quantity:** {qty}

**Discount:** {discount_percent}%

**Status:** Prediction Successful ✅
""")

st.subheader("📈 Model Performance")

perf=pd.DataFrame({
    "Metric":["Model","MAE","RMSE","R² Score"],
    "Value":["Random Forest","199.03","404.93","0.465"]
})
st.table(perf)

with st.expander("ℹ️ About Project"):
    st.markdown("""
### Objective
Predict furniture sales using Machine Learning.

### Dataset
Furniture Sales Dataset (Superstore subset)

### Technologies
- Python
- Pandas
- Scikit-Learn
- Plotly
- Streamlit

### Workflow
EDA → Feature Engineering → Model Training → Prediction Dashboard
""")

st.markdown("<hr>",unsafe_allow_html=True)
st.markdown(
"<div class='footer'><b>Developed by Shreyash Kashyap</b><br>"
"Internship: NAVIOTECH SOLUTIONS PVT. LTD.</div>",
unsafe_allow_html=True)
