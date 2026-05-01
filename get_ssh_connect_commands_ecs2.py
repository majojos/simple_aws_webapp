#!/home/jordan/.pyenv/shims/python3
import subprocess

KEY_FILE = "from_ubuntu.pem"   # <-- anpassen!
USER = "ec2-user"           # Amazon Linux → ec2-user, Ubuntu → ubuntu

def get_instances():
    cmd = [
        "aws", "ec2", "describe-instances",
        "--filters", "Name=instance-state-name,Values=running",
        "--query", "Reservations[].Instances[].PublicIpAddress",
        "--output", "text"
    ]

    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode != 0:
        print("Fehler beim Abrufen der Instanzen:")
        print(result.stderr)
        return []

    ips = result.stdout.strip().split()

    return ips


def print_ssh_commands(ips):
    if not ips:
        print("Keine laufenden Instanzen gefunden.")
        return

    print("\nSSH Verbindungen:\n")

    for ip in ips:
        print(f"ssh -i {KEY_FILE} {USER}@{ip}")


if __name__ == "__main__":
    ips = get_instances()
    print_ssh_commands(ips)
