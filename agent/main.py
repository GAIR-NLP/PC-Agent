from openai import OpenAI
from pcagent import PCAgent
from planner import PlannerAgent
from grounding import GroundingAgent

grounding_client = OpenAI(
    api_key="EMPTY",
    base_url="http://localhost:8000/v1",
)

plan_client = OpenAI(
    api_key="EMPTY",
    base_url="http://localhost:8002/v1",
)

def exec_task(task_description, output_queue=None):
    agent = PCAgent(PlannerAgent(plan_client), GroundingAgent(grounding_client), task_description, output_queue)
    agent.run()

if __name__ == "__main__":
    task_description = input("Please input the task description: ")
    exec_task(task_description)
