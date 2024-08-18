class Task:
    def __init__(self, description, inputs=[], outputs=[], dependencies=[]):
        self.description = description
        self.inputs = inputs  # List of required data for the task
        self.outputs = outputs  # List of expected outputs from the task
        self.dependencies = dependencies  # List of other tasks that need to be completed before this task can begin

# Example usage
marketing_strategy_task = Task(
    "Develop a marketing strategy",
    inputs=["customer data", "market trends"],
    outputs=["marketing strategy document"]
)

content_creation_task = Task(
    "Create marketing content",
    inputs=["marketing strategy document", "brand guidelines"],
    outputs=["marketing materials"],
    dependencies=[marketing_strategy_task]  # Needs marketing strategy first
)