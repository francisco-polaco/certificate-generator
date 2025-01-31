# Certificate Generator

This project allows you to generate certificates using a PowerPoint (`.pptx`) template. By leveraging Python, it automates the creation of personalized certificates based on a provided template and configuration.

## Features

- Generate certificates from a `.pptx` template.
- Customize certificate content through configuration files.
- Batch processing for multiple certificates.

## Requirements

- Python 3.x
- Required Python packages (listed in `requirements.txt`)

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/francisco-polaco/certificate-generator.git
   cd certificate-generator
   ```

2. **Install Dependencies:**

   It's recommended to use a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use venv\Scripts\activate
   ```

   Then, install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Prepare Your Template:**

   - Create a PowerPoint (`.pptx`) file that serves as your certificate template.
   - Use placeholders (e.g., `{name}`, `{date}`) in the template where dynamic content should appear.

2. **Configure the Application:**

   - Edit the `config.yml` file to specify the template path, output directory, and any other configurations.
   - Ensure that your data source (e.g., a XLSX file with participant names) is correctly referenced in the configuration.

3. **Generate Certificates:**

   Run the main script:

   ```bash
   python main.py
   ```

   The generated certificates will be saved in the specified output directory.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to enhance the functionality or fix bugs.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

*Note: This README provides a general overview. For detailed instructions and advanced configurations, please refer to the project's documentation or source code comments.** 

