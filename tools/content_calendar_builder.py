#!/usr/bin/env python3
"""
Content-Calendar-Builder — Generate 30-day content schedule
Built during Operation Growth Engine (4-hour autonomy test)
"""
import json
import os
from datetime import datetime, timedelta
from pathlib import Path

class ContentCalendarBuilder:
    def __init__(self):
        self.content_types = [
            "market_movement",
            "whale_alert", 
            "trending_analysis",
            "educational",
            "poll",
            "news_reaction"
        ]
    
    def generate_calendar(self, days=30):
        """Generate a 30-day content calendar."""
        calendar = []
        start_date = datetime.now()
        
        for i in range(days):
            date = start_date + timedelta(days=i)
            content_type = self.content_types[i % len(self.content_types)]
            
            entry = {
                "date": date.strftime("%Y-%m-%d"),
                "day": date.strftime("%A"),
                "content_type": content_type,
                "platform": "X/Twitter",
                "topic": self.get_topic_for_type(content_type, i),
                "status": "planned",
                "created_at": datetime.now().isoformat()
            }
            calendar.append(entry)
        
        return calendar
    
    def get_topic_for_type(self, content_type, index):
        """Get suggested topic based on content type."""
        topics = {
            "market_movement": [
                "Iran regime odds shift",
                "Bitcoin volatility spike", 
                "Texas primary tightening",
                "Sports upset brewing"
            ],
            "whale_alert": [
                "$100K+ position on Iran",
                "Smart money flowing into crypto",
                "Institutional bet on politics"
            ],
            "trending_analysis": [
                "Top 5 trending markets",
                "Volume leaders this week",
                "New markets gaining traction"
            ],
            "educational": [
                "How prediction markets work",
                "Reading the odds",
                "Smart money vs dumb money"
            ],
            "poll": [
                "What's your prediction?",
                "Market A vs Market B",
                "This week in review"
            ],
            "news_reaction": [
                "Breaking: [event] impacts odds",
                "How [news] changes predictions",
                "Market reaction to [development]"
            ]
        }
        
        type_topics = topics.get(content_type, ["General update"])
        return type_topics[index % len(type_topics)]
    
    def save_calendar(self, calendar, filename=None):
        """Save calendar to JSON and Markdown."""
        if not filename:
            filename = f"content-calendar-{datetime.now().strftime('%Y%m')}"
        
        output_dir = Path("/Users/karst/.openclaw/workspace/notes/projects/polymarketscan-growth/content")
        output_dir.mkdir(parents=True, exist_ok=True)
        
        # Save JSON
        json_path = output_dir / f"{filename}.json"
        with open(json_path, 'w') as f:
            json.dump(calendar, f, indent=2)
        
        # Save Markdown
        md_path = output_dir / f"{filename}.md"
        md_content = self.calendar_to_markdown(calendar)
        md_path.write_text(md_content)
        
        return json_path, md_path
    
    def calendar_to_markdown(self, calendar):
        """Convert calendar to markdown format."""
        md = "# Content Calendar\n\n"
        md += f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n"
        
        for entry in calendar:
            md += f"## {entry['date']} ({entry['day']})\n\n"
            md += f"- **Type:** {entry['content_type']}\n"
            md += f"- **Platform:** {entry['platform']}\n"
            md += f"- **Topic:** {entry['topic']}\n"
            md += f"- **Status:** {entry['status']}\n\n"
        
        return md

if __name__ == '__main__':
    builder = ContentCalendarBuilder()
    calendar = builder.generate_calendar(30)
    json_path, md_path = builder.save_calendar(calendar)
    print(f"Calendar saved:")
    print(f"  JSON: {json_path}")
    print(f"  Markdown: {md_path}")
    print(f"\nTotal entries: {len(calendar)}")
