## Inspiration
In a time where natural disasters seem to be happening more often, it's important to know how to immediately pack for emergencies. With the growing impacts of global warming and man-made disasters—Hurricane Milton (2024), Flooding in various regions of Brazil (2024-25), Earthquake at the Noto Peninsula in Japan (2025), California forest fires (2025). These events remind us how unpredictable life can be. It's imperative to prepare quickly for such emergencies, and one of the best ways to do that is by having a go-bag—a bag packed with essentials so you can leave quickly when disaster strikes. 

With these challenges in mind, we were inspired to create **ReadySetGo**:  AI-powered Retrieval-Augmented Generation (RAG) solution designed to simplify emergency packing decisions. Our goal is to help individuals make quick, informed choices during evacuations and emergencies, ensuring efficiency and preparedness when time is of the essence.

## What it does
ReadySetGo is an AI-powered emergency packing assistant designed to make survival planning simpler and faster. It combines Retrieval-Augmented Generation (RAG) technology with an interactive user interface to assist users in critical moments. It offers various key features:

- Knowledge Retrieval: ReadySetGo fetches relevant survival information, such as essential packing lists, safety guidelines, and general emergency advice from a Snowflake knowledge base. This ensures recommendations are backed by reliable and context-specific data.

- AI-Powered Packing Advice: Mistral’s advanced embedding and generative models are utilized to analyze user inputs, understand their emergency scenarios, and generate curated packing recommendations in real time.

- Interactive Chat Interface: The user-friendly Streamlit interface allows users to engage in a natural conversation, ask questions about emergencies, and receive implementable advice.

- Seamless Efficiency: ReadySetGo incorporates caching for embeddings, reducing redundancy and improving response speed. Built-in error handling ensures robust performance during critical moments.

## How we built it
ReadySetGo was developed as a modern, AI-powered Retrieval-Augmented Generation (RAG) solution using Snowflake for database management, Streamlit for the frontend interface, and Mistral’s API for embedding generation and natural language processing. Below is an in-depth look at the architecture, the technologies we used, and key components that make up the solution.

## Overall Architecture
The ReadySetGo architecture is designed to integrate AI capabilities seamlessly into a user-friendly web application. Here's an overview of its components:

1. **Frontend**:
Built with Streamlit, the frontend provides an interactive interface where users can interact with the AI assistant by posing emergency packing-related queries.
2. **Backend**:
The backend consists of Python scripts that: Fetch relevant knowledge base documents from Snowflake, use Mistral’s embedding model to generate semantic embeddings for user queries and knowledge base content, process the embeddings to retrieve contextually relevant documents, generate AI responses using Mistral’s large language model.
3. **Database**: A Snowflake database is used to store the knowledge base, which contains emergency packing information. The database is queried dynamically to fetch relevant documents based on user queries.
4. **Embedding and Retrieval**:
Mistral API is used to create semantic embeddings for both the user query and stored knowledge base content. A local embedding cache implemented with Pickle ensures efficient reuse of embeddings to save resources.

## Challenges we ran into
1. **Integrating Multiple Technologies**:
We were integrating several technologies, including Mistral's AI API, Snowflake for database queries, and Streamlit for the frontend, each with their own requirements and configurations. Managing these interactions proved to be slightly challenging.
2. **Maintaining Session State for Chat History**:
We had to ensure that the session state was handled properly in order to maintain a continuous conversation. Streamlit's session state management tool was leveraged.
3. **Scaling the Knowledge Base**: A growing knowledge base caused an increased computational load and increased query volume. We structured the knowledge base with tags and categories, allowing for more efficient retrieval of documents.

## Accomplishments that we're proud of
We’re thrilled to have created ReadySetGo, an AI-powered tool designed to help users make quick, informed packing decisions during emergencies, especially in natural disasters:

- **AI-Powered, Context-Sensitive Assistance**: Using Retrieval-Augmented Generation (RAG), ReadySetGo generates personalized packing suggestions based on the concerned emergency scenario. This ensures that user's get specific advice tailored to their emergency. 

- **Real-Time Data Retrieval**: Seamless integration with Snowflake allows for quick access to relevant documents, ensuring users get accurate, up-to-date packing advice.

- **User-Friendly Interface**: ReadySetGo’s chat interface is to-the-point and simple, offering easy interaction, making it easy to use during high-pressure situations.

- **Useful for Natural Disasters**: ReadySetGo is a solution that can make a real difference during natural disasters, helping people pack efficiently and stay safe.

## What we learned
- **Optimizing AI for Contextual Responses**: We learned how to fine-tune AI models for accurate and context-sensitive recommendations, ensuring that packing advice is tailored to specific emergency scenarios.

- **Efficient Data Retrieval and Integration**: Handling datasets and integrating them with Snowflake taught us how to efficiently retrieve relevant information in real-time, which is crucial during urgent situations.

- **Integrating Frontend and Backend**: Working with both Streamlit for the frontend and Mistral for AI-powered content generation deepened our understanding of full-stack development and how to seamlessly integrate AI with user interfaces for smooth user experiences.

- **Importance of Scalability in Critical Applications**: We understood the importance of building scalable systems that can handle high user loads along with fast, reliable responses.

## What's next for ReadySetGo - Packing For Survival, Simplified
- **Real-Time Updates**: We aim to incorporate real-time updates for emergency situations, ensuring that users receive the latest, most relevant packing suggestions as circumstances evolve, such as shifting weather conditions or new disaster alerts, specific to their location. 

- **Expanded and Specific Information**: We plan to integrate more specialized data, including region-specific disaster response guidelines and local emergency resource information to provide even more specific implementable recommendations.
