import json
import os

HIGHSCORE_FILE = "highscores.json"

class HighscoreManager:
    def __init__(self):
        self.highscores = []
        self.load_highscores()
    
    def load_highscores(self):
        """Laad highscores uit het JSON bestand"""
        if os.path.exists(HIGHSCORE_FILE):
            try:
                with open(HIGHSCORE_FILE, 'r') as f:
                    self.highscores = json.load(f)
            except:
                self.highscores = []
        else:
            self.highscores = []
    
    def save_highscores(self):
        """Sla highscores op in het JSON bestand"""
        with open(HIGHSCORE_FILE, 'w') as f:
            json.dump(self.highscores, f, indent=2)
    
    def add_score(self, name, score):
        """Voeg een nieuwe score toe"""
        self.highscores.append({"name": name, "score": score})
        # Sorteer op score (hoogste eerst)
        self.highscores.sort(key=lambda x: x["score"], reverse=True)
        # Houd alleen de top 10
        self.highscores = self.highscores[:10]
        self.save_highscores()
    
    def get_highscores(self):
        """Geef de highscores terug"""
        return self.highscores
    
    def is_highscore(self, score):
        """Check of een score een highscore is (top 10)"""
        if len(self.highscores) < 10:
            return True
        return score > self.highscores[-1]["score"]
