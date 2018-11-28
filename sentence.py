class Sentence():
    def __init__(self, struct, words):
        self.eng = " ".join(f"{n.meaning}.{t}" for t, n in zip(struct, words))
        self.whole = " ".join(str(n) for n in words)
        
    def __str__(self):
        return self.whole

    def __repr__(self):
        return f"Sentence({self.eng})"
