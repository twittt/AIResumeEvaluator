# Resume and Job Description Matcher

This project is a full-stack application that allows users to upload a resume and a job description, and then get a match score and evaluation using the OpenAI API. The application leverages a React frontend and a Flask backend.

## Project Capabilities

- **File Upload**: Users can upload resume files in `.doc`, `.docx` or `.pdf` formats, and job description files in `.doc`, `.docx` or `.pdf` formats.
- **Match Score**: The application evaluates how well the resume matches the job description and provides a match score.
- **Evaluation**: The application uses the OpenAI API to provide a detailed evaluation of the match, including suggestions for improving the resume to better fit the job description.

## Technology Stack

- **Frontend**: React
- **Backend**: Flask
- **Database**: SQLite
- **File Processing**: `python-docx` for `.doc` files, `PyPDF2` for `.pdf` files
- **AI Evaluation**: OpenAI API

## Prerequisites

- Node.js and npm (for running the React frontend)
- Python 3.x and pip (for running the Flask backend)
- OpenAI API Key

## Installation

### Backend (Flask)

1. Navigate to the `backend` directory:

    ```bash
    cd backend
    ```

2. Create and activate a virtual environment:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the `backend` directory and add your OpenAI API key:

    ```bash
    OPENAI_API_KEY=your_openai_api_key
    ```

5. Run the Flask application:

    ```bash
    flask run
    ```

### Frontend (React)

1. Navigate to the `frontend` directory:

    ```bash
    cd frontend
    ```

2. Install the required npm packages:

    ```bash
    npm install
    ```

3. Start the React application:

    ```bash
    npm start
    ```

## Running the Application

1. **Start the Flask backend**:

    ```bash
    cd backend
    source venv/bin/activate
    flask run
    ```

2. **Start the React frontend**:

    ```bash
    cd frontend
    npm start
    ```

3. Open your web browser and go to `http://localhost:3000` to access the application.

## File Structure

### Backend

- `app.py`: Main Flask application file.
- `models.py`: SQLAlchemy models for the database.
- `requirements.txt`: List of Python dependencies.
- `uploads/`: Directory to store uploaded files.

### Frontend

- `src/App.js`: Main React application file.
- `public/`: Public assets for the React application.
- `package.json`: List of npm dependencies.

## API Endpoints

### `/upload` (POST)

- **Description**: Upload a resume and a job description, and get a match score and evaluation.
- **Request**: Multipart form data with `resume` and `jobDescription` files.
- **Response**: JSON object with `score` and `suggestions`.

## Example Response

```json
{
  "score": 85.0,
  "suggestions": "Tela Wittig's resume is clearly impressive and highlights a strong history of professional achievements in software engineering and leadership roles. To strengthen the resume further and increase its impact, consider the following suggestions:

Format and Structure:

Add a Space After Name: Ensure there is a space between "PMP" and the rest of the contact information for better readability.
Section Headings: Use clear section headings (e.g., "Executive Summary," "Skills," "Professional Experience," "Education") that are easily distinguishable using bold or a slightly larger font size.
Consistent Bullets: Ensure bullet points are consistently used across the document for all achievements under each role to enhance readability and organization.
Contact Information:

Reverse Order: Place the LinkedIn URL after the email for a more intuitive left-to-right reading flow of essential contacts.
Executive Summary:

Conciseness: Keep it concise by removing less impactful words and emphasizing your unique value proposition and achievements.
Quantifiable Metrics: Further emphasize quantifiable achievements or specific technologies/initiatives to support claims of innovation and impact.
Skills Section:

Reorganization: Group related skills into categories (e.g., Programming Languages, Cloud Platforms, Development Practices) for an easier grasp of capabilities.
Avoid Repetition: "Data Engineering" appears twice; keep only one instance to avoid redundancy.
Prioritization: Place the most critical skills and technologies for the roles you’re targeting towards the start.
Professional Experience:

Verb Consistency: Start each bullet with active verbs for better emphasis and impact.
Impact Metrics: Attempt to include more specific metrics or results, where feasible, to illustrate success or impact beyond the mentioned instances.
Descriptive Details: When stating achievements, try to include more context (like technologies used) around the accomplishment for added clarity.
Avoid Ambiguity: Explain initially unclear terms or acronyms under experience descriptions, like "RFPs," for clarity to non-specialists.
Education:

Placement: Consider moving the education section before professional experience if targeting roles at companies that heavily weigh academic background. Otherwise, it is positioned well.
Details: Adding relevant coursework or projects might also aid in showcasing relevance to technology roles, although this can be optional given current experience levels.
Certifications:

Separate Section: Consider creating a separate section for certifications, especially since being a PMP is a significant credential and may be overlooked if not properly highlighted.
General Suggestions:

Tailoring: Tailor the resume to each specific job application by adding relevant keywords based on job descriptions, ensuring alignment with desired roles.
Proofreading: Ensure the entire document is free from typographical errors and grammatical mistakes.
Implementing these improvements will enhance the clarity, focus, and professional presentation of Tela Wittig’s resume."
}
