import subprocess
import sys

def chat(prompt, system=None):
  options = system and f"-s {system}" or "-c"
  response = subprocess.check_output(f"llm {options} {prompt}", shell=True, text=True).strip()
  print(f"\n[RESPONSE] {response}\n")
  return response

def main():
  goal = sys.argv[1]
  response = chat(f"GOAL: {goal}\n\nWHAT IS YOUR OVERALL PLAN?")

  while True:
    response = chat("SHELL COMMAND TO EXECUTE OR `DONE`. NO ADDITIONAL CONTEXT OR EXPLANATION:").strip()
    if response == "DONE":
      break

    sleep(3)
    output = subprocess.check_output(response, shell=True, text=True)
    response = chat(f"COMMAND COMPLETED WITH RETURN CODE: {output.returncode}. OUTPUT:\n{output}\n\nWHAT ARE YOUR OBSERVATIONS?")

if __name__ == "__main__":
  main()
