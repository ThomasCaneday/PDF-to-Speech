# PDF to Speech

A simple Python program to convert a PDF document to speech using PyPDF2 and gTTS.

## Features

- Extract text from a PDF file.
- Convert the extracted text to speech.
- Save the speech as an MP3 file.
- Automatically open the generated MP3 file.

## Requirements

- Python 3.x

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/ThomasCaneday/pdf-to-speech.git
    cd pdf-to-speech
    ```

2. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Ensure you have a PDF file you want to convert to speech.
2. Update the `pdf_file` variable in the script with the path to your PDF file:
    ```python
    pdf_file = 'path/to/your/file.pdf'
    mp3_file = 'audio.mp3'
    ```
3. Run the script:
    ```sh
    python pdf_to_speech.py
    ```

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. **Fork the repository**: Click the "Fork" button at the top right corner of this repository to create your own copy of the project.

2. **Clone the repository**: Clone your forked repository to your local machine using:
    ```sh
    git clone https://github.com/ThomasCaneday/pdf-to-speech.git
    cd pdf-to-speech
    ```

3. **Create a new branch**: Create a new branch for your feature or bug fix:
    ```sh
    git checkout -b feature-or-bugfix-name
    ```

4. **Make your changes**: Make your changes to the codebase. Ensure that your code follows the project's coding standards and includes necessary tests.

5. **Commit your changes**: Commit your changes with a clear and descriptive commit message:
    ```sh
    git add .
    git commit -m "Description of your changes"
    ```

6. **Push your changes**: Push your changes to your forked repository:
    ```sh
    git push origin feature-or-bugfix-name
    ```

7. **Create a pull request**: Go to the original repository on GitHub and create a pull request from your forked repository. Provide a clear description of your changes and the problem they solve.

8. **Review process**: Your pull request will be reviewed by the maintainers. Be prepared to make any necessary changes during the review process.

9. **Merge**: Once your pull request is approved, it will be merged into the main branch of the project.

Thank you for your contributions!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
