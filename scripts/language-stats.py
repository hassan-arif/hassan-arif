import requests
import os
import matplotlib.pyplot as plt

def get_repos(url, headers):
    repos = []
    while url:
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            raise Exception(f"Failed to fetch data: {response.status_code}, {response.text}")
        repos.extend(response.json())
        url = response.links.get('next', {}).get('url')
    return repos

def fetch_all_repos(personal_token, github_token):
    personal_headers = {"Authorization": f"token {personal_token}"}
    github_headers = {"Authorization": f"token {github_token}"}
    
    # Fetch user repos
    user_repos = get_repos("https://api.github.com/user/repos?per_page=100", personal_headers)
    
    # Fetch collaborated repos
    collab_repos = get_repos("https://api.github.com/user/repos?affiliation=collaborator&per_page=100", personal_headers)
    
    # Fetch organization repos
    orgs = get_repos("https://api.github.com/user/orgs", personal_headers)
    org_repos = []
    for org in orgs:
        org_repos.extend(get_repos(f"https://api.github.com/orgs/{org['login']}/repos?per_page=100", github_headers))
    
    return user_repos + collab_repos + org_repos

def analyze_languages(repos):
    languages = {}
    for repo in repos:
        if repo['language']:
            languages[repo['language']] = languages.get(repo['language'], 0) + 1
    return languages

def plot_languages(languages):
    # Sort languages by count in descending order
    sorted_languages = sorted(languages.items(), key=lambda x: x[1], reverse=True)
    
    # Get the top 5 languages and the remaining "Other" category
    top_languages = {k: v for k, v in sorted_languages[:5]}
    other_count = sum(v for k, v in sorted_languages[5:])
    
    # Create labels and sizes for the pie chart
    labels = list(top_languages.keys()) + ['Others']
    sizes = list(top_languages.values()) + [other_count]
    
    # Define colors for the pie chart
    colors = ['#61dafb', '#0055ff', '#00557f', '#55aa00', '#00aaff', '#563d7c']
    
    plt.figure(figsize=(8, 6), facecolor='black')
    plt.subplots_adjust(right=0.6)

    plt.pie(sizes, labels=None, colors=colors, shadow=True, startangle=140) # autopct='%1.1f%%'
    plt.title('Most Used Languages', fontweight='bold', color='#64dafb')

    total_count = sum(sizes)
    percentages = [(s / total_count) * 100 if l != 'Others' else (other_count / total_count) * 100 for l, s in zip(labels, sizes)]
    labels = [f'{l}, {p:0.1f}%' for l, p in zip(labels, percentages)]
    plt.legend(fontsize='large', labels=labels, loc='upper left', bbox_to_anchor=(1.02, 1), labelcolor='white', facecolor='#20232a', edgecolor='white')

    plt.axis('equal')
    plt.savefig('assets/language-stats.png', facecolor='#20232a')

def main():
    personal_token = os.getenv("PERSONAL_ACCESS_TOKEN")
    github_token = os.getenv("GITHUB_TOKEN")
    
    if not personal_token or not github_token:
        raise Exception("Both PERSONAL_ACCESS_TOKEN and GITHUB_TOKEN environment variables must be set")
    
    all_repos = fetch_all_repos(personal_token, github_token)
    
    languages = analyze_languages(all_repos)
    plot_languages(languages)

if __name__ == "__main__":
    main()