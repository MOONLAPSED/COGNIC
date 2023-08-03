# instructions:
### use git bash or msys2 or similar if on windows
/* put your model in the models folder, note its name eg. orca-mini-7b.ggmlv3.q4_0.bin eg... */

  cp ~/your_model.bin ~/LocalAI/models/your_model.bin

cd LocalAI

python3 -m pip install -r requirements.txt

cd modules

vi localai.py

><modify the model name to your model name>

cd ..

Docker-compose up -d --pull always

curl http://localhost:8080/v1/models

><your model>

curl http://localhost:8080/v1/completions -H "Content-Type: application/json" -d '{"model": "orca-mini-7b.ggmlv3.q4_0.bin","prompt": "A long time ago in a galaxy far, far away",
"temperature": 0.7}'

><something about jedi>

localai.py initialized, model: orca-mini-7b.ggmlv3.q4_0.bin

drop-in replacement for gpt-3.5 api (https://beta.openai.com/docs/api-reference/completions/create) >>> https://localai.io/basics/getting_started/index.html

