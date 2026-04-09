"""
DevOps Learning Hub - Daily Content Generator

Uses Google Gemini to generate daily DevOps learning content.
Automatically determines the next topic based on existing content.
"""

import os
import json
from datetime import datetime
from pathlib import Path

try:
    import google.generativeai as genai
except ImportError:
    print("Please install google-generativeai: pip install google-generativeai")
    exit(1)


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


def get_api_key() -> str:
    """Get Gemini API key from environment."""
    key = os.getenv("GEMINI_API_KEY")
    if not key:
        raise ValueError("GEMINI_API_KEY environment variable not set")
    return key


def load_prompt() -> str:
    """Load the system prompt for content generation."""
    prompt_path = Path(__file__).parent.parent / "prompts" / "devops_content.txt"
    if prompt_path.exists():
        return prompt_path.read_text()
    return "You are a DevOps expert creating educational content."


def get_existing_content(topics_dir: Path) -> dict:
    """Scan existing content to determine progress."""
    progress = {}
    
    for topic in CURRICULUM.keys():
        topic_dir = topics_dir / topic
        if not topic_dir.exists():
            progress[topic] = 0
            continue
        
        # Count day-XX files
        day_files = list(topic_dir.glob("day-*.md"))
        progress[topic] = len(day_files)
    
    return progress


def get_next_topic(progress: dict) -> tuple[str, int, str]:
    """
    Determine the next topic to generate based on progress.
    Returns: (topic_name, day_number, subtopic_name)
    """
    # Order of topics
    topic_order = list(CURRICULUM.keys())
    
    for topic in topic_order:
        current_day = progress.get(topic, 0)
        subtopics = CURRICULUM[topic]
        
        if current_day < len(subtopics):
            # This topic still has content to generate
            next_day = current_day + 1
            subtopic = subtopics[current_day]
            return topic, next_day, subtopic
    
    # All topics complete - cycle back
    return topic_order[0], 1, CURRICULUM[topic_order[0]][0]


def generate_content(topic: str, day: int, subtopic: str) -> str:
    """Generate content using Gemini API."""
    api_key = get_api_key()
    genai.configure(api_key=api_key)
    
    model = genai.GenerativeModel(
        model_name="gemini-2.5-flash",
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

Use this front matter:
---
layout: topic
title: {subtopic}
category: {topic}
day: {day}
date: {today}
description: {topic.capitalize()} - {subtopic}
---

Output ONLY the Markdown content, nothing else."""

    response = model.generate_content(
        prompt,
        generation_config=genai.types.GenerationConfig(
            temperature=0.3,
            max_output_tokens=4000,
        )
    )
    
    return response.text


def save_content(topics_dir: Path, topic: str, day: int, content: str):
    """Save generated content to file."""
    topic_dir = topics_dir / topic
    topic_dir.mkdir(parents=True, exist_ok=True)
    
    # Create filename
    filename = f"day-{day:02d}-{slugify(content)}.md"
    filepath = topic_dir / filename
    
    filepath.write_text(content)
    print(f"✅ Created: {filepath}")
    return filepath


def slugify(content: str) -> str:
    """Extract slug from content title."""
    # Try to extract title from front matter
    lines = content.split('\n')
    for line in lines:
        if line.startswith('title:'):
            title = line.replace('title:', '').strip()
            # Convert to slug
            slug = title.lower()
            slug = slug.replace(' ', '-')
            slug = ''.join(c for c in slug if c.isalnum() or c == '-')
            return slug[:50]  # Limit length
    return "content"


def main():
    """Main entry point."""
    print("🚀 DevOps Learning Hub - Content Generator")
    print("=" * 50)
    
    # Paths
    script_dir = Path(__file__).parent
    devops_dir = script_dir.parent
    topics_dir = devops_dir / "topics"
    
    # Get progress
    progress = get_existing_content(topics_dir)
    print("\n📊 Current Progress:")
    for topic, days in progress.items():
        total = len(CURRICULUM.get(topic, []))
        print(f"  {topic}: {days}/{total} days")
    
    # Determine next topic
    topic, day, subtopic = get_next_topic(progress)
    print(f"\n📝 Generating: {topic.capitalize()} - Day {day}: {subtopic}")
    
    # Generate content
    try:
        content = generate_content(topic, day, subtopic)
        filepath = save_content(topics_dir, topic, day, content)
        print(f"\n✨ Content generated successfully!")
        return str(filepath)
    except Exception as e:
        print(f"\n❌ Error generating content: {e}")
        raise


if __name__ == "__main__":
    main()
