import subprocess
import time

# Customize paths & container name
input_path = r"C:\Users\umadevi\OneDrive\Desktop\pdf_extractor\input"
output_path = r"C:\Users\umadevi\OneDrive\Desktop\pdf_extractor\output"
container_name = "pdf_extractor:001"

docker_cmd = [
    "docker", "run", "--rm",
    "-v", f"{input_path}:/app/input",
    "-v", f"{output_path}:/app/output",
    "--network", "none",
    container_name
]

print("🚀 Running PDF extractor…")
start_time = time.time()

result = subprocess.run(docker_cmd, capture_output=True, text=True)

end_time = time.time()
elapsed = end_time - start_time

print("✅ Docker run finished.")
print(f"🕒 Elapsed time: {elapsed:.2f} seconds")

if result.stdout:
    print("--- stdout ---")
    print(result.stdout)
if result.stderr:
    print("--- stderr ---")
    print(result.stderr)
