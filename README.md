# PulseDash: Real-time System Metrics Dashboard

## Project Overview

PulseDash is a web-based dashboard designed to display real-time system health and performance metrics such as CPU usage, memory usage, and disk space utilisation. This project combines a Python backend with a simple HTML and JavaScript frontend, providing a lightweight yet powerful tool for monitoring system metrics. Users can access up-to-date information from any device with internet access, making it easier to keep an eye on system health and performance. This setup allows users to monitor their systems' health from anywhere, as long as they have internet access.

### Key Features

- **Real-time Updates**: System metrics are updated on the web dashboard every 5 seconds.
- **Lightweight Design**: Utilises Flask for the backend and Vanilla JavaScript for the frontend, ensuring fast load times and responsiveness.
- **Easy Setup**: With minimal dependencies, PulseDash can be set up quickly and run on most systems with Python.

## Getting Started

### Prerequisites

Before you begin, ensure you have the following installed on your system:
- Python 3.6 or later
- pip (Python package installer)

### Installation

1. **Clone the Repository**

   Start by cloning the repository to your local machine:

   ```sh
   git clone https://github.com/<your-username>/PulseDash.git
   cd PulseDash
   ```

2. **Install Required Python Packages**

   Install Flask and psutil using pip:

   ```sh
   pip install Flask psutil
   ```

   > **Note**: It's recommended to use a virtual environment for Python projects to avoid conflicts between packages. You can create a virtual environment using `python -m venv venv` and activate it with `source venv/bin/activate` (Unix) or `.env\Scriptsctivate` (Windows).

### Running PulseDash

1. **Start the Backend Server**

   Navigate to the project directory and run:

   ```sh
   export FLASK_APP="metrics_collector.py"  # Use `set` instead of `export` on Windows
   flask run
   ```

   This starts the Flask development server, making the dashboard accessible on `http://127.0.0.1:5000`.

2. **Access the Dashboard**

   Open a web browser and go to `http://127.0.0.1:5000` to view the dashboard. The system metrics should update approximately every 5 seconds.

## Project Structure

- `metrics_collector.py`: The Flask application responsible for collecting system metrics and serving the web dashboard.
- `templates/index.html`: The frontend HTML file with embedded JavaScript for displaying the system metrics.

## Automation and Deployment

It is recommended to write a Dockerfile to containerise the application, ensuring it can be easily set up and run anywhere Docker is supported. Include a `docker-compose.yml` for easy setup and teardown. This step will ensure that your application can be easily set up and run in any environment that supports Docker. Please note that I have not created a Dockerfile for this project. 

## Contributions

Contributions to PulseDash are welcome! Please feel free to report any issues or suggest enhancements through the GitHub issue tracker. It also provides a foundation that can be easily extended or modified as needed, with clear paths for adding more sophisticated features or scaling up in the future.

## Disclaimer

PulseDash is intended for educational and monitoring purposes only and should not be used as a replacement for professional system monitoring tools, especially in production environments.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
