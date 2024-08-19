
# Domain Availability Checker

This project is a Python script that checks the availability of domain names using Selenium and ChromeDriver. The script reads a list of Top-Level Domains (TLDs) from a file (`tlds.txt`), checks if the domain `rul.[tld]` is available on Niagahoster, and writes the results to text files (`available_tlds.txt` for available domains and `not_available_tlds.txt` for unavailable domains).

## Requirements

- Docker
- Docker Compose

### Python Dependencies

The following Python packages are required:

- `selenium`
- `chromedriver-autoinstaller`

These dependencies are automatically installed when using Docker.

## Project Structure

```plaintext
├── .gitignore
├── Dockerfile
├── available_tlds.txt
├── cek_domain.py
├── docker-compose.yml
├── not_available_tlds.txt
├── requirements.txt
└── tlds.txt
```

- `Dockerfile`: Defines the Docker image configuration for running the script.
- `docker-compose.yml`: Used to build and run the Docker container.
- `cek_domain.py`: The main Python script that checks domain availability.
- `tlds.txt`: A list of TLDs to check.
- `available_tlds.txt`: Output file containing the domains that are available.
- `not_available_tlds.txt`: Output file containing the domains that are not available.
- `requirements.txt`: List of Python dependencies.

## How to Run

### 1. Using Docker

1. **Build and Run the Container:**

   ```bash
   docker compose up --build
   ```

2. **View the Results:**

   - `available_tlds.txt`: Contains the list of available domains.
   - `not_available_tlds.txt`: Contains the list of unavailable domains.

### 2. Running Locally (Without Docker)

1. **Install Python dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

2. **Run the script:**

   ```bash
   python cek_domain.py
   ```

3. **View the Results:**

   - `available_tlds.txt`: Contains the list of available domains.
   - `not_available_tlds.txt`: Contains the list of unavailable domains.

## Notes

- Ensure you have Docker and Docker Compose installed on your system.
- The script uses Selenium with ChromeDriver in headless mode to automate the browser for checking domain availability.
- The script may need adjustments if Niagahoster's website structure changes.

## Troubleshooting

- **Docker Compose command not found:** Ensure Docker Compose is installed and accessible in your command line.
- **ChromeDriver issues:** Ensure that ChromeDriver is installed correctly and that it matches the version of Chrome installed in the Docker container.
- **Permissions issues:** Use the `--no-sandbox` and `--disable-dev-shm-usage` options in headless mode to avoid permission issues in certain environments.
