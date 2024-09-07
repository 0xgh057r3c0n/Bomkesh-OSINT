import requests
from googlesearch import search
from bs4 import BeautifulSoup
import re
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

# Banner and version info
def show_banner():
    banner = """                         
                         `:oDFo:`                            
                       ./ymM0dayMmy/.                          
                    -+dHJ5aGFyZGVyIQ==+-                    
                `:sm⏣~~Destroy.No.Data~~s:`                
             -+h2~~Maintain.No.Persistence~~h+-              
         `:odNo2~~Above.All.Else.Do.No.Harm~~Ndo:`          
      ./etc/shadow.0days-Data'%20OR%201=1--.No.0MN8'/.      
   -++SecKCoin++e.AMd`       `.-://///+hbove.913.ElsMNh+-    
  -~/.ssh/id_rsa.Des-                  `htN01UserWroteMe!-  
  :dopeAW.No<nano>o                     :is:TЯiKC.sudo-.A:  
  :we're.all.alike'`                     The.PFYroy.No.D7:  
  :PLACEDRINKHERE!:                      yxp_cmdshell.Ab0:    
  :msf>exploit -j.                       :Ns.BOB&ALICEes7:    
  :---srwxrwx:-.`                        `MS146.52.No.Per:    
  :<script>.Ac816/                        sENbove3101.404:    
  :NT_AUTHORITY.Do                        `T:/shSYSTEM-.N:    
  :09.14.2011.raid                       /STFU|wall.No.Pr:    
  :hevnsntSurb025N.                      dNVRGOING2GIVUUP:    
  :#OUTHOUSE-  -s:                       /corykennedyData:    
  :$nmap -oS                              SSo.6178306Ence:    
  :Awsm.da:                            /shMTl#beats3o.No.:    
  :Ring0:                             `dDestRoyREXKC3ta/M:    
  :23d:                               sSETEC.ASTRONOMYist:    
   /-                        /yo-    .ence.N:(){ :|: & };:    
                             `:Shall.We.Play.A.Game?tron/    
                             ```-ooy.if1ghtf0r+ehUser5`    
                           ..th3.H1V3.U2VjRFNN.jMh+.`          
                          `MjM~~WE.ARE.se~~MMjMs              
                           +~KANSAS.CITY's~-`                  
                            J~HAKCERS~./.`                    
                            .esc:wq!:`                        
                             +++ATH`                                                           `
.---.                .-.               .-.   
: .; :               : :.-.            : :   
:   .' .--. ,-.,-.,-.: `'.' .--.  .--. : `-. 
: .; :' .; :: ,. ,. :: . `.' '_.'`._-.': .. :
:___.'`.__.':_;:_;:_;:_;:_;`.__.'`.__.':_;:_;                                                                                                                                                        
Version: 1.0
Author: G4UR4V007
Inspired by: Satyaneshi Bomkesh Bakshi
Description: A tool for uncovering social media profiles and performing reverse email lookups for news and legal charges against him, inspired by the astute detective Bomkesh Bakshi
    """
    print(Fore.CYAN + banner)

# Regex patterns for phone number and email extraction
phone_pattern = re.compile(r'\+?\d[\d\-\(\) ]{9,}\d')
email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')

# Function to extract phone numbers and emails from a block of text
def extract_contacts(text):
    phones = re.findall(phone_pattern, text)
    emails = re.findall(email_pattern, text)
    return phones, emails

# Function to search username on Twitter
def search_twitter(username):
    url = f"https://twitter.com/{username}"
    response = requests.get(url)
    if response.status_code == 200:
        return f"Found Twitter Profile: {url}"
    else:
        return f"Twitter profile for {username} not found."

# Function to search username on Facebook
def search_facebook(username):
    url = f"https://www.facebook.com/{username}"
    response = requests.get(url)
    if response.status_code == 200:
        return f"Found Facebook Profile: {url}"
    else:
        return f"Facebook profile for {username} not found."

# Function to search username on Instagram
def search_instagram(username):
    url = f"https://www.instagram.com/{username}/"
    response = requests.get(url)
    if response.status_code == 200:
        return f"Found Instagram Profile: {url}"
    else:
        return f"Instagram profile for {username} not found."

# Function to search username on LinkedIn
def search_linkedin(username):
    url = f"https://www.linkedin.com/in/{username}"
    response = requests.get(url)
    if response.status_code == 200:
        return f"Found LinkedIn Profile: {url}"
    else:
        return f"LinkedIn profile for {username} not found."

# Function to reverse search a name on Google
def reverse_google_search(name):
    search_results = []
    query = f"{name} email phone"
    try:
        for result in search(query):
            search_results.append(result)
            if len(search_results) >= 5:
                break
    except Exception as e:
        return f"Error during Google search: {str(e)}"
    
    return search_results

# Function to reverse search for legal documents on Indian Kanoon via Google
def search_indian_kanoon_via_google(name):
    search_results = []
    query = f"{name} Indian Kanoon"
    try:
        for result in search(query):
            search_results.append(result)
            if len(search_results) >= 5:
                break
    except Exception as e:
        return f"Error during Google search for Indian Kanoon: {str(e)}"
    
    return search_results

# Function to reverse search an email on Google
def reverse_search_email(email):
    email_results = []
    query = f"{email} facebook"
    try:
        for result in search(query):
            email_results.append(result)
            if len(email_results) >= 5:
                break
    except Exception as e:
        return f"Error during email reverse search: {str(e)}"
    
    return email_results

# Function to search for news articles related to a person
def search_news(name):
    news_results = []
    query = f"{name} news"
    try:
        for result in search(query):
            news_results.append(result)
            if len(news_results) >= 5:
                break
    except Exception as e:
        return f"Error during Google search: {str(e)}"
    
    return news_results

# Print results with color
def print_result(platform, result):
    if "not found" in result:
        print(Fore.RED + f"{platform}: {result}")
    else:
        print(Fore.GREEN + f"{platform}: {result}")

# Main Function to run the tool
def run_tool():
    show_banner()
    username = input(Fore.YELLOW + "Enter the username you want to search: ")

    print("\n" + Fore.CYAN + "--- Searching Social Media Profiles ---")
    twitter_profile = search_twitter(username)
    print_result("Twitter", twitter_profile)
    
    facebook_profile = search_facebook(username)
    print_result("Facebook", facebook_profile)

    instagram_profile = search_instagram(username)
    print_result("Instagram", instagram_profile)
    
    linkedin_profile = search_linkedin(username)
    print_result("LinkedIn", linkedin_profile)

    # Attempt to extract name (for demo, just using the username)
    person_name = username

    print("\n" + Fore.CYAN + "--- Reverse Google Search for Email/Phone ---")
    google_results = reverse_google_search(person_name)
    if isinstance(google_results, str):
        print(Fore.RED + google_results)  # In case of an error
    else:
        print(Fore.GREEN + "Top Google Search Results:")
        combined_text = ""
        for result in google_results:
            print(Fore.YELLOW + result)
            try:
                response = requests.get(result)
                soup = BeautifulSoup(response.content, 'html.parser')
                combined_text += soup.get_text()  # Combine text from all pages
            except Exception as e:
                print(Fore.RED + f"Error fetching the page: {str(e)}")

    # Manual input for email reverse search
    print("\n" + Fore.CYAN + "--- Reverse Search for Emails ---")
    print(Fore.YELLOW + "Enter emails to reverse search (separated by commas):")
    user_emails = input(Fore.YELLOW + "Emails: ").split(',')
    user_emails = [email.strip() for email in user_emails]

    email_search_results = {}
    for email in user_emails:
        if email:  # Check if email is not empty
            print(Fore.YELLOW + f"\nReverse Searching Email: {email}")
            email_results = reverse_search_email(email)
            if isinstance(email_results, str):
                print(Fore.RED + email_results)  # Error message
            else:
                email_search_results[email] = email_results

    # Display reverse search results for manually entered emails
    print("\n" + Fore.CYAN + "--- Reverse Search Results for Emails ---")
    for email, results in email_search_results.items():
        print(Fore.GREEN + f"\nResults for {email}:")
        for result in results:
            print(Fore.YELLOW + result)

    print("\n" + Fore.CYAN + "--- Searching Indian Kanoon via Google ---")
    indian_kanoon_results = search_indian_kanoon_via_google(person_name)
    if isinstance(indian_kanoon_results, str):
        print(Fore.RED + indian_kanoon_results)  # In case of an error
    else:
        print(Fore.GREEN + "Indian Kanoon Related Results:")
        for result in indian_kanoon_results:
            print(Fore.YELLOW + result)

    print("\n" + Fore.CYAN + "--- Searching for News Articles ---")
    news_articles = search_news(person_name)
    if isinstance(news_articles, str):
        print(Fore.RED + news_articles)  # In case of an error
    else:
        print(Fore.GREEN + "Top News Articles:")
        for article in news_articles:
            print(Fore.YELLOW + article)

# Run the tool
if __name__ == "__main__":
    run_tool()
