# EventConnect

EventConnect 2025

## Overview

EventConnect is a web application designed to manage and explore events. It leverages Streamlit for the frontend, Google Cloud Firestore for the database, and Qdrant for vector search capabilities. The application allows users to register, log in, and interact with events by liking or disliking them. Admin users can add new events with descriptions, images, and dates.

## Features

- **User Authentication**: Secure user registration and login using `streamlit_authenticator`.
- **Event Management**: Admin users can add new events with descriptions, images, and dates.
- **Event Recommendations**: Users receive event recommendations based on their likes and dislikes.
- **Database Integration**: Uses Google Cloud Firestore to store user data and event information.
- **Vector Search**: Utilizes Qdrant for efficient vector search and recommendations.

## Installation

1. **Clone the repository**:

   ```sh
   git clone https://github.com/reddragonnm/shipathon.git
   cd eventconnect
   ```

2. **Set up the development container**:
   Ensure you have Docker installed and running. The project uses a dev container for a consistent development environment.

3. **Install dependencies**:

   ```sh
   pip install -r requirements.txt
   ```

4. **Set up Streamlit secrets**:
   Create a `secrets.toml` file with your API keys and Firebase credentials.

5. **Run the application**:
   ```sh
   streamlit run Explore.py
   ```

## Configuration

The application uses a [`config.yaml`](config.yaml) file for user credentials and roles. Update this file to manage users and their permissions.

## Test Admin User

For testing purposes, there is a pre-configured admin user with the following credentials:

- **Username**: admin
- **Password**: admin

This admin user can be used to log in and access admin functionalities such as adding new events. You can update the credentials in the [`config.yaml`](config.yaml) file if needed.

## Usage

- **Register a new user**: Navigate to the "Register User" page and fill in the required details.
- **Add a new event**: Admin users can navigate to the "Add new event" page to create a new event.
- **Explore events**: Users can explore and interact with events on the main page.

## File Structure

.
├── .devcontainer/
│ └── devcontainer.json
├── .streamlit/
│ └── secrets.toml
├── pages/
│ ├── 1_New_Event.py
│ └── 2_Register_User.py
├── **pycache**/
├── clubs.json
├── config.yaml
├── db.py
├── Explore.py
├── LICENSE
├── README.md
├── requirements.txt
└── user.py

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes or improvements.

## Contact

For any questions or inquiries, please contact the project maintainer at hello@gmail.com.
