# AI Resume Builder

In this project, an AI-powered resume builder system is designed and implemented to help users enter their personal information, education, and work experience to automatically generate a professional resume.

## Features

- **User Input Section**: 
  - Collect personal information (name, contact number, email, address)
  - Collect education details (university, field of study, graduation year)
  - Collect work experience (job title, company, start and end date, job description)
  - Collect skills and certifications
  - Ability to save entered information for future use

- **Resume Generation and Storage**:
  - Use ReportLab or WeasyPrint libraries to generate resumes in PDF and Word formats
  - Provide at least three ready-to-use templates dynamically filled with user input
  - Allow users to choose their preferred template
  - Store generated resume files and maintain their addresses in MySQL, SQLite, or PostgreSQL database

- **Data Validation**:
  - Validate email format
  - Validate dates (like birth date and work experience dates)
  - Prevent incomplete data entry

- **Advanced Features**:
  - Improve writing and grammar using tools like LanguageTool or TextBlob

## Recommended Technologies

- **User Interface**: PyQt
- **Server and APIs**: FastAPI
- **Database**: MySQL, PostgreSQL, SQLite
- **File Generation**: WeasyPrint, ReportLab

## Installation and Setup

To install and set up the project, follow these steps:

1. Clone or download the source code from the GitHub repository.
2. Install the project dependencies.
3. Set up the database and perform necessary migrations.
4. Run the application:

## Usage

1. Run the application.
2. Enter your information in the respective forms.
3. Choose your desired template.
4. Download and save the generated resume.

## Contribution

Your suggestions and feedback are highly valuable for improving this project. Feel free to collaborate with us by creating issues or pull requests in the GitHub repository.

## License

This project is licensed under the MIT License. For more details, refer to the [LICENSE](./LICENSE) file.
