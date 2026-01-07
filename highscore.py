import json
import os
from typing import List, Dict

HIGHSCORE_FILE = "highscores.json"

class HighscoreManager:
    def __init__(self, max_entries=10):
        self.max_entries = max_entries
        self.highscores = self.load_highscores()
    
    def load_highscores(self) -> List[Dict[str, any]]:
        """Load highscores from JSON file"""
        if os.path.exists(HIGHSCORE_FILE):
            try:
                with open(HIGHSCORE_FILE, 'r') as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError):
                return []
        return []
    
    def save_highscores(self):
        """Save highscores to JSON file"""
        try:
            with open(HIGHSCORE_FILE, 'w') as f:
                json.dump(self.highscores, f, indent=2)
        except IOError as e:
            print(f"Error saving highscores: {e}")
    
    def add_score(self, name: str, score: int):
        """Add a new score to the highscore list"""
        self.highscores.append({
            'name': name,
            'score': score
        })
        # Sort by score (descending)
        self.highscores.sort(key=lambda x: x['score'], reverse=True)
        # Keep only top entries
        self.highscores = self.highscores[:self.max_entries]
        self.save_highscores()
    
    def is_highscore(self, score: int) -> bool:
        """Check if a score qualifies as a highscore"""
        if len(self.highscores) < self.max_entries:
            return True
        return score > self.highscores[-1]['score']
    
    def get_highscores(self) -> List[Dict[str, any]]:
        """Get the list of highscores"""
        return self.highscores
