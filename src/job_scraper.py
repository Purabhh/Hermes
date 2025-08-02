import requests
import re
from bs4 import BeautifulSoup

class JobScraper:
    def scrape_indeed(self, keywords, location, max_results=10):
        query = "+".join(keywords.split())
        url = f"https://www.indeed.com/jobs?q={query}&l={location}"

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")

            jobs = []
            # Try multiple selectors as Indeed changes their HTML structure
            selectors = [
                "a[data-hide-spinner='true']",
                "h2.jobTitle a",
                "a[data-jk]",
                ".job_seen_beacon a",
                ".jobTitle a"
            ]
            
            for selector in selectors:
                job_links = soup.select(selector)
                if job_links:
                    for link in job_links[:max_results]:
                        title = link.get_text(strip=True)
                        href = link.get("href")
                        if href and title:
                            if href.startswith("/"):
                                full_link = "https://www.indeed.com" + href
                            else:
                                full_link = href
                            jobs.append({
                                "title": title,
                                "link": full_link
                            })
                    break  # If we found jobs with this selector, stop trying others
            
            return jobs
            
        except Exception as e:
            print(f"Error scraping Indeed: {e}")
            return []

    def scrape_github_internships(self):
        # Use the GitHub API to get the README content
        url = "https://api.github.com/repos/SimplifyJobs/Summer2026-Internships/readme"
        
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "Accept": "application/vnd.github.v3+json"
        }
        
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            
            # Decode the base64 content from GitHub API
            import base64
            content = base64.b64decode(response.json()['content']).decode('utf-8')
            
            print(f"Downloaded {len(content)} characters from GitHub API")
            
            jobs = []
            
            # Parse the markdown content to extract job listings
            lines = content.split('\n')
            current_company = None
            
            for line in lines:
                line = line.strip()
                
                # Look for company names (usually in bold **Company** format)
                if line.startswith('| **[') and '](' in line:
                    # Extract company name from markdown link format
                    company_start = line.find('[') + 1
                    company_end = line.find(']')
                    if company_start > 0 and company_end > company_start:
                        current_company = line[company_start:company_end]
                
                # Look for role information in table rows
                elif line.startswith('|') and '|' in line and current_company:
                    parts = line.split('|')
                    if len(parts) >= 4:  # Should have company, role, location, application
                        role = parts[2].strip() if len(parts) > 2 else ""
                        location = parts[3].strip() if len(parts) > 3 else ""
                        
                        if role and role != "Role" and "---" not in role:
                            jobs.append({
                                "company": current_company,
                                "role": role,
                                "location": location
                            })
            
            print(f"Found {len(jobs)} job listings")
            return jobs
            
        except Exception as e:
            print(f"Error scraping GitHub internships: {e}")
            return []
