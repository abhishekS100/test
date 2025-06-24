from google.generativeai.agentchat import Agent, Tool
from tools import recommend_plan, submit_order

recommendation_tool = Tool(
    name="recommend_plan",
    description="Recommends internet or service plans based on customer profile",
    function=recommend_plan
)

order_tool = Tool(
    name="submit_order",
    description="Submits an order and confirms the upgrade",
    function=submit_order
)

support_agent = Agent(
    name="SupportAgent",
    role="Technical Support Expert",
    instructions="Help troubleshoot technical issues and suggest upgrades.",
    tools=[recommendation_tool, order_tool]
)

billing_agent = Agent(
    name="BillingAgent",
    role="Billing Advisor",
    instructions="Help customers with billing concerns and suggest appropriate plans.",
    tools=[recommendation_tool]
)

sales_agent = Agent(
    name="SalesAgent",
    role="Sales Optimization AI",
    instructions="Identify opportunities and upsell suitable services to customers.",
    tools=[recommendation_tool, order_tool]
)

agents = {
    "support": support_agent,
    "billing": billing_agent,
    "sales": sales_agent
}
