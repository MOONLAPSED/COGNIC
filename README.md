<|SOS|><system>

/* Co-cognition framework for IT/CS/AI learners; LLM-integration and utility - POSIX integration, unix file system, stdio, python & bash (xonsh) */

# COGNIC - LLM Cognition Platform v0.9
#### "Why has the entire landscape of cognition changed because of a new information technology?"

How is it that the domain of computer science has suddenly claimed a kind of superiority in the annals of thought, production & industry, academia, and the realm of neuroscience? What revolution remains in our historically-bounded conquest of dimensionality, which began in earnest in the 16th century with Isaac Newton or perhaps with some of his contemporaries like Nicolaus Copernicus or one of histories prohphets? What could this technology possibly have erected across the great gulch between our understanding of the world and the hardest problem of all; consciousness? It confronts the very essence of its own demiurge, akin to the enigmatic "hard problem of evil," that being cognition—a puzzle that has perplexed humanity for ages.

I'm sure that you already know the answer to these rhetorical questions; perhaps even to your own consternation, as news of it saturates the airwaves and the consciousness of a globe-spanning species with impossibly-rich networks and interconnections. Large Language Models (LLM herein) and the eponymous ChatGPT are indeed the topic and the star of this show.

 - LLM and the application of NLP are the most significant advancements towards AI in our lifetimes.
 - LLM is the 'transistor-moment' for the next generation of software.
 - The next generation of software, with LLM as a core element, will shatter the UI paradigm of the early 21st century and the UX rooted in the beginnings of computer science. It will even shed the trappings of academia and industry jargonification, as well as the veritable historiography of relevant texts and the countless minutiae of software design architecture.
 - Already, we are dealing with a Turing-complete and highly-capable new 'scripting language' that is functionally a superset of BASH, Python, JavaScript, and all the rest. This language is accessible to anyone with a smartphone, but the advancements have only just begun.

#### Installation
COGNIC, will serve as an on-going research proof of these adumbrations as far as the public is conscerned. This codebase is experimental and not ready for end users. Only an expert should attempt to use any of this code because I am, at best, a Sophomore programmer and the code featured in this repo is not safely implimented.

#### Roadmap
 - client & server apps
   - Server handles computation & resources, hosts filesystem, COGNICs integration point into other LLM software and workflows like LogSeq, Firefox, AGiXT, LocalAI, Chainlit, Manifest, Wandb, LocalGPT, Textgen-webui, and GPT4ALL.
   - User interacts with the client; a browser-based fancy markdown editor and server interface. Client represents the #LogSeq portion of COGNIC's database functionality - serving also as a 'control' for COGNIC's growing server-side (AI-facing) databases. User handles the LogSeq integration themselves with copy & paste for now.
 - Server integration with other AI applications
   - xonsh scripts spin up docker containers for 'services'
 - Reverse engineer apis 


#### Summary
In as few words as possible this project is a framework for extending my Zettelkasten LogSeq knowledge base and cultivating an organized 'second-brain.' COGNIC is the shared file-system for co-cognition between a primary learner(me) and any number of machine learning algorithms, language models, neural nets, etc. whilst handling additional training (on-top of the large foundation models) and logging in the simplest possible text:text RLHF personalized training knowledge bases (kb). Agnosticism is a guiding principle in these exuberant and rapidly changing times. Good design is potable design. Agility and good data practices are all that matter.


#### Map of the project files

.

..

~/main
  
	./cognic.py
	
	├── chat_manipulation.py 
	
	├── client_application.py
	
	├── docker_configuration.py
	
	├── filesystem_access.py
	
	├── llama_model.py
	
	├── server_administration.py
	
	├── stdio_tasks.py
	
	├── threading_core_utils.py
	
	├── unix_functionality.py
	
	├── virtualized_access.py
	
	├── web_application.py
	
	├── xonsh_extension.py
	
	└── main.py
  
  ~/agents
	
 	├── basher.py
     		 	
  	└── prompter.py

</s><|EOS|>