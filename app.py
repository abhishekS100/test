import streamlit as st
from agents import agents

st.title("📡 Comcast Business AI Sales Assistant")
st.subheader("Powered by Google Cloud Agentic AI")

scenario = st.selectbox("Choose Scenario", ["Support", "Billing", "Sales"])
user_input = st.text_area("Customer Says...", placeholder="Hi, my internet is slow...")

if st.button("Run Agent"):
    if scenario and user_input:
        agent = agents[scenario.lower()]
        response = agent.chat(user_input)
        st.write("### 🤖 Agent Response")
        st.markdown(response.text)

        if response.tools_called:
            st.write("### 🔧 Tool Actions")
            for tool_result in response.tools_called:
                st.json(tool_result.result)
