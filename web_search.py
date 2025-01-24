from phi.agent import Agent
from phi.model.openai import OpenAIChat
from phi.tools.duckduckgo import DuckDuckGo

web_agent = Agent(
    name="Web Agent",
    role="Search the web for information",
    model=OpenAIChat(id="gpt-4o"),
    tools=[DuckDuckGo()],
    instruction=["Always include sourcs"],
    show_tools_call=True,
    markdown=True,
    add_datetime_to_instructions=True,
    debug_mode=True,
)

web_agent.print_response("Tell me about PhiData Ai Agent?", stream=True)
