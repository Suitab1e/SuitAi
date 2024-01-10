# SuitAi

Test first commit

# test start

cd desktop/SuitAi
source venv/bin/activate
rasa run actions

cd desktop/SuitAi
source venv/bin/activate
rasa shell

# Activating virtual env

	source venv/bin/activate


# Starting/Stopping Rasa bot
	rasa shell

	/stop

	rasa run actions

# Train model 

	rasa train


## Notes 

Step 1: Define Intents and Entities

Identify Intents:
Greet Intent: For the chatbot to greet the user.
AskBrand, AskStyle, AskFit, AskCollarSize Intents: For each of the four questions.

Specify Entities:
Entities like brand, style, fit, collar_size that the bot needs to capture from user inputs.

Step 2: Create Initial Training Data
NLU Training Data:
Add examples in data/nlu.yml for each intent.
Include phrases users might use to express each intent and annotate entities.

Initial Stories:
Write simple stories in data/stories.yml reflecting a basic conversation flow.

Step 3: Domain Configuration
Define the chatbot's domain in domain.yml, listing all intents, entities, responses for greetings, and placeholders for the four questions.

Step 4: Basic Custom Actions (Placeholder for Now)
Set up placeholder custom actions in actions/. These will later be used for database queries.

Step 5: Rasa Model Configuration
Configure config.yml for the NLU pipeline and policy ensemble. Start with a basic setup which can be adjusted later.

Step 6: Train the Rasa Model
Run rasa train to train your chatbot on the initial data.

Step 7: Test the Basic Interaction
Use rasa shell to test the basic conversation flow (greeting and asking the four questions).

Step 8: Iterative Development
Refine your training data, domain configurations, and stories based on the initial testing.
Regularly commit and push changes to GitHub.

Step 9: Adding Database Interaction
Once the basic flow is working, start integrating custom actions to interact with your SQL database.

Step 10: Advanced Stories and Testing
Develop more complex stories to handle various user paths and responses.
Continuously test and refine the bot's responses and database interactions.

Step 11: Final Testing and Refinement
Ensure all paths and scenarios are covered and tested.
Fine-tune the responses, custom actions, and database queries.

Step 12: Preparing for Future UI Integration
Consider how the bot will integrate with a UI, preparing for REST API or other communication methods.


## Summary 
Certainly! Here's a more concise summary of the progress on your Rasa chatbot project:

1. Project Setup
Initiated a Rasa project, creating the necessary structure for the chatbot.
2. Intents and Entities
Configured data/nlu.yml to define key user intents (greet, goodbye, inform_brand, etc.) and provided annotated examples for each, highlighting how the bot should recognize user input.
3. Domain Configuration
Prepared the domain.yml file, detailing the chatbot's intents, entities, slots, responses, and actions, which collectively define how the chatbot should interpret and respond to inputs.
4. Stories Creation
Developed stories.yml with sample conversation paths that guide the chatbot on how to interact based on user intents and bot actions.
5. Establishing Rules
Formulated rules.yml to set specific, predictable response patterns for certain user intents, ensuring consistent bot behavior in these scenarios.
7. Training and Testing
Performed model training with rasa train and conducted initial testing using rasa shell to validate the chatbot's conversational capabilities.
Next Steps
The focus will be on further refining the chatbot, testing its interactions, and potentially integrating advanced features for enhanced functionality.
