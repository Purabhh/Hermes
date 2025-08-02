# Hermes Job Search AI Agent - Complete Setup Guide

## Project Overview

Building an AI agent that automatically:

1. **Finds newest jobs** from job boards
2. **Writes personalized cover letters** using AI
3. **Finds recruiter LinkedIn emails**
4. **Writes and sends emails** to recruiters

## System Architecture

### Core Components

```
Hermes/
├── job_scraper.py      # Scrapes job boards (Indeed, LinkedIn, etc.)
├── cover_letter_gen.py # AI-powered cover letter generation
├── email_finder.py     # Finds recruiter emails from LinkedIn
├── email_sender.py     # Sends emails to recruiters
├── main_agent.py       # Orchestrates the entire process
├── config.py          # Configuration and settings
└── database.py        # Tracks applications and metrics
```

## Step 1: Install Ollama & Setup

### Install Ollamano 

```bash
# Already installed via winget
# Start Ollama service
ollama serve
```

### Pull Models

```bash
# For general AI tasks (cover letters, emails)
ollama pull llama2

# For coding tasks (web scraping, automation)
ollama pull codellama

# For smaller, faster processing
ollama pull mistral
```

## Step 2: Job Scraping Module

### Job Sources to Scrape

- **Indeed.com** - Largest job board
- **LinkedIn Jobs** - Professional networking
- **Glassdoor** - Company reviews + jobs
- **AngelList** - Startup jobs
- **Remote.co** - Remote positions

### Scraping Strategy

```python
# Example job scraper structure
class JobScraper:
    def scrape_indeed(self, keywords, location):
        # Scrape Indeed for newest jobs
        pass

    def scrape_linkedin(self, keywords, location):
        # Scrape LinkedIn Jobs
        pass

    def filter_jobs(self, jobs, criteria):
        # Filter by salary, experience, company size
        pass
```

## Step 3: AI Cover Letter Generator

### Using Ollama with LangChain

```python
from langchain_community.llms import Ollama
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

# Initialize Ollama
llm = Ollama(model="llama2")

# Cover letter prompt template
cover_letter_prompt = PromptTemplate(
    input_variables=["job_title", "company", "job_description", "resume_summary"],
    template="""
    Write a compelling cover letter for a {job_title} position at {company}.

    Job Description: {job_description}

    My Background: {resume_summary}

    Make it personalized, professional, and highlight relevant experience.
    """
)

cover_letter_chain = LLMChain(llm=llm, prompt=cover_letter_prompt)
```

## Step 4: LinkedIn Email Finder

### Finding Recruiter Emails

```python
class LinkedInEmailFinder:
    def find_company_recruiters(self, company_name):
        # Search LinkedIn for company recruiters
        pass

    def extract_email_patterns(self, company_domain):
        # Common email patterns: first.last@company.com
        pass

    def verify_email(self, email):
        # Verify email exists
        pass
```

## Step 5: Email Automation

### Email Sender Module

```python
class EmailSender:
    def send_application_email(self, recruiter_email, cover_letter, resume):
        # Send personalized application email
        pass

    def follow_up_email(self, recruiter_email, days_later=7):
        # Send follow-up email
        pass
```

## Step 6: Main AI Agent

### Orchestration Agent

```python
class HermesJobAgent:
    def __init__(self):
        self.scraper = JobScraper()
        self.cover_letter_gen = CoverLetterGenerator()
        self.email_finder = LinkedInEmailFinder()
        self.email_sender = EmailSender()

    def run_daily_job_search(self):
        # 1. Find new jobs
        jobs = self.scraper.find_new_jobs()

        # 2. For each job, generate cover letter
        for job in jobs:
            cover_letter = self.cover_letter_gen.generate(job)

            # 3. Find recruiter email
            recruiter_email = self.email_finder.find_email(job.company)

            # 4. Send application email
            if recruiter_email:
                self.email_sender.send_application(job, cover_letter, recruiter_email)
```

## Configuration

### Environment Variables

```bash
# Email Configuration
GMAIL_ADDRESS=your_email@gmail.com
GMAIL_APP_PASSWORD=your_app_password

# LinkedIn Configuration (optional)
LINKEDIN_EMAIL=your_linkedin_email
LINKEDIN_PASSWORD=your_linkedin_password

# Job Search Settings
SEARCH_KEYWORDS="software engineer,python developer,full stack"
LOCATION="San Francisco, CA"
SALARY_MIN=80000
REMOTE_ONLY=false

# AI Settings
OLLAMA_MODEL=llama2
MAX_APPLICATIONS_PER_DAY=10
```

## Usage Examples

### Basic Usage

```python
from hermes_agent import HermesJobAgent

# Initialize the agent
agent = HermesJobAgent()

# Run daily job search and applications
agent.run_daily_job_search()

# Manual job application
agent.apply_to_job("Software Engineer", "Google", job_url="...")
```

### Advanced Usage

```python
# Custom job search
jobs = agent.search_jobs(
    keywords=["machine learning", "AI engineer"],
    location="New York",
    remote_only=True,
    salary_min=120000
)

# Generate cover letter for specific job
cover_letter = agent.generate_cover_letter(job_description, my_resume)

# Find and contact recruiter
recruiter_email = agent.find_recruiter_email("Microsoft")
agent.send_application_email(recruiter_email, cover_letter, resume)
```

## Advantages of This Approach

- ✅ **Fully Automated** - Runs daily without manual intervention
- ✅ **AI-Powered** - Personalized cover letters and emails
- ✅ **Comprehensive** - Covers entire application process
- ✅ **Scalable** - Can apply to hundreds of jobs
- ✅ **Trackable** - Database tracks all applications
- ✅ **Free** - Uses Ollama instead of paid APIs

## Next Steps

1. **Install dependencies** - `pip install -r requirements.txt`
2. **Start Ollama** - `ollama serve`
3. **Pull model** - `ollama pull llama2`
4. **Configure email** - Set up Gmail app password
5. **Build modules** - Start with job scraper
6. **Test integration** - Run end-to-end test

## Ethical Considerations

- ✅ Respect rate limits on job boards
- ✅ Don't spam recruiters
- ✅ Personalize each application
- ✅ Follow up appropriately
- ✅ Be transparent about automation
