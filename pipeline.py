import subprocess


pipeline_steps = [
    "main.py",
    "db-conn.py",
    "put_data.py",
]


for step in pipeline_steps:
    try:
        subprocess.run(["python", step], check=True)
        print(f"Step {step} completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Step {step} failed with error: {e}")



