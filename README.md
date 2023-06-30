# crypto-flask (formerly Cryptography-Rest_APIs)

crypto-flask is an open-source project that aims to create REST APIs for various cryptographic algorithms.

## Cloning and Usage

To clone and use this project, make sure you have Python 3.7 installed. Follow these steps:

1. Clone the project repository.
2. Install the required dependencies by running the command `pip install -r requirements.txt`.
3. To run the command line examples, navigate to the respective algorithm folders and execute the test scripts using the command `python -m "file_name"`. Make sure you are in the correct directory.
4. To run the Flask app, navigate to the `flask_app` directory and use the command `python -m run`.

## Project Structure

The project is structured as follows:

### Example

This folder contains command line examples of each implemented algorithm, along with their documentation. The algorithms are further categorized into sub-folders based on their type or functionality.

### flask_app

This folder contains the Flask app, which provides REST APIs for all the algorithms. Use the `run.py` file in this directory to start the Flask app. The routing logic is implemented in the `routing` folder. Each algorithm has its own implementation within this folder, organized into sub-folders.

### misc

This folder contains files that are not directly related to the core project but are required for its functionality. It may include files related to key generation, key storage, and other miscellaneous components.

## Contributing Guidelines

If you wish to contribute to this project, please follow these guidelines:

1. Adhere to coding best practices. Maintain consistency with the existing codebase.
2. When adding a new feature to the Flask app, create a test script first.
3. Use appropriate comments to describe any changes you make to the codebase.

Feel free to contribute to this project and help improve its functionality and usability.