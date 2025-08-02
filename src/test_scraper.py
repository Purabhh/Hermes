from job_scraper import JobScraper

print("=== GitHub Internships Scraper Test ===")
scraper = JobScraper()

print("\nScraping Summer 2026 internships from GitHub...")
try:
    results = scraper.scrape_github_internships()
    print(f"\nFound {len(results)} internship opportunities!")
    
    if results:
        print("\nFirst 10 internships:")
        for i, job in enumerate(results[:10], 1):
            print(f"{i}. {job['company']} - {job['role']}")
            print(f"   Location: {job['location']}")
            print()
        
        if len(results) > 10:
            print(f"... and {len(results) - 10} more internships available!")
    else:
        print("No internships found")
        
except Exception as e:
    print(f"Error occurred: {e}")
    import traceback
    traceback.print_exc()

print("\n=== Test Complete ===")
