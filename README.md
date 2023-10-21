# AutoSpotify
🍊Automates Spotify Account Creation and Liking! 🍊 Based on Selenium and Needs Edge Driver.
This is a Python application for generating Spotify accounts using the Selenium web automation framework. It allows you to create multiple Spotify accounts with various options such as Headless mode and limited run count.

## Prerequisites
- Python
- PyQt5
- Selenium
- Faker

## Installation

Make sure you have Python installed. Then, you can install the required libraries using pip:

```bash
pip install PyQt5 selenium faker
```

## Usage

1. Run the application by executing `main.py`.

2. You can configure the following options:
   - **Headless**: Enable or disable headless mode.
   - **Limited Run**: Enable this option and set the run count if you want to generate a limited number of Spotify accounts.
   - **Enter URL for Profile/Playlist**: Enter the URL for the Spotify profile or playlist you want to interact with.

3. Click the "Create Account 🧔" button to start generating Spotify accounts. The application will open a web browser, create accounts, and display the results in the list on the right.

4. You can click the "Like Playlist💖" and "Follow User🍀" buttons to perform actions on the specified Spotify profile or playlist.

## Features
- Creates Spotify accounts with random data using the Faker library.
- Configurable headless mode for account creation.
- Generates accounts with options like name, email, date of birth, and gender.
- Keeps a record of successfully created accounts.
- Ability to like a playlist or follow a user on Spotify.

## Credits

This application is created by Hamza.

## License

This project is licensed under the GPL-3.0 License - see the [LICENSE.md](LICENSE.md) file for details.
