from agent import Agent, create_agent_hierarchy
from task import Task  # Include the task module
from utils import write_yaml_to_file

def is_task_doable(agent, task):
  # Replace this with your actual evaluation logic
  # Example: Check if agent skills cover all task requirements
  required_skills = set(task.inputs)
  return required_skills.issubset(set(agent.skills))

def main():
  # Define a root agent and its task
  root_agent = Agent("Project Manager", "Oversee project execution")
  task = Task("Develop a marketing strategy", inputs=["customer data", "market trends"])

  def task_evaluator(agent):
    return is_task_doable(agent, task)

  create_agent_hierarchy(root_agent, max_depth=3, branching_factor=2, task_evaluator=task_evaluator)

  # Check if the task is doable at the root level
  if is_task_doable(root_agent, task):
    print(f"Task '{task.description}' is considered doable by the Project Manager.")
  else:
    # Hierarchy might have sub-agents who can handle the task
    print(f"Root agent might need help. Hierarchy created for task evaluation.")
    write_yaml_to_file(root_agent, "agent.yaml")

if __name__ == "__main__":
  main()