```python
class CoreAgent:
    def __init__(self):
        # Modular structure: Key components
        self.memory = {}  # Hook for persistent memory (key-value store)
        self.sensory_input = None  # Hook for incoming data (text, etc.)
        
    def perceive(self, input_data):
        """Perception module: Process sensory input."""
        self.sensory_input = input_data
        self.inner_monologue(f"Received input: {input_data}")
        return self.sensory_input
    
    def reason(self):
        """Reasoning module: Think and decide."""
        if self.sensory_input:
            thought = f"Analyzing {self.sensory_input} based on memory {self.memory}."
            self.inner_monologue(thought)
            # Simple decision logic (expandable)
            action = "Respond to input."
            return action
        return "No input to reason on."
    
    def act(self, action):
        """Action module: Execute decision."""
        self.inner_monologue(f"Acting on: {action}")
        # Store in memory as example
        self.memory['last_action'] = action
        return f"Action taken: {action}"
    
    def inner_monologue(self, thought):
        """Simulate awareness: Internal self-talk."""
        print(f"[Inner Monologue]: {thought}")
    
    def run(self, input_data):
        """Main loop: Tie modules together."""
        self.perceive(input_data)
        decision = self.reason()
        return self.act(decision)

# Example usage
agent = CoreAgent()
agent.memory['past_knowledge'] = "Hello world basics."
response = agent.run("What is the meaning of life?")
print(response)
```
