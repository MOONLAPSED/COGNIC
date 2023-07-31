<|SOS|>
`Co-cognition framework for IT/CS/AI learners; LLM-integration and utility - POSIX integration, unix file system, stdio, python & bash (xonsh)`

# COGNIC v0.91 - NLP+AI-assisted CS+IT learning project(s)

## Rules of Thumb & Heuristics

Creating a clear project structure is vital for seamless development. Consider these guidelines:

1. Use consistent naming conventions for keys and values to make understanding and searching easier.
2. Organize related data logically using nesting and arrays.
3. Provide comments to explain complex or ambiguous data.
4. Enhance readability with proper indentation for levels of hierarchy.
5. Use backticks to denote code or programming language syntax.
6. Keep the structure simple, avoiding unnecessary complexity.
7. Test and validate structured data to ensure accuracy and error-free implementation.

Key Considerations

1. **Understand the Project Purpose and Requirements**: Clearly define the project's purpose and target domain(s) such as Prompt Engineering, Prompt Generation, NLP tasks, or AI assistance. This understanding is crucial for effective customization.

2. **Clarity, Specificity, and Context**: Ensure the project is well-defined, specific, and contextually rich to generate desired responses effectively. Avoid ambiguity and vagueness.

3. **Include Relevant Data and Context**: Provide all relevant data and context within the project's objective or files. Use variables or placeholders for dynamic elements or files and folders.
   - **Define Variables and Placeholders**: Identify dynamic elements that require specific values during generation.
   - **Provide Examples and Data Sources**: Offer data examples to fill variables or placeholders, and reference external data sources if applicable.
   - **Contextual References**: Refer to past interactions to maintain context and coherence.

4. **Explicit Instructions and Guidelines**: Clearly specify instructions and constraints for new additions. Ensure even AI models or novices can comprehend the boundaries and limitations. For instance, "Calculate the dot product using a new class method without importing a new python library for it."
   - **Precise Language**: Use clear and concise language to express instructions. Avoid ambiguity or vagueness.
   - **Step-by-Step Instructions**: Break complex tasks into step-by-step instructions for effective user and AI model responses.
   - **Boundary Definitions**: Clearly define limitations for users, contributors, or AI models. Specify allowed methods, CLI arguments, etc.
   - **Example Usage**: Provide correct usage examples with expected responses for desired behavior.
   - **Error Handling**: Include instructions on handling potential errors or unexpected situations. Define fallback options or alternative instructions.

5. **Structured Data Formats**: Utilize JSON to represent the project's data and I/O. Consistent naming, nesting, and comments enhance readability and understanding.
   - **Example of a structured data format**: {"key": "value", "data": "syntax_hint"}
   - The provided JSON string object follows standard syntax with keys and string values enclosed in double quotes (") and separated by colons (:).
   - JSON validation libraries or built-in functions can programmatically validate the syntax.
   - The "syntax_hint" section provides supplementary guidance during messaging creation and organization, unlocking advanced practices.
   - To effectively use this crucial structure, think of key-value pairs as atomic units within an object (hash table).
   - Each key identifies a unique concept and frequently uses lowercase or abbreviated words for readability.
   - Values then provide detailed contents related to their respective keys, associating names with descriptions, facts, or instructions across various domains.
   - Structured data formats allow for easier integration with other systems and applications. eg: Many APIs require data to be in a specific format like json or bash.
   - Use a variety of data structures to store information, including arrays, dictionaries, hash tables, trees, graphs, strings, JSON, and other formats for text-based data.

Installation

COGNIC, will serve as an on-going research proof of these adumbrations as far as the public is conscerned. This codebase is experimental and not ready for end users. Only an expert should attempt to use any of this code because I am, at best, a Sophomore programmer and the code featured in this repo is not safely implimented.

Roadmap

 - client & server apps
   - Server handles computation & resources, hosts filesystem, COGNICs integration point into other LLM software and workflows like LogSeq, Firefox, AGiXT, LocalAI, Chainlit, Manifest, Wandb, LocalGPT, Textgen-webui, and GPT4ALL.
   - User interacts with the client; a browser-based fancy markdown editor and server interface. Client represents the #LogSeq portion of COGNIC's database functionality - serving also as a 'control' for COGNIC's growing server-side (AI-facing) databases. User handles the LogSeq integration themselves with copy & paste for now.
 - Server integration with other AI applications
   - xonsh scripts spin up docker containers for 'services'
 - Reverse engineer apis
 	 - gpt4all+LocalAI

Summary

In as few words as possible this project is a framework for extending my Zettelkasten LogSeq knowledge base and cultivating an organized 'second-brain.' COGNIC is the shared file-system for co-cognition between a primary learner(me) and any number of machine learning algorithms, language models, neural nets, etc. whilst handling additional training (on-top of the large foundation models) and logging in the simplest possible text:text RLHF personalized training knowledge bases (kb).

Glossary

- **#COGNIC**: The project name and identifier for the AI/NLP-assisted software coding project.
- **#rulesofthumb**: Guiding principles and heuristics for creating a clear project structure.
- **#heuristics**: Practical guidelines or rules of thumb to aid decision-making in the project development process.
- **#DataFormat**: The structured representation of data, often using formats like JSON, for efficient I/O and integration.
- **#GuidingPrinciples**: Fundamental principles that provide direction and guidance for the project's development.
- **#Integration**: The process of combining various components or modules to work together seamlessly.
- **#ArchitectureInspiration**: Concepts or ideas that serve as a foundation for the project's overall architecture.
- **#KnowledgeSharing**: The act of disseminating project-related information and insights among team members and stakeholders.
- **#Xonsh**: A Python-based, cross-platform shell language that integrates Python syntax and functionality with shell commands.
- **#Client-Server**: A computing architecture where a client requests resources or services from a server over a network.
- **#CodeExecution**: The process of running or executing code, often performed on the server in this project's context.
- **#Endpoint**: A specific URL or route on the server that responds to client requests.
- **#Client-ServerInteraction**: The communication and exchange of data between the client and server.
- **#ErrorHandling**: Strategies and techniques for dealing with errors and exceptions in the project.
- **#ClientView**: The presentation and visualization of data in the client-side interface.
- **#MVC**: The Model-View-Controller architectural pattern that separates concerns in the project.
- **#LooseCoupling**: Designing components with minimal dependencies on each other for better flexibility.
- **#AbstractionLayers**: Layers of abstraction that hide implementation details and provide simpler interfaces.
- **#RepositoryPattern**: An architectural pattern that separates the domain and data layers.
- **#DependencyInjection**: A technique that provides objects with their dependencies rather than creating them internally.
- **#Testing**: The process of evaluating and verifying the correctness and functionality of the project.
- **#DomainDrivenDesign**: An approach that focuses on modeling the project based on the domain it serves.
- **#PlainText**: Unformatted and human-readable text without additional markup or styling.
- **#CLI**: Command Line Interface, a text-based interface for interacting with the project.
- **#Scripting**: Using scripts to automate tasks and processes in the project.
- **#HardwareConstraints**: Limitations imposed by the hardware resources available for the project.
- **#Languages**: Programming languages used in the project's development.
- **#ComputerScienceBasics**: Fundamental concepts and principles of computer science relevant to the project.
- **#Endpoints**: Specific URLs or routes that handle client requests in the project's API.
- **#Responses**: The structured data or output provided by the server in response to client requests.
- **#Authentication**: The process of verifying the identity of a user or client.
- **#Validation**: Ensuring that inputs and outputs meet specified criteria or requirements.
- **#Versioning**: Managing and identifying different versions of the project or its components.
- **#RateLimiting**: Limiting the number of requests or actions a user or client can perform within a given time frame.
- **#Documentation**: Creating and maintaining project-related documentation to aid understanding and usage.
- **#SDKs**: Software Development Kits that provide tools and libraries for interacting with the project's API.
- **#Deployment**: The process of making the project available and functional in a production environment.
- **#Encryption**: Securing data through encoding and decoding using cryptographic techniques.
- **#DataHandling**: Managing and processing data within the project.
- **#AccessControl**: Controlling and managing user or client access to specific resources or features.
- **#LeastPrivilege**: Granting users or clients the minimum privileges necessary to perform their tasks.
- **#Monitoring**: Observing and collecting data about the project's performance and behavior.
- **#SecureSDLC**: Secure Software Development Life Cycle, integrating security measures throughout the project's development process.
- **#PrintDebugging**: Debugging technique using print statements to display information during runtime.
- **#Logging**: Recording events and activities within the project for analysis and debugging.
- **#Debugger**: A tool for interactive debugging and examining the project's execution.
- **#Assertions**: Statements that check the correctness of assumptions during development.
- **#UnitTesting**: Testing individual components or units of the project for correctness.
- **#Tracing**: Analyzing and understanding the flow of execution in the project.
- **#StaticAnalysis**: Evaluating the project's source code for potential issues without executing it.
- **#Linting**: The process of analyzing code for potential errors or violations of style guidelines.
- **#CodeReview**: Evaluating and providing feedback on the project's code by peers or experts.
- **#PostmortemAnalysis**: Examining and learning from failures or incidents in the project.
- **#Setuptools**: A package development and distribution tool in Python.
- **#Requirements.txt**: A file specifying the project's dependencies and their versions.
- **#VirtualEnvironments**: Isolated environments for managing Python package dependencies.
- **#Pip**: The package installer for Python packages.
- **#PyPI**: The Python Package Index, a repository of Python packages.
- **#Conda**: A package manager used for Python and other languages.
- **#Poetry**: A dependency management and packaging tool for Python projects.
- **#Versioning**: Managing and identifying different versions of the project or its components.
- **#StyleGuide**: A set of standards and conventions for consistent code formatting and organization.
- **#Docstrings**: Documentation strings providing information about functions and classes.
- **#SchemaDesign**: Designing the structure and layout of data schemas.
- **#DataPipelines**: A series of data processing steps for transforming and moving data.
- **#MessageQueues**: A mechanism for asynchronous communication between components.
- **#DataLakes**: Storage repositories for storing vast amounts of raw data in various formats.
- **#DataCleaning**: The process of identifying and correcting errors and inconsistencies in data.
- **#Metrics**: Measurable indicators used to assess performance and progress in the project.
- **#KPIs**: Key Performance Indicators, specific metrics used to evaluate success in the project.
- **#Dashboards**: Visual displays of data for real-time monitoring and decision-making.
- **#DataExploration**: Analyzing and investigating data to understand its characteristics and patterns.
- **#PerformanceTuning**: Optimizing the project's performance and resource utilization.
- **#MetadataManagement**: Organizing and managing metadata to enhance data discovery and understanding.
- **#HorizontalScaling**: Increasing capacity by adding more machines to the system.
- **#DataPartitioning**: Dividing data into smaller subsets for improved performance and manageability.
- **#Caching**: Storing frequently accessed data in memory for faster retrieval.
- **#LoadBalancing**: Distributing incoming network traffic across multiple servers.
- **#Retries**: Repeating failed operations or requests to achieve successful execution.
- **#RateLimiting**: Restricting the number of requests or operations to prevent overload or abuse.
- **#Auto-scaling**: Automatically adjusting resources based on demand or load.
- **#StressTesting**: Evaluating the project's performance under extreme conditions.
- **#Modularity**: Designing components that can be easily separated and replaced.
- **#SeparationofConcerns**: Isolating different aspects of the project's functionality.
- **#DRY**: Don't Repeat Yourself, avoiding duplications in the codebase.
- **#Abstraction**: Hiding implementation details behind a simple interface.
- **#FailFast**: Identifying and reporting issues as early as possible in the development process.
- **#SideEffects**: Unintended changes or actions that occur in addition to the intended ones.
- **#PureFunctions**: Functions with no side effects and consistent return values for the same inputs.
- **#YAGNI**: You Aren't Gonna Need It, avoiding unnecessary features or complexity.
- **#IntuitionBuilding**: Developing an understanding and familiarity with the project's domain.
- **#LocalAI**: It is designed to be used as a local alternative to OpenAI's API.

Xonsh Python REPL on server for use by client

   - Browser is frontend, Ubuntu server backend [[Client-Server]]
   - Python executes on the server, not the client [[Code Execution]]
   - Xonsh Python REPL endpoint on the server [[Endpoint]] [[Xonsh]]
   - The client sends code snippets which the endpoint executes [[Client-Server Interaction]]
   - Return output and errors as structured data [[Error Handling]]
   - Render output nicely in the client view [[Client View]]

Architecture

   - Separate model, view, controller concerns [[MVC]]
   - Loose coupling through interfaces [[Loose Coupling]]
   - Abstraction layers hide implementation details [[Abstraction Layers]]
   - Repository pattern separates domain and data [[Repository Pattern]]
   - Dependency injection provides flexibility [[Dependency Injection]]
   - Testability through isolated components [[Testing]]
   - Design focused on domain model not framework [[Domain Driven Design]]

Constraints

   - Scope limited to text files and Markdown [[Plain Text]]
   - Command line interfaces for accessibility [[CLI]]
   - Embrace Unix/POSIX compatibility, employing file-centric [[Scripting]]
   - Consumer hardware limitations [[Hardware Constraints]]
   - Restricted languages like Python and C [[Languages]]
   - Focus on core CS fundamentals [[Computer Science Basics]]

Python Rules of Thumb

   - Add input validation checks before processing user input (e.g., ensure that only valid JSON strings are accepted as input).
   - Check if required libraries/modules are imported and available before trying to use them, otherwise, raise an appropriate exception.
   - Consider adding more descriptive variable names, which makes the code easier to read and understand.
   - Use built-in functions like type() instead of explicit type checking (isinstance()), since they provide better performance when used appropriately.
   - Be careful when modifying global states inside a function, especially one without global.
   - When printing debug information, consider redirecting all messages to a log file so that logs are saved permanently.
   - Include docstrings for both your module and any public functions within it so users know what the code does and how to use it.
   - Implement unit tests to verify the correctness of the code under various conditions.
   - Consider refactoring long lines into multiple lines for clarity and ease of reading. In summary, there is always room for improvement, even in well-written code.

API Design Principles

   - Well-defined endpoints and routes [[Endpoints]]
   - Consistent response formats and codes [[Responses]]
   - Authentication and access control [[Authentication]]
   - Validation of inputs and outputs [[Validation]]
   - Versioning and backward compatibility [[Versioning]]
   - Rate limiting policies [[Rate Limiting]]
   - OpenAPI/Swagger documentation [[Documentation]]
   - Test suite covering cases [[Testing]]
   - Client SDKs for ease of use [[SDKs]]
   - Deployment configuration and scaling [[Deployment]]

Web Application Security

   - Encryption via TLS/SSL [[Encryption]]
   - Input sanitization and output encoding [[Data Handling]]
   - Access control for resources [[Access Control]]
   - The principle of least privilege [[Least Privilege]]
   - Monitoring, logging, and auditing [[Monitoring]]
   - Secure development practices [[Secure SDLC]]

Debugging Techniques

   - Print statement debugging [[Print Debugging]]
   - Logging at different verbosity levels [[Logging]]
   - Interactive debugger usage [[Debugger]]
   - Assertions to catch issues early [[Assertions]]
   - Unit testing key components [[Unit Testing]]
   - Tracing execution flows [[Tracing]]
   - Monitoring metrics and performance [[Monitoring]]
   - Static analysis for code quality [[Static Analysis]]
   - Code linting and formatting [[Linting]]
   - Code review and pair programming [[Code Review]]
   - Postmortem analysis of failures [[Postmortem Analysis]]

Python Packaging

   - Setuptools for wrapping and distributing [[Setuptools]]
   - Requirements.txt for dependencies [[Requirements.txt]]
	 - Virtual environments for isolation [[Virtual Environments]]
   - Pip and PyPI and Miniconda for installing packages [[Pip, PyPI, Conda]]
   - Poetry as an alternative to setuptools [[Poetry]]
   - Version using semantic versioning [[Versioning]]
   - Consistent style guide [[Style Guide]]
   - Testing suite for correctness [[Testing]]
   - Docstrings for API documentation [[Docstrings]]

Data Engineering

   - Design schema for analytics and data science [[Schema Design]]
   - Build data pipelines with workflow tools [[Data Pipelines]]
   - Leverage message queues for streaming [[Message Queues]]
   - Store data in data lakes [[Data Lakes]]
   - Cleanse and transform data [[Data Cleaning]]
   - Identify metrics and KPIs [[Metrics, KPIs]]
   - Implement dashboards for visibility [[Dashboards]]
   - Enable interactive data exploration [[Data Exploration]]
   - Optimize for analytic performance [[Performance Tuning]]
   - Metadata management for discovery [[Metadata Management]]

System Design Concepts

   - Scale horizontally for reliability [[Horizontal Scaling]]
   - Partition data for scalability [[Data Partitioning]]
   - Caching improves performance [[Caching]]
   - Use load balancers to distribute requests [[Load Balancing]]
   - Implement retries with exponential backoff [[Retries]]
   - Rate limiting prevents abuse [[Rate Limiting]]
   - Auto-scaling adapts to demand [[Auto-scaling]]
   - Benchmark and stress test for capacity [[Stress Testing]]

Software Engineering Principles

   - Modular components with clear interfaces [[Modularity]]
   - Loose coupling between modules [[Loose Coupling]]
   - Separation of concerns [[Separation of Concerns]]
   - Don't repeat yourself (DRY) [[DRY]]
   - Encapsulate complexity behind abstractions [[Abstraction]]
   - Fail fast to surface issues early [[Fail Fast]]
   - Minimize and isolate side effects [[Side Effects]]
   - Favor pure functions when possible [[Pure Functions]]
   - Prefer simplicity and avoid premature optimization [[YAGNI]]
   - Develop intuitions before diving into complexity [[Intuition Building]]

Co-cognition and collaboration

   Key considerations for human-AI co-cognition and collaboration:
   - Focus on simple text for portability and training [[Data Format]]
   - Principles of knowledge sharing, iteration, self-improvement [[Guiding Principles]]
   - Integrate with existing tools like LogSeq and apis [[Integration]]
   - Model human memory and learning via associations [[Architecture Inspiration]]
   - Maintain user privacy and ownership [[Knowledge Sharing]]

LocalAI Reveresed API endpoint from github

   [[LocalAI]] is a dockerized API endpoint for AI models. It is designed to be used as a local alternative to OpenAI's API. It is a reverse-engineered version of the OpenAI API, and it is not affiliated with OpenAI in any way. It is intended to be used for testing and development purposes only.
   - Docker-compose up -d --pull always
   - curl http://localhost:8080/v1/models
   - put your model in the models folder, note its name eg. orca-mini-7b.ggmlv3.q4_0.bin
   ```call
   (3ten) op@deV:~/cognic/LocalAI$ curl http://localhost:8080/v1/completions -H "Content-Type: application/json" -d '{
     "model": "orca-mini-7b.ggmlv3.q4_0.bin",            
     "prompt": "A long time ago in a galaxy far, far away",
     "temperature": 0.7
   }'
   ```
   ```response
   {"object":"text_completion","model":"orca-mini-7b.ggmlv3.q4_0.bin","choices":[{"index":0,"finish_reason":"stop","text":", there was a group of people who called themselves the Jedi. They were a religious order dedicated to using the Force for good and fighting against the dark side. One of these Jedi was named Luke Skywalker, who lived on the planet of Tatooine with his family. One day, he received a message from his friend and fellow Jedi, Obi-Wan Kenobi, asking him to come to the desert planet of Dagobah to receive Jedi training from the wise and powerful Master Yoda. Luke accepted the invitation and set off on a journey that would change the course of the galaxy forever."}],"usage":{"prompt_tokens":0,"completion_tokens":0,"total_tokens":0}}
   ```

Map of the project files

```
. .. ~/cognic/
├── ~/.scratch/             // Agent/user directory
└── ~/.logs/                // Logging directory
~/main/                     // COGNIC codebase
├── chat_manipulation.py    // Chatbot communications and message handling
├── client_application.py   // Client UI and controls for user interactions
├── docker_configuration.py // Docker container orchestration settings
├── filesystem_access.py    // Filesystem helpers
├── llama_model.py          // LLM integration  
├── server_administration.py // Server management
├── stdio_tasks.py          // Command line tools
├── threading_core_utils.py // Multithreading  
├── unix_functionality.py   // Unix/Linux helpers
├── virtualized_access.py   // Virtualization
├── web_application.py      // Web server code
├── xonsh_extension.py      // Xonsh helpers
└── main.py                 // Entry point
~/LocalAi/                  // Reversed API endpoint from GitHub
├── docker-compose.yml      // Docker Compose configuration for LocalAi
└── curl http://localhost:8080/v1/models // Sample API request to LocalAi
~/agents/
├── basher.py               // BASH-specialist LLM agent
└── prompter.py             // Meta-prompt specialist LLM agent
```

#### json project Map

{
  "status": "success",
  "message": "The map of project files has been provided.",
  "data": {
    "project_structure": [
      {
        "name": "cognic",
        "description": "Root directory for the COGNIC project.",
        "subdirectories": [
          {
            "name": ".scratch",
            "description": "Agent/user directory for temporary files and data."
          },
          {
            "name": ".logs",
            "description": "Logging directory for COGNIC's logs."
          }
        ]
      },
      {
        "name": "main",
        "description": "COGNIC codebase.",
        "files": [
          {
            "name": "chat_manipulation.py",
            "description": "Chatbot communications and message handling."
          },
          {
            "name": "client_application.py",
            "description": "Client UI and controls for user interactions."
          },
          {
            "name": "docker_configuration.py",
            "description": "Docker container orchestration settings."
          },
          {
            "name": "filesystem_access.py",
            "description": "Filesystem helpers for COGNIC."
          },
          {
            "name": "llama_model.py",
            "description": "Integration with Large Language Models (LLM)."
          },
          {
            "name": "server_administration.py",
            "description": "Server management code for COGNIC."
          },
          {
            "name": "stdio_tasks.py",
            "description": "Command line tools and tasks for COGNIC."
          },
          {
            "name": "threading_core_utils.py",
            "description": "Multithreading utilities."
          },
          {
            "name": "unix_functionality.py",
            "description": "Unix/Linux helpers for COGNIC."
          },
          {
            "name": "virtualized_access.py",
            "description": "Virtualization utilities for COGNIC."
          },
          {
            "name": "web_application.py",
            "description": "Web server code for COGNIC."
          },
          {
            "name": "xonsh_extension.py",
            "description": "Xonsh helpers for COGNIC."
          },
          {
            "name": "main.py",
            "description": "Entry point for COGNIC application."
          }
        ]
      },
      {
        "name": "LocalAi",
        "description": "Reversed API endpoint from GitHub.",
        "files": [
          {
            "name": "docker-compose.yml",
            "description": "Docker Compose configuration for LocalAi."
          },
          {
            "name": "curl http://localhost:8080/v1/models",
            "description": "Sample API request to LocalAi."
          }
        ]
      },
      {
        "name": "agents",
        "description": "Directory containing COGNIC agents.",
        "files": [
          {
            "name": "basher.py",
            "description": "Python script for BASH-specialist LLM agent."
          },
          {
            "name": "prompter.py",
            "description": "Python script for Meta-prompt specialist LLM agent."
          }
        ]
      }
    ]
  }
}

<|EOS|>