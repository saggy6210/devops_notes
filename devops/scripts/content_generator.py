"""
DevOps Learning Hub - Daily Content Generator

Uses Google Gemini to generate daily DevOps learning content.
Automatically determines the next topic based on existing content.
"""

import os
import re
import sys
import time
from datetime import datetime
from pathlib import Path

try:
    import google.generativeai as genai
except ImportError:
    print("❌ Please install google-generativeai: pip install google-generativeai")
    sys.exit(1)


# Topic curriculum - ordered list of topics with subtopics
CURRICULUM = {
    "docker": [
        "Core Concepts",
        "Networking",
        "Volumes and Storage",
        "Dockerfile Best Practices",
        "Multi-stage Builds",
        "Docker Compose",
        "Security Best Practices",
        "Logging and Debugging",
        "Docker in Production",
        "Docker Interview Deep Dive"
    ],
    "kubernetes": [
        "K8s Architecture",
        "Pods and ReplicaSets",
        "Deployments",
        "Services",
        "ConfigMaps and Secrets",
        "Storage PV and PVC",
        "Networking",
        "Ingress Controllers",
        "RBAC Security",
        "Helm Package Manager",
        "Operators",
        "Troubleshooting",
        "Production Best Practices",
        "Managed K8s EKS AKS GKE",
        "K8s Interview Deep Dive"
    ],
    "terraform": [
        "Introduction to IaC",
        "HCL Syntax and Basics",
        "Providers and Resources",
        "Variables and Outputs",
        "State Management",
        "Modules",
        "Workspaces",
        "Backend Configuration",
        "Best Practices",
        "Terraform Interview Deep Dive"
    ],
    "ansible": [
        "Introduction and Architecture",
        "Inventory Management",
        "Ad-hoc Commands",
        "Playbooks Basics",
        "Variables and Facts",
        "Templates Jinja2",
        "Roles and Collections",
        "Ansible Vault",
        "Best Practices",
        "Ansible Interview Deep Dive"
    ],
    "azure": [
        "Azure Fundamentals",
        "Compute Services",
        "Storage Services",
        "Networking VNet",
        "Azure Kubernetes Service",
        "Azure DevOps",
        "ARM Templates and Bicep",
        "Security and Identity",
        "Monitoring",
        "Azure Interview Deep Dive"
    ],
    "aws": [
        "AWS Fundamentals",
        "EC2 and Compute",
        "S3 and Storage",
        "VPC Networking",
        "IAM Security",
        "EKS Kubernetes",
        "Lambda Serverless",
        "CloudFormation",
        "Monitoring CloudWatch",
        "AWS Interview Deep Dive"
    ],
    "bash": [
        "Shell Basics",
        "Variables and Data Types",
        "Control Structures",
        "Functions",
        "File Operations",
        "Text Processing grep sed awk",
        "Process Management",
        "Best Practices",
        "Bash Interview Deep Dive"
    ],
    "python": [
        "Python Basics for DevOps",
        "File and System Operations",
        "Working with APIs",
        "AWS SDK boto3",
        "Azure SDK",
        "Automation Scripts",
        "Error Handling",
        "Testing with pytest",
        "Python Interview Deep Dive"
    ],
    "monitoring": [
        "Monitoring Fundamentals",
        "Prometheus Basics",
        "PromQL Queries",
        "Grafana Dashboards",
        "Alerting Strategies",
        "Log Aggregation ELK",
        "Datadog Integration",
        "APM Concepts",
        "Monitoring Interview Deep Dive"
    ],
    "cicd": [
        "CI CD Fundamentals",
        "GitHub Actions Basics",
        "GitHub Actions Advanced",
        "GitLab CI CD",
        "Jenkins Pipelines",
        "Artifact Management",
        "Deployment Strategies",
        "GitOps with ArgoCD",
        "Security Scanning",
        "CI CD Interview Deep Dive"
    ]
}

# Maximum retries for API calls
MAX_RETRIES = 3
RETRY_DELAY = 5  # seconds


def get_api_key() -> str:
    """Get Gemini API key from environment."""
    key = os.getenv("GEMINI_API_KEY")
    if not key:
        raise ValueError("❌ GEMINI_API_KEY environment variable not set")
    return key


def load_prompt() -> str:
    """Load the system prompt for content generation."""
    prompt_path = Path(__file__).parent.parent / "prompts" / "devops_content.txt"
    if prompt_path.exists():
        return prompt_path.read_text()
    return "You are a DevOps expert creating educational content."


def get_existing_content(topics_dir: Path) -> dict:
    """
    Scan existing content to determine progress.
    Returns the highest day number found for each topic.
    """
    progress = {}
    
    for topic in CURRICULUM.keys():
        topic_dir = topics_dir / topic
        if not topic_dir.exists():
            progress[topic] = 0
            continue
        
        # Find all day-XX files and extract day numbers
        max_day = 0
        for filepath in topic_dir.iterdir():
            if filepath.is_file():
                match = re.match(r'day-(\d+)', filepath.name)
                if match:
                    day_num = int(match.group(1))
                    max_day = max(max_day, day_num)
        
        progress[topic] = max_day
    
    return progress


def get_next_topic(progress: dict) -> tuple:
    """
    Determine the next topic to generate based on progress.
    Returns: (topic_name, day_number, subtopic_name)
    """
    topic_order = list(CURRICULUM.keys())
    
    for topic in topic_order:
        current_day = progress.get(topic, 0)
        subtopics = CURRICULUM[topic]
        
        if current_day < len(subtopics):
            next_day = current_day + 1
            subtopic = subtopics[current_day]
            return topic, next_day, subtopic
    
    # All topics complete - cycle back
    print("🔄 All topics completed! Starting new cycle...")
    return topic_order[0], 1, CURRICULUM[topic_order[0]][0]


def slugify(text: str) -> str:
    """Convert text to URL-friendly slug."""
    if not text:
        return "content"
    slug = text.lower().strip()
    slug = re.sub(r'[^a-z0-9\s-]', '', slug)
    slug = re.sub(r'[\s_]+', '-', slug)
    slug = re.sub(r'-+', '-', slug)
    slug = slug.strip('-')
    return slug[:50] if slug else "content"


def validate_content(content: str) -> bool:
    """Validate that generated content is valid and complete."""
    if not content or len(content) < 500:
        print(f"❌ Content too short: {len(content)} chars")
        return False
    
    if not content.strip().startswith('---'):
        print("❌ Missing front matter")
        return False
    
    required_markers = ['#', 'day:', 'category:']
    for marker in required_markers:
        if marker not in content.lower():
            print(f"❌ Missing required marker: {marker}")
            return False
    
    print(f"✅ Content validation passed ({len(content)} chars)")
    return True


def generate_content(topic: str, day: int, subtopic: str) -> str:
    """Generate content using Gemini API with retry logic."""
    api_key = get_api_key()
    genai.configure(api_key=api_key)
    
    model = genai.GenerativeModel(
        model_name="gemini-2.0-flash",
        system_instruction=load_prompt()
    )
    
    today = datetime.now().strftime("%Y-%m-%d")
    
    prompt = f"""Generate DevOps learning content for:

Topic: {topic.capitalize()}
Day: {day}
Subtopic: {subtopic}
Date: {today}

Create comprehensive but concise notes following the template in your instructions.
Include:
1. Core concepts explanation
2. Practical commands/examples
3. 5-7 interview questions with answers
4. 2-3 scenario-based questions
5. 1-2 architecture/design questions

Use this EXACT front matter format:
---
layout: topic
title: {subtopic}
category: {topic}
day: {day}
date: {today}
description: {topic.capitalize()} - {subtopic}
---

Output ONLY the Markdown content starting with the front matter, nothing else."""

    last_error = None
    
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            print(f"🔄 API call attempt {attempt}/{MAX_RETRIES}...")
            
            response = model.generate_content(
                prompt,
                generation_config=genai.types.GenerationConfig(
                    temperature=0.3,
                    max_output_tokens=8000,
                )
            )
            
            content = response.text
            
            if validate_content(content):
                return content
            else:
                print(f"⚠️ Attempt {attempt}: Content validation failed, retrying...")
                last_error = "Content validation failed"
                
        except Exception as e:
            last_error = str(e)
            print(f"⚠️ Attempt {attempt} failed: {e}")
        
        if attempt < MAX_RETRIES:
            print(f"⏳ Waiting {RETRY_DELAY}s before retry...")
            time.sleep(RETRY_DELAY)
    
    raise RuntimeError(f"❌ Failed after {MAX_RETRIES} attempts. Last error: {last_error}")


def save_content(topics_dir: Path, topic: str, day: int, subtopic: str, content: str) -> Path:
    """Save generated content to file."""
    topic_dir = topics_dir / topic
    topic_dir.mkdir(parents=True, exist_ok=True)
    
    slug = slugify(subtopic)
    filename = f"day-{day:02d}-{slug}.html"
    filepath = topic_dir / filename
    
    # Safety check for existing file
    if filepath.exists():
        print(f"⚠️ File already exists: {filepath}")
        timestamp = datetime.now().strftime("%H%M%S")
        filename = f"day-{day:02d}-{slug}-{timestamp}.html"
        filepath = topic_dir / filename
    
    filepath.write_text(content)
    print(f"✅ Created: {filepath}")
    return filepath


def update_topic_index(topics_dir: Path, topic: str, day: int, filename: str):
    """Update the topic's index.html to unlock the newly created day."""
    index_path = topics_dir / topic / "index.html"
    if not index_path.exists():
        print(f"⚠️ No index.html found for {topic} - skipping index update")
        return
    
    content = index_path.read_text()
    day_str = f"{day:02d}"
    
    old_pattern = f'''<li class="locked">
                                <a href="#">
                                    <span class="day-number">{day_str}</span>'''
    
    new_pattern = f'''<li class="active">
                                <a href="{filename}">
                                    <span class="day-number">{day_str}</span>'''
    
    if old_pattern in content:
        content = content.replace(old_pattern, new_pattern)
        
        parts = content.split(new_pattern)
        if len(parts) > 1:
            second_part = parts[1]
            second_part = second_part.replace('fa-lock', 'fa-check-circle', 1)
            content = new_pattern.join([parts[0], second_part])
        
        index_path.write_text(content)
        print(f"✅ Updated {topic}/index.html - Day {day} unlocked")
    else:
        print(f"ℹ️ Day {day} entry not found or already unlocked in {topic}/index.html")


def main():
    """Main entry point."""
    print("=" * 60)
    print("🚀 DevOps Learning Hub - Content Generator")
    print(f"📅 Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)
    
    script_dir = Path(__file__).parent
    devops_dir = script_dir.parent
    topics_dir = devops_dir / "topics"
    
    print(f"\n📁 Topics directory: {topics_dir}")
    
    if not topics_dir.exists():
        print(f"❌ Topics directory not found: {topics_dir}")
        sys.exit(1)
    
    # Get progress
    progress = get_existing_content(topics_dir)
    print("\n📊 Current Progress:")
    total_days = 0
    total_possible = 0
    for topic, days in progress.items():
        topic_total = len(CURRICULUM.get(topic, []))
        total_days += days
        total_possible += topic_total
        status = "✅" if days == topic_total else "🔄"
        print(f"  {status} {topic}: {days}/{topic_total} days")
    
    print(f"\n📈 Overall: {total_days}/{total_possible} days completed")
    
    # Determine next topic
    topic, day, subtopic = get_next_topic(progress)
    print(f"\n📝 Next Content: {topic.capitalize()} - Day {day}: {subtopic}")
    
    # Generate content
    try:
        print("\n🔧 Generating content...")
        content = generate_content(topic, day, subtopic)
        
        print("\n💾 Saving content...")
        filepath = save_content(topics_dir, topic, day, subtopic, content)
        
        print("\n🔓 Updating topic index...")
        update_topic_index(topics_dir, topic, day, filepath.name)
        
        print("\n" + "=" * 60)
        print("✨ SUCCESS! Content generated and saved!")
        print(f"📄 File: {filepath}")
        print(f"🏷️ Topic: {topic} | Day: {day} | Subtopic: {subtopic}")
        print("=" * 60)
        
        return str(filepath)
        
    except Exception as e:
        print("\n" + "=" * 60)
        print(f"❌ FAILED: {e}")
        print("=" * 60)
        sys.exit(1)


if __name__ == "__main__":
    main()
