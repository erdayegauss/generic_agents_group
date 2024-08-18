import random
import json

class Agent:
    def __init__(self, role, goal, skills=[], sub_agents=[]):
        self.role = role
        self.goal = goal
        self.skills = skills
        self.sub_agents = sub_agents



def create_agent_hierarchy(root_agent, max_depth, branching_factor, task_evaluator):
    if max_depth == 0:
        return

    for _ in range(branching_factor):
        sub_agent = Agent(
            role=f"Sub-agent of {root_agent.role}",
            goal=f"Supports {root_agent.role} in achieving its goal",
            skills=[]  # Add skills as needed
        )
        root_agent.sub_agents.append(sub_agent)

        if task_evaluator(sub_agent):
            # Task is doable, no need to create further hierarchy
            continue
        else:
            create_agent_hierarchy(sub_agent, max_depth - 1, branching_factor, task_evaluator)

def task_evaluator(agent):
    # Placeholder for task evaluation logic
    # Example: Check if agent's skills are sufficient for the task
    required_skills = ["skill1", "skill2"]
    return all(skill in agent.skills for skill in required_skills)



def save_agent_hierarchy(agents, filename="agents.json"):
    with open(filename, "w") as f:
        json.dump([agent.__dict__ for agent in agents], f, indent=4)

def load_agent_hierarchy(filename="agents.json"):
    with open(filename, "r") as f:
        agent_data = json.load(f)
        agents = [Agent(**agent_dict) for agent_dict in agent_data]
        return agents